import streamlit as st
import os
import zipfile
import tempfile
import pandas as pd
import plotly.express as px

# Import helper modules (make sure these files exist and work)
from resume_parser import extract_text_pdf, extract_text_docx
from jd_parser import extract_skills
from score_engine import calculate_score, verdict

# ------------------- PAGE CONFIG -------------------
st.set_page_config(
    page_title="Resume Relevance Checker",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ------------------- CUSTOM CSS -------------------
st.markdown("""
    <style>
        /* 🌈 Global gradient background */
        .stApp {
            background: linear-gradient(135deg, #fceabb, #f8b500);
            color: #222222;
            font-family: 'Segoe UI', sans-serif;
        }
        h1, h2, h3, h4 {
            color: #4a148c !important;
        }
        /* Sidebar styling */
        section[data-testid="stSidebar"] {
            background: #1b4332 !important;
        }
        section[data-testid="stSidebar"] * {
            color: #fefae0 !important;
            font-weight: 600 !important;
        }
        /* File uploader label */
        [data-testid="stFileUploader"] label {
            color: #4a148c !important;
            font-weight: 600;
        }
        /* Info/Warning/Success/Dashboard messages */
        [data-testid="stNotification"] {
            background: linear-gradient(135deg, #ffecd2, #fcb69f) !important;
            color: #4e342e !important;
            font-weight: bold !important;
            border-radius: 10px;
            padding: 1rem;
        }
        /* Data table font color */
        .stDataFrame div {
            color: #003049 !important;
            font-weight: 500 !important;
        }
        /* Buttons */
        div.stButton > button {
            background: linear-gradient(to right, #ff6f61, #6a1b9a);
            color: white !important;
            border: none;
            border-radius: 8px;
            padding: 0.6em 1.2em;
            font-weight: 600;
            cursor: pointer;
            transition: 0.3s;
        }
        div.stButton > button:hover {
            transform: scale(1.05);
            background: linear-gradient(to right, #6a1b9a, #ff6f61);
        }
        /* Footer */
        #footer {
            position: fixed;
            bottom: 0;
            width: 100%;
            text-align: center;
            color: #4a148c !important;
            padding: 0.5rem;
            font-size: 0.9rem;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

# ------------------- GLOBAL STATE -------------------
if "jd_text" not in st.session_state:
    st.session_state.jd_text = ""
if "jd_skills" not in st.session_state:
    st.session_state.jd_skills = []
if "results" not in st.session_state:
    st.session_state.results = []

# ------------------- FUNCTIONS -------------------
def save_and_extract_resumes(uploaded_files):
    """Handles PDF/DOCX/ZIP uploads and extracts text"""
    extracted = []
    for uploaded_file in uploaded_files:
        filename = uploaded_file.name
        suffix = os.path.splitext(filename)[-1].lower()

        if suffix == ".zip":
            with tempfile.TemporaryDirectory() as tmpdir:
                zip_path = os.path.join(tmpdir, filename)
                with open(zip_path, "wb") as f:
                    f.write(uploaded_file.getbuffer())
                with zipfile.ZipFile(zip_path, "r") as zip_ref:
                    zip_ref.extractall(tmpdir)
                for f in os.listdir(tmpdir):
                    fpath = os.path.join(tmpdir, f)
                    if f.lower().endswith(".pdf"):
                        text = extract_text_pdf(fpath)
                        extracted.append((f, text))
                    elif f.lower().endswith(".docx"):
                        text = extract_text_docx(fpath)
                        extracted.append((f, text))
        elif suffix == ".pdf":
            text = extract_text_pdf(uploaded_file)
            extracted.append((filename, text))
        elif suffix == ".docx":
            text = extract_text_docx(uploaded_file)
            extracted.append((filename, text))
    return extracted

def analyze_resumes(resumes, jd_text, jd_skills):
    """Compare resumes with JD and return results"""
    results = []
    for name, text in resumes:
        score = calculate_score(text, jd_text, jd_skills)
        verdict_label = verdict(score)
        results.append({
            "Name": name,
            "Score": score,  # ensure 0–100 score is added
            "Verdict": verdict_label,
            "Extracted Text": text
        })
    return pd.DataFrame(results)

# ------------------- SIDEBAR NAV -------------------
st.sidebar.title("📂 Navigation")
page = st.sidebar.radio(
    "Go to",
    ["🏠 Home", "ℹ️ About", "📑 Upload JD", "📂 Upload Resumes", "📊 Dashboard"]
)

# ------------------- HOME PAGE -------------------
if page == "🏠 Home":
    st.title("📄 Automated Resume Relevance Check System")
    st.markdown("""
        Welcome to the **Automated Resume Relevance Checker**.  
        This system helps recruiters quickly match resumes with job descriptions.  

        ✅ Upload Job Description  
        ✅ Upload Resumes (PDF/DOCX/ZIP)  
        ✅ Get **Relevance Scores** (0–100)  
        ✅ Identify Missing Skills  
        ✅ See **High / Medium / Low Fit Verdicts**  
        ✅ Export results for placement team  

        ---
    """)

# ------------------- ABOUT PAGE -------------------
elif page == "ℹ️ About":
    st.title("ℹ️ About This Project")
    st.markdown("""
        The **Resume Relevance Checker** was developed to solve the problem of manual, 
        time-consuming resume evaluations in placement processes.  

        🔹 **Problem:** Recruiters spend hours shortlisting resumes manually.  
        🔹 **Solution:** Automate resume scoring & skill gap identification.  
        🔹 **Outcome:** Faster, consistent, and fair evaluations.  

        ---
        Developed by **Mounika**
    """)

# ------------------- UPLOAD JD -------------------
elif page == "📑 Upload JD":
    st.title("📑 Upload Job Description")
    jd_file = st.file_uploader("Upload Job Description File (PDF/DOCX/TXT)", type=["pdf", "docx", "txt"])
    if jd_file:
        suffix = os.path.splitext(jd_file.name)[-1].lower()
        if suffix == ".pdf":
            text = extract_text_pdf(jd_file)
        elif suffix == ".docx":
            text = extract_text_docx(jd_file)
        else:
            text = jd_file.read().decode("utf-8")
        st.session_state.jd_text = text
        st.session_state.jd_skills = extract_skills(text)

        st.subheader("Extracted JD Skills:")
        st.write(", ".join(st.session_state.jd_skills))

# ------------------- UPLOAD RESUMES -------------------
elif page == "📂 Upload Resumes":
    st.title("📂 Upload Resumes")
    uploaded_files = st.file_uploader(
        "Upload Resume Files (PDF/DOCX or ZIP of resumes)",
        type=["pdf", "docx", "zip"],
        accept_multiple_files=True
    )
    if uploaded_files and st.session_state.jd_text:
        with st.spinner("⏳ Analyzing resumes..."):
            resumes = save_and_extract_resumes(uploaded_files)
            results_df = analyze_resumes(resumes, st.session_state.jd_text, st.session_state.jd_skills)
            st.session_state.results = results_df
        st.success("✅ Resumes processed successfully! Go to Dashboard to view results.")
    elif uploaded_files and not st.session_state.jd_text:
        st.warning("⚠️ Please upload a Job Description first!")

# ------------------- DASHBOARD -------------------
elif page == "📊 Dashboard":
    st.title("📊 Dashboard")

    if len(st.session_state.results) == 0:
        st.info("Upload JD and resumes to see results.")
    else:
        df = st.session_state.results.copy()

        # Top-N Filter
        top_filter = st.selectbox(
            "Filter candidates:",
            ["All", "Top 1", "Top 2", "Top 3", "Top 5", "Top 10"]
        )

        if top_filter != "All":
            n = int(top_filter.split()[1])
            df = df.sort_values("Score", ascending=False).head(n)

        # Display Results Table
        st.dataframe(df[["Name", "Score", "Verdict"]], use_container_width=True)

        # Download CSV
        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button(
            label="📥 Download Results CSV",
            data=csv,
            file_name="resume_results.csv",
            mime="text/csv"
        )

        # Charts
        col1, col2 = st.columns(2)
        with col1:
            fig1 = px.histogram(df, x="Score", nbins=10, title="Score Distribution", template="plotly_dark")
            st.plotly_chart(fig1, use_container_width=True, key="score_chart")
        with col2:
            verdict_counts = df["Verdict"].value_counts().reset_index()
            verdict_counts.columns = ["Verdict", "count"]
            fig2 = px.bar(verdict_counts,
                          x="Verdict", y="count",
                          color="Verdict",
                          title="Verdict Counts",
                          template="plotly_dark")
            st.plotly_chart(fig2, use_container_width=True, key="verdict_chart")

        # Resume Expanders
        st.subheader("📂 Resume Details")
        for i, row in df.iterrows():
            with st.expander(f"{row['Name']} — Score: {row['Score']} ({row['Verdict']})"):
                st.text_area("Extracted Resume Text", row["Extracted Text"], height=200)

# ------------------- FOOTER -------------------
st.markdown('<div id="footer">Developed by Mounika</div>', unsafe_allow_html=True)
