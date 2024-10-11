document.onload = () => {
  document.getElementById("cmdInp").focus();
};

document.getElementById("cmdContainer").addEventListener("click", () => {
  document.getElementById("cmdInp").focus();
});

document.getElementById("cmdInp").addEventListener("input", () => {
  let contentWidth = document.getElementById("cmdInp").scrollWidth;
  let contentheight = document.getElementById("cmdInp").scrollHeight;
  document.getElementById("cmdInp").style.width = contentWidth + "px";
  document.getElementById("cmdInp").style.height = contentheight + "px";
});
