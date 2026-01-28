# backend/skill_extractor.py

import re

# normalize text into words
def normalize_text(text):
    text = text.lower()
    text = re.sub(r"[^\w\s]", " ", text)  # remove punctuation
    return text


def extract_skills(text):
    text = normalize_text(text)

    known_skills = [
        "c","java","python","sql","cloud","automation","devops",
        "autocad","bim","staad","construction planning",
        "solidworks","cnc","manufacturing","robotics",
        "embedded c","iot","vlsi","edge computing",
        "plc","smart grids","energy analytics",
        "legal writing","legal research","case analysis",
        "cyber law","legal analytics",
        "accounting","excel","finance","marketing","business analytics",
        "clinical skills","health informatics","digital health",
        "laboratory skills","simulation tools","computational methods",
        "design basics","digital design","ui ux","media technology",
        "teaching methods","e learning tools","digital pedagogy",
        "digital literacy"
    ]

    extracted = []

    for skill in known_skills:
        # match full word or full phrase
        pattern = r"\b" + re.escape(skill) + r"\b"
        if re.search(pattern, text):
            extracted.append(skill)

    return extracted

def detect_branch(text):
    text = text.lower()

    # DIRECT KEYWORDS (highest priority)
    if any(k in text for k in ["law", "legal", "court"]):
        return "Law Professional"

    if any(k in text for k in ["civil", "construction", "autocad", "staad", "bim"]):
        return "Civil Engineer"

    if any(k in text for k in ["mechanical", "cnc", "solidworks", "manufacturing", "robotics"]):
        return "Mechanical Engineer"

    if any(k in text for k in ["ece", "embedded", "vlsi", "iot", "edge computing"]):
        return "ECE Engineer"

    if any(k in text for k in ["eee", "plc", "smart grids", "power systems"]):
        return "EEE Engineer"

    if any(k in text for k in ["business", "mba", "finance", "marketing"]):
        return "Business Professional"

    if any(k in text for k in ["medical", "health", "clinical"]):
        return "Health Professional"

    if any(k in text for k in ["teacher", "teaching", "education"]):
        return "Education Professional"

    if any(k in text for k in ["design", "ui", "ux", "media"]):
        return "Arts Professional"

    if any(k in text for k in ["data analysis", "simulation", "research"]):
        return "Science Professional"

    # 🔥 SKILL-BASED INFERENCE (MOST IMPORTANT FIX)
    if any(k in text for k in ["c", "java", "python", "sql", "cloud", "devops"]):
        return "Software Engineer"

    # FALLBACK
    return "General"
