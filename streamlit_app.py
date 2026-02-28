import streamlit as st
from app import process_uploaded_resumes

st.set_page_config(page_title="AI Resume Screening System", layout="wide")

st.title("🤖 AI Resume Screening & Ranking System")

job_description = st.text_area("Paste Job Description Here")

uploaded_files = st.file_uploader(
    "Upload Resume PDFs",
    type=["pdf"],
    accept_multiple_files=True
)

if st.button("Run Screening"):

    if not job_description.strip():
        st.warning("Please enter a job description.")
    elif not uploaded_files:
        st.warning("Please upload at least one resume.")
    else:
        with st.spinner("Processing resumes..."):
            results = process_uploaded_resumes(uploaded_files, job_description)

        st.success("Screening Complete ✅")

        for rank, (filename, score, skills, status) in enumerate(results, start=1):
            st.markdown(f"### {rank}. {filename}")
            st.write(f"Score: {score}%")
            st.progress(float(score) / 100)
            st.write(f"Status: {status}")
            st.write("Matched Skills:", ", ".join(skills))
            st.write("---")
        import pandas as pd
        import matplotlib.pyplot as plt

        df = pd.DataFrame(results, columns=["Name", "Score", "Skills", "Status"])

        st.subheader("📊 Candidate Score Comparison")

        fig, ax = plt.subplots()
        ax.bar(df["Name"], df["Score"])
        ax.set_ylabel("Score (%)")
        ax.set_xticklabels(df["Name"], rotation=45, ha="right")

        st.pyplot(fig)