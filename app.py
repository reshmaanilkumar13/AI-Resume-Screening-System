import os
import csv
from resume_parser import extract_resume_text
from utils import clean_text
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer('all-MiniLM-L6-v2')

required_skills = [
    "python", "machine learning", "scikit-learn",
    "numpy", "pandas", "mysql",
    "git", "github", "html", "css", "javascript"
]

SHORTLIST_THRESHOLD = 50

def process_resumes(resume_folder, job_description_text):

    cleaned_job = clean_text(job_description_text)
    job_embedding = model.encode(cleaned_job)

    results = []

    for filename in os.listdir(resume_folder):
        if filename.endswith(".pdf"):
            file_path = os.path.join(resume_folder, filename)

            text = extract_resume_text(file_path)
            cleaned_resume = clean_text(text)

            # Semantic similarity
            resume_embedding = model.encode(cleaned_resume)
            similarity = cosine_similarity(
                [resume_embedding],
                [job_embedding]
            )[0][0]

            semantic_score = round(similarity * 100, 2)

            # Skill matching
            matched_skills = [
                skill for skill in required_skills
                if skill in cleaned_resume
            ]

            skill_score = (len(matched_skills) / len(required_skills)) * 100

            # Experience bonus
            experience_bonus = 0
            if "internship" in cleaned_resume:
                experience_bonus += 5
            if "project" in cleaned_resume:
                experience_bonus += 5
            if "experience" in cleaned_resume:
                experience_bonus += 5

            # Final score
            final_score = round(
                (0.6 * semantic_score) +
                (0.3 * skill_score) +
                (0.1 * experience_bonus),
                2
            )

            status = "Shortlisted" if final_score >= SHORTLIST_THRESHOLD else "Rejected"

            results.append((filename, final_score, matched_skills, status))

    results.sort(key=lambda x: x[1], reverse=True)

    return results