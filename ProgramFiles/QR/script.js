// Selecting elements from HTML
const video = document.getElementById('qr-video');
const canvas = document.getElementById('qr-canvas');
const ctx = canvas.getContext('2d');
const qrResult = document.getElementById('qr-result');
const qrInput = document.getElementById('qr-input');

// Variables for camera-based scanning
let scanning = false;

// Function to start camera-based scanning
function startCamera() {
    navigator.mediaDevices.getUserMedia({ video: { facingMode: 'user' } })
        .then(function (stream) {
            video.srcObject = stream;
            video.play();
            video.addEventListener('loadedmetadata', function() {
                canvas.width = video.videoWidth;
                canvas.height = video.videoHeight;
                scanning = true;
                scanCode();
            });
        })
        .catch(function (error) {
            console.error('Error accessing camera:', error);
        });
}

// Function to scan the QR code from camera feed
function scanCode() {
    if (!scanning) return;
    
    ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
    const imageData = ctx.getImageData(0, 0, canvas.width, canvas.height);
    const code = jsQR(imageData.data, imageData.width, imageData.height);

    if (code) {
        drawLine(code.location.topLeftCorner, code.location.topRightCorner, '#FF3B58');
        drawLine(code.location.topRightCorner, code.location.bottomRightCorner, '#FF3B58');
        drawLine(code.location.bottomRightCorner, code.location.bottomLeftCorner, '#FF3B58');
        drawLine(code.location.bottomLeftCorner, code.location.topLeftCorner, '#FF3B58');
        
        qrResult.textContent = code.data;
        scanning = false;
        video.pause();
    } else {
        requestAnimationFrame(scanCode);
    }
}

// Function to draw a line on the canvas
function drawLine(begin, end, color) {
    ctx.beginPath();
    ctx.moveTo(begin.x, begin.y);
    ctx.lineTo(end.x, end.y);
    ctx.lineWidth = 4;
    ctx.strokeStyle = color;
    ctx.stroke();
}

// Event listener for input file change (image-based scanning)
qrInput.addEventListener('change', function (e) {
    const file = e.target.files[0];
    const reader = new FileReader();
    
    reader.onload = function () {
        const img = new Image();
        img.onload = function () {
            canvas.width = img.width;
            canvas.height = img.height;
            ctx.drawImage(img, 0, 0);
            const imageData = ctx.getImageData(0, 0, canvas.width, canvas.height);
            const code = jsQR(imageData.data, imageData.width, imageData.height);
            if (code) {
                qrResult.textContent = code.data;
            } else {
                qrResult.textContent = 'No QR code found.';
            }
        };
        img.src = reader.result;
    };
    
    reader.readAsDataURL(file);
});

// Start camera-based scanning
startCamera();