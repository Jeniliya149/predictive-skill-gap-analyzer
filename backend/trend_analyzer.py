import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATASET_PATH = os.path.join(BASE_DIR, "dataset", "jobs.csv")

def predict_future_skills(job_role):
    """
    Predict future skills using last 3 years (2023–2025)
    based on job role only.
    """

    df = pd.read_csv(DATASET_PATH)

    role_df = df[df["job_role"] == job_role]

    if role_df.empty:
        return []

    latest_year = role_df["year"].max()
    recent_df = role_df[role_df["year"] >= latest_year - 2]

    future_skills = set()

    for skills in recent_df["skills"]:
        for skill in skills.split(","):
            future_skills.add(skill.strip())

    return sorted(list(future_skills))



