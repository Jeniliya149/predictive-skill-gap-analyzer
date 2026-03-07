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

document.getElementById("role").textContent =
data.job_role_detected;

document.getElementById("experience").textContent =
data.experience_level;

document.getElementById("currentSkills").textContent =
data.current_skills.join(", ");

document.getElementById("futureSkills").textContent =
data.future_skills.join(", ");

document.getElementById("skillGap").textContent =
data.skill_gap.join(", ");


let plan="";

for(let skill in data.recommended_courses){

plan += skill + " : " + data.recommended_courses[skill] + " | ";

}

document.getElementById("learningPlan").textContent = plan;

})

.catch(()=>{

alert("Error connecting to backend.");

});

}



