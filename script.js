const textarea = document.getElementById("inputText");
const guidanceText = "Please describe your skills and experience clearly below:\n\n";

// Set initial guidance
window.onload = function () {
    textarea.value = guidanceText;
    textarea.style.color = "#888";  // light grey
};

// Prevent deleting guidance text
textarea.addEventListener("keydown", function (e) {
    if (textarea.selectionStart <= guidanceText.length) {
        if (e.key === "Backspace" || e.key === "Delete") {
            e.preventDefault();
        }
    }
});

// When user types after guidance, change text color to black
textarea.addEventListener("input", function () {
    if (textarea.value.length > guidanceText.length) {
        textarea.style.color = "#000";
    }
});

document.getElementById("analyzeBtn").addEventListener("click", analyzeSkills);

function analyzeSkills() {

    const resultBox = document.getElementById("result");

    const userText = textarea.value.replace(guidanceText, "").trim();

    if (userText === "") {
        resultBox.textContent = "Please enter your skills and experience.";
        return;
    }

    resultBox.textContent = "Analyzing skill gap...";

    fetch("https://predictive-skill-gap-backend.onrender.com/analyze", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ text: userText })
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




