const dropArea = document.querySelector(".drag-image"),
dragText = dropArea.querySelector("h6"),
button = dropArea.querySelector("button"),
input = dropArea.querySelector("input");
let file; 

button.onclick = ()=>{
  input.click(); 
}

input.addEventListener("change", function(){
 
  file = this.files[0];
  dropArea.classList.add("active");
  viewfile();
});

dropArea.addEventListener("dragover", (event)=>{
  event.preventDefault();
  dropArea.classList.add("active");
  dragText.textContent = "Release to Upload File";
});


dropArea.addEventListener("dragleave", ()=>{
  dropArea.classList.remove("active");
  dragText.textContent = "Drag & Drop to Upload File";
}); 

dropArea.addEventListener("drop", (event)=>{
  event.preventDefault(); 
   
  file = event.dataTransfer.files[0];
  viewfile(); 
});

function viewfile(){
  let fileType = file.type; 
  let validExtensions = ["image/jpeg", "image/jpg", "image/png"];
  if(validExtensions.includes(fileType)){ 
    let fileReader = new FileReader(); 
    fileReader.onload = ()=>{
      let fileURL = fileReader.result; 
       let imgTag = `<img src="${fileURL}" alt="image">`;
      dropArea.innerHTML = imgTag; 
    }
    fileReader.readAsDataURL(file);
  }else{
    alert("This is not an Image File!");
    dropArea.classList.remove("active");
    dragText.textContent = "Drag & Drop to Upload File";
  }
}


    const statusCell = document.querySelector('.status-cell');
    const statusText = statusCell.querySelector('.status-text');
    const statusTick = statusCell.querySelector('.status-icon.tick');
    const statusCross = statusCell.querySelector('.status-icon.cross');
    const statusPen = statusCell.querySelector('.status-icon.pen');

    statusTick.addEventListener('click', () => {
        statusText.innerHTML = 'Shortlisted';
        statusText.style.backgroundColor = 'var(--color-success)';
    });

    statusCross.addEventListener('click', () => {
        statusText.innerHTML = 'Rejected';
        statusText.style.backgroundColor = 'var(--color-danger)';
    });

    statusPen.addEventListener('click', () => {
        const currentStatus = statusText.innerHTML;
        if (currentStatus === 'Shortlisted') {
            statusText.innerHTML = 'Rejected';
            statusText.style.backgroundColor = 'var(--color-danger)';
        } else if (currentStatus === 'Rejected') {
            statusText.innerHTML = 'Shortlisted';
            statusText.style.backgroundColor = 'var(--color-success)';
        }
    });

    const sendMailBtn = document.querySelector('.action-icon.send-mail');
    sendMailBtn.addEventListener('click', () => {
        window.open('mailto:praneetha2829@gmail.com?subject=&body=', '_blank');
    });

