function openDrop(){
  document.getElementById('modal').style.display="block";
}
function closeDrop(){
  document.getElementById('modal').style.display="none";
}

window.onclick = function(event) {
  if (event.target==modal) {

   document.getElementById('modal').style.display="none";
  }
}

// Created by Mudit Singhal, Pravin Jangir, Tarun Kumar
