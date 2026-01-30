from flask import Flask, request, jsonify
from flask_cors import CORS

from skill_extractor import detect_branch, detect_experience, extract_skills
from trend_analyzer import predict_future_skills
from recommender import recommend

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def home():
    return "Predictive Skill Gap Analyzer API is running"

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    text = data.get("text", "")

    # Detect information
    job_role = detect_branch(text)
    experience_level = detect_experience(text)
    current_skills = extract_skills(text)

    # Predict future skills (ROLE-BASED)
    future_skills = predict_future_skills(job_role)

    # Skill gap
    skill_gap = sorted(list(set(future_skills) - set(current_skills)))

    # Recommendations (can depend on skill gap)
    recommendations = recommend(skill_gap)

    return jsonify({
        "job_role_detected": job_role,
        "experience_level": experience_level,
        "current_skills": current_skills,
        "future_skills": future_skills,
        "skill_gap": skill_gap,
        "recommended_courses": recommendations
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)



