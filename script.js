console.log("JS Loaded");
const options = document.querySelectorAll(".option");
const question = document.getElementById("question").innerText;

options.forEach(option => {
  option.addEventListener("mouseenter", async () => {
    console.log("Hovering:", option.innerText);

    try {
      const response = await fetch("http://127.0.0.1:5000/check", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          question: question,
          option: option.innerText
        })
      });

      const result = await response.json();

      if (result.status === "correct") {
        option.style.backgroundColor = "green";
      } else {
        option.style.backgroundColor = "red";
      }

    } catch (error) {
      console.error("Error:", error);
    }
  });
});
