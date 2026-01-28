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
    "ai","artificial intelligence","machine learning",

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

    # SOFTWARE ENGINEER
    if any(k in text for k in [
        "software", "programming", "developer", "java", "python", "devops"
    ]):
        return "Software Engineer"

    # CIVIL ENGINEER
    if any(k in text for k in [
        "civil", "construction", "autocad", "staad", "bim"
    ]):
        return "Civil Engineer"

    # MECHANICAL ENGINEER
    if any(k in text for k in [
        "mechanical", "manufacturing", "cnc", "solidworks", "robotics"
    ]):
        return "Mechanical Engineer"

    # ECE ENGINEER
    if any(k in text for k in [
        "ece", "embedded", "iot", "vlsi", "edge computing"
    ]):
        return "ECE Engineer"

    # EEE ENGINEER
    if any(k in text for k in [
        "eee", "power systems", "plc", "smart grids"
    ]):
        return "EEE Engineer"

    # LAW
    if any(k in text for k in [
        "law", "legal", "court", "case"
    ]):
        return "Law Professional"

    # BUSINESS
    if any(k in text for k in [
        "business", "mba", "finance", "marketing", "management"
    ]):
        return "Business Professional"

    # HEALTH
    if any(k in text for k in [
        "medical", "health", "clinical", "patient"
    ]):
        return "Health Professional"

    # SCIENCE
    if any(k in text for k in [
        "science", "research", "laboratory", "simulation", "data analysis"
    ]):
        return "Science Professional"

    # ARTS
    if any(k in text for k in [
        "design", "ui", "ux", "media", "arts"
    ]):
        return "Arts Professional"

    # EDUCATION
    if any(k in text for k in [
        "teacher", "teaching", "education", "e learning", "online learning"
    ]):
        return "Education Professional"

    return "General"
