import re

# -------------------------
# Normalize text
# -------------------------
def normalize(text):
    return text.lower()

# -------------------------
# Detect Experience Level
# -------------------------
def detect_experience(text):
    text = normalize(text)

    if "senior" in text:
        return "senior"
    if "mid" in text or "experienced" in text:
        return "mid"
    if "junior" in text:
        return "junior"
    if "fresher" in text or "student" in text:
        return "fresher"

    return "unknown"

# -------------------------
# Detect Job Role (STRICT & DATASET-BASED)
# -------------------------
def detect_branch(text):
    text = normalize(text)

    role_keywords = {
        "Software Engineer": [
            "software", "programming", "developer", "coding",
            "python", "java", "sql", "oop", "git",
            "cloud", "devops", "docker", "kubernetes",
            "ci cd", "microservices", "rest api", "ai tools"
        ],

        "Civil Engineer": [
            "civil", "construction", "surveying", "autocad",
            "building materials", "structural analysis",
            "staad", "bim", "bim modeling",
            "construction planning", "project management",
            "smart construction", "sustainable construction",
            "digital twins"
        ],

        "Mechanical Engineer": [
            "mechanical", "engineering drawing", "thermodynamics",
            "solidworks", "manufacturing processes",
            "cnc machining", "robotics",
            "automation systems", "mechatronics",
            "smart manufacturing", "industry 4.0",
            "digital manufacturing"
        ],

        "ECE Engineer": [
            "ece", "electronics", "basic electronics",
            "analog circuits", "digital electronics",
            "signals and systems", "communication systems",
            "embedded c", "iot systems",
            "vlsi design", "edge computing",
            "ai hardware integration",
            "intelligent embedded systems"
        ],

        "EEE Engineer": [
            "eee", "electrical", "electrical machines",
            "power systems", "control systems",
            "power electronics", "renewable energy",
            "smart grids", "energy management systems",
            "electric vehicles", "battery management systems",
            "sustainable energy systems",
            "ai based power optimization"
        ],

        "Aerospace Engineer": [
            "aerospace", "engineering mechanics",
            "fluid mechanics", "aerodynamics",
            "aircraft structures", "propulsion systems",
            "flight dynamics", "composite materials",
            "avionics", "uav systems",
            "space systems engineering",
            "autonomous flight systems"
        ],

        "Law Professional": [
            "law", "legal", "legal research",
            "legal writing", "constitutional law",
            "criminal law", "corporate law",
            "intellectual property law",
            "cyber law", "legal analytics",
            "tech law", "ai governance",
            "digital law compliance"
        ],

        "Doctor": [
            "doctor", "medical", "human anatomy",
            "physiology", "pathology", "pharmacology",
            "clinical diagnosis", "medical imaging",
            "telemedicine", "digital health records",
            "ai assisted diagnosis",
            "personalized medicine",
            "predictive healthcare analytics"
        ],

        "Business Management": [
            "business", "management", "business fundamentals",
            "accounting", "marketing",
            "operations management",
            "financial management",
            "business analytics",
            "data driven decision making",
            "digital transformation",
            "strategic management",
            "ai in business",
            "intelligent enterprise systems"
        ]
    }

    scores = {}

    for role, keywords in role_keywords.items():
        scores[role] = 0
        for keyword in keywords:
            if keyword in text:
                scores[role] += 1

    # Select role with highest keyword match
    best_role = max(scores, key=scores.get)

    # If no keywords matched at all → Unknown (HONEST)
    if scores[best_role] == 0:
        return "Unknown"

    return best_role

# -------------------------
# Extract Skills (STRICT DATASET SKILLS)
# -------------------------
def extract_skills(text):
    text = text.lower()

    known_skills = [
        # Software
        "c", "java", "python", "sql", "oop", "git",
        "cloud", "cloud basics", "rest api",
        "microservices", "devops", "docker",
        "kubernetes", "ci cd", "cloud automation",
        "cloud devops", "ai tools",

        # Civil
        "surveying", "autocad", "building materials",
        "structural analysis", "staad",
        "bim", "bim modeling", "construction planning",
        "project management", "smart construction",
        "sustainable construction", "digital twins",

        # Mechanical
        "engineering drawing", "thermodynamics",
        "solidworks", "manufacturing processes",
        "cnc machining", "robotics",
        "automation systems", "mechatronics",
        "smart manufacturing", "industry 4.0",
        "digital manufacturing",

        # ECE
        "basic electronics", "analog circuits",
        "digital electronics", "signals and systems",
        "communication systems", "embedded c",
        "iot systems", "vlsi design",
        "edge computing", "ai hardware integration",
        "intelligent embedded systems",

        # EEE
        "electrical machines", "power systems",
        "control systems", "power electronics",
        "renewable energy", "smart grids",
        "energy management systems",
        "electric vehicles",
        "battery management systems",
        "sustainable energy systems",
        "ai based power optimization",

        # Aerospace
        "engineering mechanics", "fluid mechanics",
        "aerodynamics", "aircraft structures",
        "propulsion systems", "flight dynamics",
        "composite materials", "avionics basics",
        "uav systems", "space systems engineering",
        "autonomous flight systems",

        # Law
        "legal research", "legal writing",
        "constitutional law", "criminal law",
        "corporate law", "intellectual property law",
        "cyber law", "legal analytics",
        "tech law", "ai governance",
        "digital law compliance",

        # Doctor
        "human anatomy", "physiology",
        "pathology", "pharmacology",
        "clinical diagnosis", "medical imaging basics",
        "telemedicine", "digital health records",
        "ai assisted diagnosis",
        "personalized medicine",
        "predictive healthcare analytics",

        # Business
        "business fundamentals", "accounting basics",
        "marketing principles", "operations management",
        "financial management", "business analytics",
        "data driven decision making",
        "digital transformation",
        "strategic management",
        "ai in business",
        "intelligent enterprise systems"
    ]

    extracted = []

    for skill in known_skills:
        # match full word or full phrase only
        pattern = r"\b" + re.escape(skill) + r"\b"
        if re.search(pattern, text):
            extracted.append(skill)

    return sorted(list(set(extracted)))
