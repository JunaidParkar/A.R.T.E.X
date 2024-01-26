let notificationAudio = new Audio("../assets/system/sounds/notify.mp3");
notificationAudio.preload = "auto";

const notifyUser = (
  text,
  src = "",
  success = false,
  danger = false,
  error = false
) => {
  let mainDiv = document.createElement("div");
  mainDiv.classList.add("notification");
  let iconDiv = document.createElement("div");
  iconDiv.classList.add("icon");
  let img = document.createElement("img");
  img.src = success
    ? "../assets/system/icons/success.png"
    : danger
    ? "../assets/system/icons/danger.png"
    : error
    ? "../assets/system/icons/error.png"
    : src;
  iconDiv.appendChild(img);
  let textElement = document.createElement("p");
  textElement.textContent = text;
  mainDiv.appendChild(iconDiv);
  mainDiv.appendChild(textElement);
  mainDiv.style.top = "20px";
  document.body.appendChild(mainDiv);

  setTimeout(() => {
    mainDiv.style.top = "-100px";
    mainDiv.addEventListener("transitionend", () => {
      document.body.removeChild(mainDiv);
    });
  }, 5000);
};

const ConfirmFromUser = (heading, message) => {
  return new Promise((resolve, reject) => {
    let mainDiv = document.createElement("div");
    mainDiv.classList.add("mainAlert");
    let alertDiv = document.createElement("div");
    alertDiv.classList.add("alert");
    let headingDiv = document.createElement("div");
    headingDiv.classList.add("heading");
    let headingTxt = document.createElement("p");
    headingTxt.textContent = heading;
    headingDiv.appendChild(headingTxt);
    let messageDiv = document.createElement("div");
    messageDiv.classList.add("message");
    let messageText = document.createElement("p");
    messageText.textContent = message;
    messageDiv.appendChild(messageText);
    let buttonDiv = document.createElement("div");
    buttonDiv.classList.add("buttons");
    let cancelButton = document.createElement("button");
    cancelButton.textContent = "Cancel";
    cancelButton.onclick = () => {
      document.body.removeChild(mainDiv);
      reject();
    };
    let confirmButtom = document.createElement("button");
    confirmButtom.textContent = "Confirm";
    confirmButtom.onclick = () => {
      document.body.removeChild(mainDiv);
      resolve();
    };
    buttonDiv.appendChild(cancelButton);
    buttonDiv.appendChild(confirmButtom);
    alertDiv.appendChild(headingDiv);
    alertDiv.appendChild(messageDiv);
    alertDiv.appendChild(buttonDiv);
    mainDiv.appendChild(alertDiv);
    document.body.appendChild(mainDiv);
  });
};
