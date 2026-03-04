import re
import pandas as pd
import os


# -------------------------
# Normalize text
# -------------------------
def normalize(text):
    return text.lower().strip()


# -------------------------
# Dataset Path
# -------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATASET_PATH = os.path.join(BASE_DIR, "dataset", "jobs.csv")


# -------------------------
# Load dataset
# -------------------------
df = pd.read_csv(DATASET_PATH)

# Build skill → role mapping automatically
skill_role_map = {}

for _, row in df.iterrows():
    role = row["job_role"].strip()
    skills = row["skills"].split(",")

    for skill in skills:
        skill = skill.strip().lower()
        skill_role_map[skill] = role


# -------------------------
# Detect Experience Level
# -------------------------
def detect_experience(text):
    text = normalize(text)

    if "senior" in text:
        return "senior"
    elif "mid" in text or "experienced" in text:
        return "mid"
    elif "junior" in text:
        return "junior"
    elif "fresher" in text or "student" in text:
        return "fresher"

    return "unknown"


# -------------------------
# Detect Job Role
# -------------------------
def detect_branch(text):
    text = normalize(text)

    # Remove special characters
    text = re.sub(r"[^a-z0-9\s]", " ", text)

    for skill, role in skill_role_map.items():
        if skill in text:
            return role

    return "Unknown"


# -------------------------
# Extract Skills
# -------------------------
def extract_skills(text):
    text = normalize(text)

    # Remove special characters
    text = re.sub(r"[^a-z0-9\s]", " ", text)

    extracted = []

    for skill in skill_role_map.keys():
        if skill in text:
            extracted.append(skill)

    return sorted(list(set(extracted)))
