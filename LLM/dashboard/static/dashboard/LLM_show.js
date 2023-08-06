function showResultBox() {
  document.getElementById("result-box").style.display = "block";
}

const jobForm = document.getElementById("job-form");
jobForm.addEventListener("submit", function (event) {
  event.preventDefault();
});
