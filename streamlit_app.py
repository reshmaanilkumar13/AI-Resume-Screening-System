import streamlit as st
import os
from app import process_resumes

st.set_page_config(page_title="AI Resume Screening System", layout="wide")

st.title("🤖 AI Resume Screening & Ranking System")

resume_folder = "data/resumes"

job_description = st.text_area("Paste Job Description Here")

if st.button("Run Screening"):

    if job_description.strip() == "":
        st.warning("Please enter a job description.")
    else:
        with st.spinner("Processing resumes..."):
            results = process_resumes(resume_folder, job_description)

        st.success("Screening Complete ✅")

        for rank, (filename, score, skills, status) in enumerate(results, start=1):
            st.markdown(f"### {rank}. {filename}")
            st.write(f"Score: {score}%")
            st.write(f"Status: {status}")
            st.write("Matched Skills:", ", ".join(skills))
            st.write("---")