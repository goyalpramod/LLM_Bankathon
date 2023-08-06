function showScoreAndResult() {
  // Show the score card, result box, and question icon container after clicking the Save button
  document.getElementById('score-card').style.display = 'inline-block';
  document.getElementById('result-box').style.display = 'inline-block';
  document.getElementById('question-container').style.display = 'block';
}

function showPopup() {
  // Show the popup
  document.getElementById('popup').style.display = 'block';
}

function closePopup() {
  // Close the popup
  document.getElementById('popup').style.display = 'none';
}