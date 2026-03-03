import re


# -------------------------
# Normalize text
# -------------------------
def normalize(text):
    return text.lower().strip()


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
# Detect Job Role (Clean & Controlled)
# -------------------------
def detect_branch(text):
    text = normalize(text)

    role_keywords = {
        "Software Engineer": ["software", "developer", "programming"],
        "Aerospace Engineer": ["aerospace"],
        "ECE Engineer": ["ece", "electronics"],
        "EEE Engineer": ["eee", "electrical"],
        "Mechanical Engineer": ["mechanical"],
        "Civil Engineer": ["civil"],
        "Law Professional": ["law", "legal"],
        "Healthcare": ["healthcare", "doctor", "medical", "mbbs", "bds", "homeopathy"],
        "Business Management": ["business", "management"]
    }

    scores = {}

    for role, keywords in role_keywords.items():
        scores[role] = sum(1 for keyword in keywords if keyword in text)

    best_role = max(scores, key=scores.get)

    if scores[best_role] == 0:
        return "Unknown"

    return best_role


# -------------------------
# Extract Skills (STRICT DATASET MATCH)
# -------------------------
def extract_skills(text):
    text = normalize(text)

    # Remove special characters but keep spaces
    text = re.sub(r"[^a-z0-9\s]", " ", text)

    # Add padding spaces for strict matching
    text = f" {text} "

    known_skills = [

        # ===== Software Engineer (exactly from dataset) =====
        "c", "java", "oop", "python", "sql", "git",
        "cloud basics", "cloud", "rest api",
        "microservices", "devops", "docker",
        "kubernetes", "ci cd", "cloud automation",
        "ai tools", "cloud devops",
        "html", "css", "javascript",
        "dsa", "web development",
        "react", "nodejs",
        "backend development",
        "frontend development",
        "full stack development",
        "database design",
        "system design",

        # ===== Aerospace Engineer =====
        "engineering mechanics", "fluid mechanics",
        "aerodynamics", "aircraft structures",
        "propulsion systems", "flight dynamics",
        "composite materials", "avionics basics",
        "uav systems", "space systems engineering",
        "autonomous flight systems",

        # ===== ECE Engineer =====
        "basic electronics", "analog circuits",
        "digital electronics", "signals and systems",
        "communication systems", "embedded c",
        "iot systems", "vlsi design",
        "edge computing", "ai hardware integration",
        "intelligent embedded systems",

        # ===== EEE Engineer =====
        "electrical machines", "power systems",
        "control systems", "power electronics",
        "renewable energy basics", "smart grids",
        "energy management systems",
        "electric vehicles",
        "battery management systems",
        "sustainable energy systems",
        "ai based power optimization",

        # ===== Mechanical Engineer =====
        "engineering drawing", "thermodynamics",
        "solidworks", "manufacturing processes",
        "cnc machining", "robotics",
        "automation systems", "mechatronics",
        "smart manufacturing", "industry 4.0",
        "digital manufacturing",

        # ===== Civil Engineer =====
        "surveying", "autocad",
        "building materials", "structural analysis",
        "staad", "bim modeling",
        "construction planning",
        "project management",
        "smart construction",
        "sustainable construction",
        "digital twins",

        # ===== Law Professional =====
        "legal research", "legal writing",
        "constitutional law", "criminal law",
        "corporate law",
        "intellectual property law",
        "cyber law", "legal analytics",
        "tech law", "ai governance",
        "digital law compliance",

        # ===== Healthcare =====
        "mbbs", "human anatomy",
        "physiology", "basic healthcare",
        "pathology", "clinical observation",
        "pharmacology", "bds",
        "clinical diagnosis", "homeopathy",
        "medical imaging basics", "health systems",
        "telemedicine", "public health management",
        "digital health records", "health informatics",
        "ai assisted diagnosis", "clinical research",
        "personalized medicine", "medical data analysis",
        "predictive healthcare analytics",
        "healthcare technology management",

        # ===== Business Management =====
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
        pattern = f" {skill} "
        if pattern in text:
            extracted.append(skill)

    return sorted(extracted)
