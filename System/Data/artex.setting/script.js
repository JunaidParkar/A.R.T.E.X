const switches = document.querySelectorAll(".button");

switches.forEach((s) => {
  s.addEventListener("click", () => {
    s.classList.toggle("active");
  });
});

const openMoreSetting = (e) => {
  const settingId = e.dataset.moresetting;
  const allSettings = document.querySelectorAll(".moresetting div");

  allSettings.forEach((setting) => {
    if (setting.id === settingId) {
      setting.style.display = "block";
    } else {
      setting.style.display = "none";
    }
  });
};

// function setBackground(image) {
//   const imageURL = image.src;
//   localStorage.setItem('backgroundImage', imageURL);
// }

const storedBackground = localStorage.getItem("backgroundImage");
const imageList = document
  .getElementById("imageList")
  .getElementsByTagName("img");

for (let i = 0; i < imageList.length; i++) {
  if (imageList[i].src === storedBackground) {
    imageList[i].classList.add("selected");
  }
}

function setBackground(image) {
  const imageURL = image.src;
  localStorage.setItem("backgroundImage", imageURL);

  const imageList = document
    .getElementById("imageList")
    .getElementsByTagName("img");
  for (let i = 0; i < imageList.length; i++) {
    imageList[i].classList.remove("selected");
  }
  image.classList.add("selected");
}
