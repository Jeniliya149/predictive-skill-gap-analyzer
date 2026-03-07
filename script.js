document.getElementById("analyzeBtn").addEventListener("click", analyzeSkills);

function analyzeSkills(){

const text=document.getElementById("inputText").value.trim();

if(text===""){
alert("Please enter your skills");
return;
}

fetch("https://predictive-skill-gap-analyzer-2.onrender.com/analyze",{

method:"POST",

headers:{
"Content-Type":"application/json"
},

body:JSON.stringify({text:text})

})

.then(res=>res.json())

.then(data=>{

document.getElementById("role").innerHTML=
`<span class="badge">${data.job_role_detected}</span>`;

document.getElementById("experience").innerHTML=
`<span class="badge">${data.experience_level}</span>`;


document.getElementById("currentSkills").innerHTML=
data.current_skills.map(s=>`<span class="chip">${s}</span>`).join("");


document.getElementById("futureSkills").innerHTML=
data.future_skills.map(s=>`<span class="chip future">${s}</span>`).join("");


document.getElementById("skillGap").innerHTML=
data.skill_gap.map(s=>`<span class="chip gap">${s}</span>`).join("");


let planHTML="<ul>";

for(let skill in data.recommended_courses){

planHTML+=`<li><b>${skill}</b> → ${data.recommended_courses[skill]}</li>`;

}

planHTML+="</ul>";

document.getElementById("learningPlan").innerHTML=planHTML;

})

.catch(()=>{

alert("Error connecting to backend")

})

}


