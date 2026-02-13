document.getElementById("analyzeBtn").addEventListener("click", analyzeSkills);

// Move cursor automatically below guidance text
window.onload = function () {
    const textarea = document.getElementById("inputText");
    textarea.selectionStart = textarea.value.length;
    textarea.selectionEnd = textarea.value.length;
};

function analyzeSkills() {

    const textarea = document.getElementById("inputText");
    const inputText = textarea.value.trim();
    const resultBox = document.getElementById("result");

    // Remove guidance text before sending to backend
    const cleanedText = inputText.replace(
        "Please describe your skills and experience clearly below:",
        ""
    ).trim();

    if (cleanedText === "") {
        resultBox.textContent = "Please enter your skills and experience.";
        return;
    }

    resultBox.textContent = "Analyzing skill gap...";

    fetch("https://predictive-skill-gap-backend.onrender.com/analyze", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ text: cleanedText })
    })
    .then(response => response.json())
    .then(data => {

        let output = "";

        output += "Detected Role: " + data.job_role_detected + "\n";
        output += "Experience Level: " + data.experience_level + "\n\n";

        output += "Current Skills:\n";
        output += (data.current_skills.length > 0
            ? "- " + data.current_skills.join("\n- ")
            : "None") + "\n\n";

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
        resultBox.textContent = "Error connecting to backend.";
    });
}




