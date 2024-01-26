// toggle to full screen

const toggleFullScreen = () => {
    var elem = document.documentElement;
    if (!document.fullscreenElement &&
        !document.mozFullScreenElement &&
        !document.webkitFullscreenElement &&
        !document.msFullscreenElement
    ) {
        if (elem.requestFullscreen) {
            elem.requestFullscreen();
        } else if (elem.msRequestFullscreen) {
            elem.msRequestFullscreen();
        } else if (elem.mozRequestFullScreen) {
            elem.mozRequestFullScreen();
        } else if (elem.webkitRequestFullscreen) {
            elem.webkitRequestFullscreen();
        }
    } else {
        if (document.exitFullscreen) {
            document.exitFullscreen();
        } else if (document.msExitFullscreen) {
            document.msExitFullscreen();
        } else if (document.mozCancelFullScreen) {
            document.mozCancelFullScreen();
        } else if (document.webkitExitFullscreen) {
            document.webkitExitFullscreen();
        }
    }
};

// full screen event listener

document.addEventListener("fullscreenchange", async() => {
    if (!document.fullscreenElement) {
        await ConfirmFromUser("A.R.T.E.X", "Experience more in full screen")
            .then(() => {
                toggleFullScreen();
            })
            .catch(() => {});
    }
});

document.addEventListener("DOMContentLoaded", async() => {
    await ConfirmFromUser("A.R.T.E.X", "Experience more in full screen")
        .then(() => {
            toggleFullScreen();
        })
        .catch(() => {});
});

// defined shortcut keys

document.addEventListener("keydown", async(event) => {
    if (event.ctrlKey && event.code === "NumpadDecimal") {
        await toggleSearchMenu();
    }
    if (event.code === "F11") {
        event.preventDefault();
    }
});

// Custom left click

const leftClick = async() => {
    document.getElementById("contextMenu").style.display = "none";
};

// custom right click

const rightClick = (e, isIframe = false) => {
    e.preventDefault();
    let menu = document.getElementById("contextMenu");
    if (menu.style.display == "block") {
        leftClick();
    }
    let clickX = isIframe ? e.clientX + 60 : e.clientX;
    let clickY = e.clientY;
    let gap = 5;
    let windowWidth = window.innerWidth;
    let windowHeight = window.innerHeight;
    menu.style.opacity = 0;
    menu.style.display = "block";
    menu.style.left = `${clickX + gap}px`;
    menu.style.top = `${clickY + gap}px`;
    let rect = menu.getBoundingClientRect();
    if (rect.right > windowWidth) {
        menu.style.left = `${clickX - (rect.width + gap)}px`;
    }

    if (rect.bottom > windowHeight) {
        menu.style.top = `${clickY - (rect.height + gap)}px`;
    }
    menu.style.opacity = 1;
};

document.getElementById("sidebar").onclick = leftClick;
document.getElementById("sidebar").oncontextmenu = leftClick;
document.getElementById("apps").onclick = leftClick;
document.getElementById("apps").oncontextmenu = rightClick;
document.getElementById("search-menu").onclick = leftClick;
document.getElementById("search-menu").oncontextmenu = rightClick;

// attaching custom context menu to iframes

const attachEventHandlers = (iframe) => {
    iframe.contentWindow.addEventListener("click", () => {
        leftClick();
    });
    iframe.contentWindow.addEventListener("contextmenu", (e) => {
        rightClick(e, true);
    });
    iframe.contentWindow.addEventListener("keydown", function(event) {
        if (event.ctrlKey && (event.key === "r" || event.code === "KeyR")) {
            event.preventDefault();
        }
    });
};

// get brightness from bg image

const getMaximumColorFromBackgroundAndSetText = (element, textElement) => {
    element = document.querySelector(element);
    textElement = document.getElementById(textElement);
    const backgroundImage = getComputedStyle(element).backgroundImage;
    const imageUrl = backgroundImage.replace(/url\(['"]?(.*?)['"]?\)/, "$1");
    const img = new Image();
    img.src = imageUrl;
    img.onload = function() {
        const canvas = document.createElement("canvas");
        canvas.width = img.width;
        canvas.height = img.height;
        const ctx = canvas.getContext("2d");
        ctx.drawImage(img, 0, 0);
        const imageData = ctx.getImageData(0, 0, canvas.width, canvas.height);
        let maxBrightness = 0;
        let maxBrightnessPixel = null;
        for (let i = 0; i < imageData.data.length; i += 4) {
            const brightness =
                imageData.data[i] + imageData.data[i + 1] + imageData.data[i + 2];
            if (brightness > maxBrightness) {
                maxBrightness = brightness;
                maxBrightnessPixel = imageData.data.subarray(i, i + 4);
            }
        }
        textElement.style.color = `rgb(${maxBrightnessPixel[0]}, ${maxBrightnessPixel[1]}, ${maxBrightnessPixel[2]})`;
    };
};

// get time

const time = function() {
    var currentDate = new Date();
    var dayNames = [
        "Sunday",
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
    ];
    document.getElementById("year").innerHTML = currentDate.getFullYear();
    document.getElementById("month").innerHTML = currentDate.getMonth() + 1;

    let date = currentDate.getDate().toString().padStart(2, "0");
    document.getElementById("date").innerHTML = date;

    var dayIndex = currentDate.getDay();
    document.getElementById("day").innerHTML = dayNames[dayIndex];
    getMaximumColorFromBackgroundAndSetText("#root", "date");
};

setInterval(time(), 1000);