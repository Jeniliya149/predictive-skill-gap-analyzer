const textarea = document.getElementById("inputText");

document.getElementById("analyzeBtn").addEventListener("click", analyzeSkills);


function analyzeSkills(){

const userText = textarea.value.trim();

if(userText === ""){
alert("Please describe your skills and experience.");
return;
}

fetch("https://predictive-skill-gap-analyzer-2.onrender.com/analyze",{

method:"POST",

headers:{
"Content-Type":"application/json"
},

body:JSON.stringify({text:userText})

})

.then(response=>{
if(!response.ok){
throw new Error("Server error");
}
return response.json();
})

.then(data=>{

document.getElementById("role").innerHTML =
`<span class="badge">${data.job_role_detected}</span>`;

document.getElementById("experience").innerHTML =
`<span class="badge">${data.experience_level}</span>`;


/* CURRENT SKILLS */

document.getElementById("currentSkills").innerHTML =
data.current_skills.map(skill =>
`<span class="skill-tag">${skill}</span>`
).join("");


/* FUTURE SKILLS */

document.getElementById("futureSkills").innerHTML =
data.future_skills.map(skill =>
`<span class="skill-tag future">${skill}</span>`
).join("");


/* SKILL GAP */

document.getElementById("skillGap").innerHTML =
data.skill_gap.map(skill =>
`<span class="skill-tag gap">${skill}</span>`
).join("");


/* LEARNING PLAN */

let planHTML = "<ul class='plan-list'>";

for(let skill in data.recommended_courses){

planHTML += `<li><b>${skill}</b> → ${data.recommended_courses[skill]}</li>`;

}

planHTML += "</ul>";

document.getElementById("learningPlan").innerHTML = planHTML;

})

.catch(()=>{

alert("Error connecting to backend.");

});

}



