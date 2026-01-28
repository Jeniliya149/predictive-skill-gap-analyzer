function analyze() {
  const text = document.getElementById("inputText").value;

  fetch("https://predictive-skill-gap-analyzer-1.onrender.com/analyze", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      text: text
    })
  })
  .then(response => response.json())
  .then(data => {
    document.getElementById("result").textContent =
      JSON.stringify(data, null, 2);
  })
  .catch(error => {
    document.getElementById("result").textContent =
      "Error connecting to backend";
    console.error(error);
  });
}

