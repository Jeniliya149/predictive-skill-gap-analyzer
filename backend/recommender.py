"""
Recommender Module
------------------
This module recommends learning duration for missing skills.
It uses ONLY skills present in the 2015–2025 dataset.
No prediction logic is done here.
"""

# Learning duration mapping (realistic & dataset-based)
COURSE_DURATION = {

    # ===== Software Engineer (CSE) =====
    "c": "4 weeks",
    "java": "6 weeks",
    "oop": "3 weeks",
    "python": "6 weeks",
    "sql": "4 weeks",
    "git": "2 weeks",
    "cloud basics": "3 weeks",
    "cloud": "4–6 weeks",
    "rest api": "4 weeks",
    "microservices": "4–6 weeks",
    "devops": "8–12 weeks",
    "docker": "4 weeks",
    "kubernetes": "6 weeks",
    "ci cd": "3 weeks",
    "cloud automation": "4 weeks",
    "ai tools": "3 weeks",
    "cloud devops": "6 weeks",

    # ===== Aerospace Engineer =====
    "engineering mechanics": "6 weeks",
    "fluid mechanics": "6 weeks",
    "aerodynamics": "8 weeks",
    "aircraft structures": "6 weeks",
    "propulsion systems": "6 weeks",
    "flight dynamics": "6 weeks",
    "composite materials": "4 weeks",
    "avionics basics": "4 weeks",
    "uav systems": "6 weeks",
    "space systems engineering": "6 weeks",
    "autonomous flight systems": "8 weeks",

    # ===== ECE Engineer =====
    "basic electronics": "4 weeks",
    "analog circuits": "6 weeks",
    "digital electronics": "6 weeks",
    "signals and systems": "6 weeks",
    "communication systems": "6 weeks",
    "embedded c": "6 weeks",
    "iot systems": "6 weeks",
    "vlsi design": "8 weeks",
    "edge computing": "4 weeks",
    "ai hardware integration": "6 weeks",
    "intelligent embedded systems": "6 weeks",

    # ===== EEE Engineer =====
    "electrical machines": "6 weeks",
    "power systems": "6 weeks",
    "control systems": "6 weeks",
    "power electronics": "6 weeks",
    "renewable energy basics": "4 weeks",
    "smart grids": "6 weeks",
    "energy management systems": "6 weeks",
    "electric vehicles": "6 weeks",
    "battery management systems": "6 weeks",
    "sustainable energy systems": "6 weeks",
    "ai based power optimization": "4 weeks",

    # ===== Mechanical Engineer =====
    "engineering drawing": "4 weeks",
    "thermodynamics": "6 weeks",
    "solidworks": "6 weeks",
    "manufacturing processes": "6 weeks",
    "cnc machining": "4 weeks",
    "robotics": "8 weeks",
    "automation systems": "6 weeks",
    "mechatronics": "6 weeks",
    "smart manufacturing": "6 weeks",
    "industry 4.0": "6 weeks",
    "digital manufacturing": "6 weeks",

    # ===== Civil Engineer =====
    "surveying": "4 weeks",
    "autocad": "6 weeks",
    "building materials": "4 weeks",
    "structural analysis": "6 weeks",
    "staad": "6 weeks",
    "bim modeling": "6 weeks",
    "construction planning": "4 weeks",
    "project management": "6 weeks",
    "smart construction": "6 weeks",
    "sustainable construction": "6 weeks",
    "digital twins": "6 weeks",

    # ===== Law Professional =====
    "legal research": "4 weeks",
    "legal writing": "4 weeks",
    "constitutional law": "6 weeks",
    "criminal law": "6 weeks",
    "corporate law": "6 weeks",
    "intellectual property law": "6 weeks",
    "cyber law": "6 weeks",
    "legal analytics": "4 weeks",
    "tech law": "6 weeks",
    "ai governance": "4 weeks",
    "digital law compliance": "4 weeks",

    # ===== Doctor =====
    "human anatomy": "6 weeks",
    "physiology": "6 weeks",
    "pathology": "6 weeks",
    "pharmacology": "6 weeks",
    "clinical diagnosis": "6 weeks",
    "medical imaging basics": "4 weeks",
    "telemedicine": "4 weeks",
    "digital health records": "4 weeks",
    "ai assisted diagnosis": "4 weeks",
    "personalized medicine": "6 weeks",
    "predictive healthcare analytics": "6 weeks",

    # ===== Business Management =====
    "business fundamentals": "4 weeks",
    "accounting basics": "4 weeks",
    "marketing principles": "4 weeks",
    "operations management": "6 weeks",
    "financial management": "6 weeks",
    "business analytics": "6 weeks",
    "data driven decision making": "4 weeks",
    "digital transformation": "6 weeks",
    "strategic management": "6 weeks",
    "ai in business": "4 weeks",
    "intelligent enterprise systems": "6 weeks"
}


def recommend(skill_gap):
    """
    Takes a list of missing skills and returns
    recommended learning duration for each skill.
    """

    recommendations = {}

    for skill in skill_gap:
        if skill in COURSE_DURATION:
            recommendations[skill] = COURSE_DURATION[skill]
        else:
            # Safe default (won't usually occur)
            recommendations[skill] = "4–6 weeks"

    return recommendations


