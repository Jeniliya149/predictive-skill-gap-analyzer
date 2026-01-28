import pandas as pd
import os

# Absolute path to dataset (deployment-safe)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATASET_PATH = os.path.join(BASE_DIR, "dataset", "jobs.csv")

def predict_future_skills(role):
    """
    Predict future skills strictly based on historical trend
    in jobs.csv for the given job_role.
    """

    try:
        df = pd.read_csv(DATASET_PATH)
    except Exception as e:
        print("Dataset load error:", e)
        return []

    # Filter by job role
    role_df = df[df["job_role"] == role]

    if role_df.empty:
        return []

    # Sort by year
    role_df = role_df.sort_values("year")

    # Take last 2 years only (trend-based, not fake)
    recent_years = role_df["year"].unique()[-2:]
    recent_df = role_df[role_df["year"].isin(recent_years)]

    skill_set = set()

    for skills in recent_df["skills"]:
        for skill in skills.split(","):
            skill_set.add(skill.strip())

    return sorted(skill_set)
