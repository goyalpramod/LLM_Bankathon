const dropArea = document.querySelector(".drag-image");
const dragText = dropArea.querySelector("h6");
const button = dropArea.querySelector("button");
const input = dropArea.querySelector("input");
let file;

button.onclick = () => {
  input.click();
};

input.addEventListener("change", function() {
  file = this.files[0];
  dropArea.classList.add("active");
  viewfile();
});

dropArea.addEventListener("dragover", (event) => {
  event.preventDefault();
  dropArea.classList.add("active");
  dragText.textContent = "Release to Upload File";
});

dropArea.addEventListener("dragleave", () => {
  dropArea.classList.remove("active");
  dragText.textContent = "Drag & Drop to Upload File";
});

dropArea.addEventListener("drop", (event) => {
  event.preventDefault();
  file = event.dataTransfer.files[0];
  viewfile();
});

function viewfile() {
  let fileType = file.type;
  let validExtensions = ["image/jpeg", "image/jpg", "image/png"];
  if (validExtensions.includes(fileType)) {
    let fileReader = new FileReader();
    fileReader.onload = () => {
      let fileURL = fileReader.result;
      let imgTag = `<img src="${fileURL}" alt="image">`;
      dropArea.innerHTML = imgTag;
    };
    fileReader.readAsDataURL(file);
  } else {
    alert("This is not an Image File!");
    dropArea.classList.remove("active");
    dragText.textContent = "Drag & Drop to Upload File";
  }
}

const sendMailButtons = document.querySelectorAll('.send-mail-btn');
sendMailButtons.forEach(sendMailBtn => {
  sendMailBtn.addEventListener('click', () => {
    window.open('mailto:praneetha2829@gmail.com?subject=&body=', '_blank');
  });
});

const questionButtons = document.querySelectorAll('.question-button');
questionButtons.forEach(questionButton => {
  questionButton.addEventListener('click', () => {
    const seeDocLink = questionButton.nextElementSibling.href;
    if (seeDocLink) {
      window.open(seeDocLink, '_blank');
    }
  });
});

// Get all status cells and icons
const statusCells = document.querySelectorAll('.status-cell');

// Loop through each status cell and add event listeners
statusCells.forEach(statusCell => {
  const statusText = statusCell.querySelector('.status-text');
  const statusIcons = statusCell.querySelector('.status-icons');
  const statusTick = statusIcons.querySelector('.status-icon.tick');
  const statusCross = statusIcons.querySelector('.status-icon.cross');

  statusTick.addEventListener('click', () => {
    statusText.innerHTML = 'Shortlisted';
    statusText.style.backgroundColor = 'var(--color-success)';
  });

  statusCross.addEventListener('click', () => {
    statusText.innerHTML = 'Rejected';
    statusText.style.backgroundColor = 'var(--color-danger)';
  });
});

