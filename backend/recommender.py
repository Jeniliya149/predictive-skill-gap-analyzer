# backend/recommender.py

DURATION = {
    "python":"6–8 weeks",
    "java":"6–8 weeks",
    "sql":"2–4 weeks",
    "cloud":"4–6 weeks",
    "devops":"8–12 weeks",
    "bim":"4–6 weeks",
    "robotics":"8–12 weeks",
    "cnc":"4–6 weeks",
    "embedded c":"4–6 weeks",
    "iot":"4–6 weeks",
    "cyber law":"4–6 weeks",
    "legal analytics":"4–6 weeks",
    "business analytics":"4–6 weeks",
    "digital health":"4–6 weeks",
    "computational methods":"6–8 weeks",
    "digital pedagogy":"4–6 weeks"
}

def recommend(skill_gap):
    return {
        skill: f"Suggested learning duration: {DURATION[skill]}"
        for skill in skill_gap if skill in DURATION
    }

