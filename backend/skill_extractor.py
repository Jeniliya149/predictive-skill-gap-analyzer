import pandas as pd
import os
import re

# -------------------------
# Dataset Path
# -------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATASET_PATH = os.path.join(BASE_DIR, "dataset", "jobs.csv")

df = pd.read_csv(DATASET_PATH)

# -------------------------
# Text Normalization
# -------------------------

def normalize(text):
    return text.lower().strip()


# -------------------------
# Build Skill → Role Map
# -------------------------

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

    text = re.sub(r"[^a-z0-9\s]", " ", text)

    role_score = {}

    for skill, role in skill_role_map.items():

        pattern = r"\b" + re.escape(skill) + r"\b"

        if re.search(pattern, text):

            if role not in role_score:
                role_score[role] = 0

            role_score[role] += 1

    if not role_score:
        return "Unknown"

    # Return role with highest matching skills
    return max(role_score, key=role_score.get)


# -------------------------
# Extract Skills
# -------------------------

def extract_skills(text):

    text = normalize(text)

    text = re.sub(r"[^a-z0-9\s]", " ", text)

    extracted = []

    for skill in skill_role_map.keys():

        pattern = r"\b" + re.escape(skill) + r"\b"

        if re.search(pattern, text):
            extracted.append(skill)

    return sorted(list(set(extracted)))
