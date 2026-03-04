const textarea = document.getElementById("inputText");
const fixedText = "Describe your skills and experience here:\n\n";

window.onload = function () {
    textarea.value = fixedText;
    textarea.style.color = "#888"; // light grey
    textarea.setSelectionRange(fixedText.length, fixedText.length);
};

textarea.addEventListener("keydown", function (e) {
    if (textarea.selectionStart < fixedText.length) {
        e.preventDefault();
        textarea.setSelectionRange(fixedText.length, fixedText.length);
    }
});

textarea.addEventListener("click", function () {
    if (textarea.selectionStart < fixedText.length) {
        textarea.setSelectionRange(fixedText.length, fixedText.length);
    }
});

document.getElementById("analyzeBtn").addEventListener("click", analyzeSkills);

function analyzeSkills() {

    const resultBox = document.getElementById("result");

    const userText = textarea.value.replace(fixedText, "").trim();

    if (userText === "") {
        resultBox.textContent = "Please enter your skills and experience.";
        return;
    }

    resultBox.textContent = "Analyzing skill gap...";
    fetch("https://predictive-skill-gap-analyzer.onrender.com/analyze", {


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




