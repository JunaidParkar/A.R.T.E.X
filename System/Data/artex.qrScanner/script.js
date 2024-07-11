let activate_mode = "image";
const video = document.getElementById('video');
const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');
const qr_result = document.getElementById("qr_result");
const dropzone = document.getElementById("main_camera");
const file_list = document.getElementById("file_list");
const file_input = document.getElementById("file_inp");

const handleFiles = (files) => {
  file_list.innerHTML = ''; // Clear any existing file list

  if (files.length > 0) {
    const dataTransfer = new DataTransfer();
    const file = files[0];
    dataTransfer.items.add(file);

    const li = document.createElement('li');
    li.textContent = `File: ${file.name} (${file.type}, ${file.size} bytes)`;
    file_list.appendChild(li);
    
    file_input.files = dataTransfer.files;
    console.log(file_input.files);
    scan()
  }
};

dropzone.addEventListener('dragover', (event) => {
  event.preventDefault();
  dropzone.classList.add('dragover');
});

dropzone.addEventListener('dragleave', () => {
  dropzone.classList.remove('dragover');
});

dropzone.addEventListener('drop', (event) => {
  event.preventDefault();
  dropzone.classList.remove('dragover');

  const files = event.dataTransfer.files;
  handleFiles(files);
});


let scanning = false;

activate_mode == "camera" ? document.getElementById("main_camera").classList.remove("drag") : document.getElementById("main_camera").classList.add("drag")
document.getElementById("scan_with_img_btn").getElementsByTagName("p")[0].textContent = activate_mode == "camera" ? "Scan with qr image" : "Scan via camera"

const drawLine = (begin, end, color) => {
    ctx.beginPath();
    ctx.moveTo(begin.x, begin.y);
    ctx.lineTo(end.x, end.y);
    ctx.lineWidth = 4;
    ctx.strokeStyle = color;
    ctx.stroke();
}

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
        
        qr_result.textContent = code.data;
        scanning = false;
        video.pause();
    } else {
        requestAnimationFrame(scanCode);
    }
}


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

function scan(e=null) {
        const file = e.target.files[0] | document.getElementById("file_inp").files[0];
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
                    qr_result.textContent = code.data;
                } else {
                    qr_result.textContent = 'No QR code found.';
                }
            };
            img.src = reader.result;
        };
        
        reader.readAsDataURL(file);
    }

// Event listener for input file change (image-based scanning)
// qrInput.addEventListener('change', function (e) {
//     const file = e.target.files[0];
//     const reader = new FileReader();
    
//     reader.onload = function () {
//         const img = new Image();
//         img.onload = function () {
//             canvas.width = img.width;
//             canvas.height = img.height;
//             ctx.drawImage(img, 0, 0);
//             const imageData = ctx.getImageData(0, 0, canvas.width, canvas.height);
//             const code = jsQR(imageData.data, imageData.width, imageData.height);
//             if (code) {
//                 qr_result.textContent = code.data;
//             } else {
//                 qr_result.textContent = 'No QR code found.';
//             }
//         };
//         img.src = reader.result;
//     };
    
//     reader.readAsDataURL(file);
// });

// Start camera-based scanning
if (activate_mode == "camera") {
    startCamera();
}