function showScoreAndResult() {
  // Show the score card, result box, and question icon container after clicking the Save button
  const jobTitle = document.getElementById("job-title").value;
  const jobDescription = document.getElementById("job-description").value;

  document.getElementById("score-card").style.display = "inline-block";
  document.getElementById("result-box").style.display = "inline-block";
  document.getElementById("question-container").style.display = "block";

  fetch(PROCESS_FORM_URL, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      // Add CSRF Token for Django
      "X-CSRFToken": getCookie("csrftoken"),
    },
    body: JSON.stringify({
      "job-title": jobTitle,
      "job-description": jobDescription,
    }),
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      return response.json();
    })
    .then((data) => {
      if (data.score && data.updatedJD && data.changes) {
        // Update the frontend elements with the received data
        document.getElementById("score-card").querySelector("h2").innerHTML =
          "Score: " + data.score;
        document.getElementById("result-box").querySelector("p").innerHTML =
          data.updatedJD;
        document.getElementById("popup").querySelector("p").innerHTML =
          data.changes;

        // Show the score card, result box, and question icon container
        document.getElementById("score-card").style.display = "inline-block";
        document.getElementById("result-box").style.display = "inline-block";
        document.getElementById("popup").style.display = "block";
      } else {
        // Handle the case where expected data is not in the response
        console.error("Unexpected response data:", data);
      }
    })
    .catch((error) => {
      console.error("Error:", error);
    });
}

function getCookie(name) {
  let value = "; " + document.cookie;
  let parts = value.split("; " + name + "=");
  if (parts.length == 2) return parts.pop().split(";").shift();
}

function showPopup() {
  // Show the popup
  document.getElementById("popup").style.display = "block";
}

function closePopup() {
  // Close the popup
  document.getElementById("popup").style.display = "none";
}
