# 📄 Resume Relevance Checker  

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
