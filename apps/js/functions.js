document.oncontextmenu = e => e.preventDefault()
document.getElementById("window_screen").oncontextmenu = e => {
    let menu = document.getElementById("contextMenu");
    if (menu.style.display == "block") document.getElementById("contextMenu").style.display = "none"
    let clickX = e.clientX;
    let clickY = e.clientY;
    let gap = 5;
    let windowWidth = document.getElementById("window_screen").clientWidth;
    let windowHeight = document.getElementById("window_screen").clientHeight;
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
}

window.onclick = () => {
    document.getElementById("contextMenu").style.display = "none"
}

const map_numbers = (current, minimum_output, maximum_output, minimum_input, maximum_input) => {
    if (maximum_input === minimum_input) {
        throw new Error("Minimum input and maximum input cannot be the same.");
    }
    return ((current - minimum_input) * (maximum_output - minimum_output)) / (maximum_input - minimum_input) + minimum_output;
};

const get_background_image_matching_colours = (element) => {
    element = document.querySelector(element);
    let backgroundImage = getComputedStyle(element).backgroundImage;
    let imageUrl = backgroundImage.replace(/url\(['"]?(.*?)['"]?\)/, "$1");
    let img = new Image();
    img.src = imageUrl;
    return new Promise((resolve, reject) => {
        img.onload = function() {
            let canvas = document.createElement("canvas");
            canvas.width = img.width;
            canvas.height = img.height;
            let ctx = canvas.getContext("2d");
            ctx.drawImage(img, 0, 0);
            let imageData = ctx.getImageData(0, 0, canvas.width, canvas.height);
            let maxBrightness = 0;
            let maxBrightnessPixel = null;
            for (let i = 0; i < imageData.data.length; i += 4) {
                let brightness =
                    imageData.data[i] + imageData.data[i + 1] + imageData.data[i + 2];
                if (brightness > maxBrightness) {
                    maxBrightness = brightness;
                    maxBrightnessPixel = imageData.data.subarray(i, i + 4);
                }
            }
            resolve(maxBrightnessPixel);
        };
        img.onerror = function() {
            reject(new Error("Failed to load image"));
        };
    });
};

const rgbToHsl = (r, g, b) => {
    r /= 255, g /= 255, b /= 255;
    let max = Math.max(r, g, b),
        min = Math.min(r, g, b);
    let h, s, l = (max + min) / 2;

    if (max === min) {
        h = s = 0;
    } else {
        let d = max - min;
        s = l > 0.5 ? d / (2 - max - min) : d / (max + min);
        switch (max) {
            case r:
                h = (g - b) / d + (g < b ? 6 : 0);
                break;
            case g:
                h = (b - r) / d + 2;
                break;
            case b:
                h = (r - g) / d + 4;
                break;
        }
        h /= 6;
    }
    return [h * 360, s * 100, l * 100];
}

const hslToRgb = (h, s, l) => {
    let r, g, b;

    s /= 100;
    l /= 100;

    let k = (n) => (n + h / 30) % 12;
    let f = (n) => l - l * s * Math.max(Math.min(k(n), 1), -1);
    r = Math.round(255 * f(0));
    g = Math.round(255 * f(8));
    b = Math.round(255 * f(4));

    return [r, g, b];
}

const generateContrastingColor = (r, g, b, a) => {
    let [h, s, l] = rgbToHsl(r, g, b);
    let newHue = (h + 180) % 360;
    let newSaturation = Math.min(100, s + 20);
    let newLightness = l > 50 ? l - 30 : l + 30;
    let [newR, newG, newB] = hslToRgb(newHue, newSaturation, newLightness);
    return [newR, newG, newB, a];
}

const fetchTime = () => {
    let now = new Date();
    let year = now.getFullYear();
    let months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ];
    let month = Number(String(now.getMonth() + 1).padStart(2, '0'));
    let date = Number(String(now.getDate()).padStart(2, '0'));
    let hours = Number(String(now.getHours()).padStart(2, '0'));
    let minutes = Number(String(now.getMinutes()).padStart(2, '0'));
    document.getElementById("time").innerText = `${hours == 0 ? "12" : hours > 12 ? String(hours - 12).padStart(2, "0") : ""}:${String(minutes).padStart(2, "0")} ${hours < 12 ? "AM" : "PM"}`.trim();
    document.getElementById("date").innerText = `${String(date).padStart(2, "0")} ${months[month - 1]} ${year}`
    let msUntilNextMinute = (60 - now.getSeconds()) * 1000 - now.getMilliseconds();
    setTimeout(fetchTime, msUntilNextMinute);
}