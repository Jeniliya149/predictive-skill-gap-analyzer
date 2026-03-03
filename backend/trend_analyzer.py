import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATASET_PATH = os.path.join(BASE_DIR, "dataset", "jobs.csv")


def predict_future_skills(job_role):
    """
    Predict future skills using last 3 years dynamically
    based on job role.
    """

    df = pd.read_csv(DATASET_PATH)

    # Clean column formatting safety
    df["job_role"] = df["job_role"].str.strip()

    role_df = df[df["job_role"] == job_role.strip()]

    if role_df.empty:
        return []

    latest_year = role_df["year"].max()
    recent_df = role_df[role_df["year"] >= latest_year - 2]

    future_skills = set()

    for skills in recent_df["skills"]:
        for skill in skills.split(","):
            future_skills.add(skill.strip())

    return sorted(future_skills)



