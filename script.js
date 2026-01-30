document.getElementById("analyzeBtn").addEventListener("click", analyzeSkills);

function analyzeSkills() {
    const inputText = document.getElementById("inputText").value.trim();
    const resultBox = document.getElementById("result");

    if (inputText === "") {
        resultBox.textContent = "Please enter your skills or background.";
        return;
    }

    resultBox.textContent = "Analyzing skill gap...";

    fetch("https://predictive-skill-gap-backend.onrender.com/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ text: inputText })
    })
    .then(response => response.json())
    .then(data => {
        let output = "";

        output += "Detected Role: " + data.job_role_detected + "\n";
        output += "Experience Level: " + data.experience_level + "\n\n";

        output += "Current Skills:\n";
        output += (data.current_skills.length > 0 ? "- " + data.current_skills.join("\n- ") : "None") + "\n\n";

        output += "Future Required Skills:\n";
        output += "- " + data.future_skills.join("\n- ") + "\n\n";

        output += "Skill Gap:\n";
        output += "- " + data.skill_gap.join("\n- ") + "\n\n";

        output += "Recommended Learning Plan:\n";
        for (let skill in data.recommended_courses) {
            output += "- " + skill + " : " + data.recommended_courses[skill] + "\n";
        }

        resultBox.textContent = output;
    })
    .catch(() => {
        resultBox.textContent = "Error connecting to backend. Make sure backend is running.";
    });
}



