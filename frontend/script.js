function analyze() {
    const text = document.getElementById("inputText").value;

    fetch("http://127.0.0.1:5000/analyze", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ text: text })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("output").textContent =
            JSON.stringify(data, null, 2);
    })
    .catch(error => {
        document.getElementById("output").textContent =
            "Error connecting to backend";
    });
}
