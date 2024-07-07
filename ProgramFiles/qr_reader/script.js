const fileInput = document.getElementById('fileInput');
const qrImage = document.getElementById('qrImage');
const canvas = document.getElementById('canvas');
const context = canvas.getContext('2d');
const resultElement = document.getElementById('result');

fileInput.addEventListener('change', handleFile);

function handleFile(event) {
    const file = event.target.files[0];
    if (!file) {
        return;
    }
    const reader = new FileReader();
    reader.onload = function(e) {
        qrImage.src = e.target.result;
        qrImage.onload = function() {
            canvas.width = qrImage.width;
            canvas.height = qrImage.height;
            context.drawImage(qrImage, 0, 0, canvas.width, canvas.height);
            const imageData = context.getImageData(0, 0, canvas.width, canvas.height);
            const code = jsQR(imageData.data, imageData.width, imageData.height, {
                inversionAttempts: "dontInvert",
            });
            if (code) {
                drawLine(code.location.topLeftCorner, code.location.topRightCorner, "#FF3B58");
                drawLine(code.location.topRightCorner, code.location.bottomRightCorner, "#FF3B58");
                drawLine(code.location.bottomRightCorner, code.location.bottomLeftCorner, "#FF3B58");
                drawLine(code.location.bottomLeftCorner, code.location.topLeftCorner, "#FF3B58");
                resultElement.innerText = `QR Code Data: ${code.data}`;
            } else {
                resultElement.innerText = "No QR code detected.";
            }
        };
    };
    reader.readAsDataURL(file);
}

function drawLine(begin, end, color) {
    context.beginPath();
    context.moveTo(begin.x, begin.y);
    context.lineTo(end.x, end.y);
    context.lineWidth = 4;
    context.strokeStyle = color;
    context.stroke();
}