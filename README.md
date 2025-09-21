# 📄 Resume Relevance Checker  
🏆 Team Name: CodeCrafters

👤 Team / Participant Details

Name: Akumarthi Mounika

Email: 22h41a4502mounika@gmail.com

Contact: +91 9618946102

College: Bonam Venkata Chalamayya Institute of Technology and Science

Year of Pass-out: 2026
[![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)](https://www.python.org/)  
[![Streamlit](https://img.shields.io/badge/Streamlit-Deployed-brightgreen?logo=streamlit)](https://streamlit.io/)  
[![GitHub stars](https://img.shields.io/github/stars/mouniak4502/resume-checker?style=social)](https://github.com/mouniak4502/resume-checker)  

A **Resume Relevance Checker** built using **Python + Streamlit**.  
Upload your **resume (PDF/DOCX)** and a **job description (JD)**, and the app will:  
✅ Extract text  
✅ Compare resume skills with JD skills  
✅ Generate a **score (0–100%)**  
✅ Provide a **verdict (Good Match / Partial Match / Needs Improvement)**  
✅ Show interactive visualizations 📊  

🔗 **Live Demo:** [Resume Relevance Checker App](https://resume-checker-jfb6yzob5kbg4detmgztfy.streamlit.app/)  

---

## 🚀 Problem Statement  
Job seekers often struggle to know how well their resume matches a job description.  
This project helps **automatically evaluate resume–JD relevance**, saving time for both candidates and recruiters.  

---

## ✨ Features  
- 📂 Upload Resume (`.pdf` or `.docx`)  
- 📜 Upload Job Description (`.txt` or `.docx`)  
- 🧠 Skill extraction using **NLP**  
- 📊 Visual score breakdown (bar chart, pie chart)  
- 🎯 Final **Verdict** on match quality  
- 🖌️ Custom dark theme UI  

---

## ⚙️ How to Run Locally  

Clone the repo:  
```bash
Install dependencies:

pip install -r requirements.txt
Run the app:

streamlit run app.py
git clone https://github.com/mouniak4502/resume-checker.git
cd resume-checker
🌍 Deployed App

👉 Click here to use the app
from graphviz import Digraph

# Create a flow diagram with colors and icons
dot = Digraph("Resume_Relevance_Checker", format="png")

dot.attr(rankdir="LR", size="8,5")
dot.attr("node", shape="box", style="filled", fontname="Helvetica", fontsize="12")

# Nodes with colors
dot.node("A", "Upload Resume\n(PDF/DOCX)", fillcolor="#4C9AFF", fontcolor="white")
dot.node("B", "Upload Job Description\n(TXT/DOCX)", fillcolor="#36B37E", fontcolor="white")
dot.node("C", "Extract Text\n(Parsing)", fillcolor="#FFAB00", fontcolor="black")
dot.node("D", "Extract Skills\n(NLP)", fillcolor="#FF5630", fontcolor="white")
dot.node("E", "Compare Resume & JD\n(Skill Matching)", fillcolor="#6554C0", fontcolor="white")
dot.node("F", "Generate Score\n(0-100%)", fillcolor="#00B8D9", fontcolor="white")
dot.node("G", "Verdict\n(Good/Partial/Needs Improvement)", fillcolor="#172B4D", fontcolor="white")
dot.node("H", "Interactive Visualizations\n(Charts & Graphs)", fillcolor="#FF6F61", fontcolor="white")

# Edges
dot.edges(["AC", "BC"])
dot.edge("C", "D")
dot.edge("D", "E")
dot.edge("E", "F")
dot.edge("F", "G")
dot.edge("F", "H")

# Save diagram
output_path = "/mnt/data/resume_checker_flow_diagram_colored"
dot.render(output_path, cleanup=True)

output_path + ".png"
