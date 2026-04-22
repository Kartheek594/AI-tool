console.log("JS Loaded");

const options = document.querySelectorAll(".option");
const questionElement = document.getElementById("question");

if (!questionElement) {
  console.error("Question element not found");
}

const question = questionElement ? questionElement.innerText : "";

console.log("Options found:", options.length);

options.forEach(option => {
  option.addEventListener("mouseenter", () => {
    console.log("Hover working on:", option.innerText);
  });
});
