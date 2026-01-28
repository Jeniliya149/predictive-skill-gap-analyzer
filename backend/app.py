from flask import Flask, request, jsonify
from flask_cors import CORS

from skill_extractor import extract_skills, detect_branch
from trend_analyzer import predict_future_skills
from recommender import recommend

app = Flask(__name__)
CORS(app)

@app.route("/analyze", methods=["POST"])
def analyze():
    text = request.json.get("text","")

    branch = detect_branch(text)
    user_skills = extract_skills(text)
    future_skills = predict_future_skills(branch)

    skill_gap = list(set(future_skills) - set(user_skills))
    recommendations = recommend(skill_gap)

    return jsonify({
        "branch_detected": branch,
        "user_skills": user_skills,
        "future_skills": future_skills,
        "skill_gap": skill_gap,
        "recommendations": recommendations
    })

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
