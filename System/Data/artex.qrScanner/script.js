class QRScanner {
    constructor() {
        this.video = document.getElementById("video");
        this.canvas = document.getElementById("canvas");
        this.ctx = this.canvas.getContext("2d");
        this.qr_result = document.getElementById("qr_result");
        this.dropzone = document.getElementById("main_camera");
        this.activate_mode = null;
        this.scanning = false;
        this.activate_mode == "camera" ? this.dropzone.classList.remove("drag") : this.dropzone.classList.add("drag");
        document.getElementById("toggle_scan_btn").getElementsByTagName("p")[0].textContent = this.activate_mode == "camera" ? "Scan with qr image" : "Scan via camera";
        document.getElementById("toggle_scan_btn").addEventListener("click", () => this.scan());
        document.getElementById("reload").addEventListener("click", () => this.scan(true));
    }

    scan(reload = false) {
        this.activate_mode = !reload ? (this.activate_mode == "camera" ? "image" : "camera") : this.activate_mode;
        if (this.activate_mode == "camera") {
            this.drag_and_drop_stop();
            this.startCamera();
        } else {
            this.stopCamera();
            this.drag_and_drop_start();
        }
        this.activate_mode == "camera" ? this.dropzone.classList.remove("drag") : this.dropzone.classList.add("drag");
        document.getElementById("toggle_scan_btn").getElementsByTagName("p")[0].textContent = this.activate_mode == "camera" ? "Scan with qr image" : "Scan via camera";
    }

    startCamera() {
        this.qr_result.innerText = "";
        navigator.mediaDevices.getUserMedia({ video: { facingMode: 'user' } })
            .then((stream) => {
                this.video.srcObject = stream;
                this.video.play();
                this.video.addEventListener('loadedmetadata', () => {
                    this.canvas.width = this.video.videoWidth;
                    this.canvas.height = this.video.videoHeight;
                    this.scanning = true;
                    this.scanCamera();
                });
            })
            .catch(function (error) {
                console.error('Error accessing camera:', error);
            });
    }

    stopCamera() {
        try {
            const stream = this.video.srcObject;
            if (stream) {
                const tracks = stream.getTracks();
                tracks.forEach(track => track.stop());
                this.video.srcObject = null;
            }
            this.scanning = false;
        } catch (error) {
            console.error('Error stopping camera:', error);
        }
    }

    drawLine(begin, end, color) {
        this.ctx.beginPath();
        this.ctx.moveTo(begin.x, begin.y);
        this.ctx.lineTo(end.x, end.y);
        this.ctx.lineWidth = 4;
        this.ctx.strokeStyle = color;
        this.ctx.stroke();
    }

    scanCamera() {
        if (!this.scanning) return;
        this.ctx.drawImage(this.video, 0, 0, this.canvas.width, this.canvas.height);
        const imageData = this.ctx.getImageData(0, 0, this.canvas.width, this.canvas.height);
        const code = jsQR(imageData.data, imageData.width, imageData.height);

        if (code) {
            this.drawLine(code.location.topLeftCorner, code.location.topRightCorner, '#FF3B58');
            this.drawLine(code.location.topRightCorner, code.location.bottomRightCorner, '#FF3B58');
            this.drawLine(code.location.bottomRightCorner, code.location.bottomLeftCorner, '#FF3B58');
            this.drawLine(code.location.bottomLeftCorner, code.location.topLeftCorner, '#FF3B58');

            this.qr_result.textContent = code.data;
            this.scanning = false;
            this.video.pause();
        } else {
            requestAnimationFrame(() => this.scanCamera());
        }
    }

    drag_and_drop_start() {
        this.qr_result.innerText = "";
        this.dropzone.addEventListener("dragover", this.dragOver.bind(this));
        this.dropzone.addEventListener("dragleave", this.dragLeave.bind(this));
        this.dropzone.addEventListener("drop", this.drop.bind(this));
    }

    drag_and_drop_stop() {
        this.dropzone.removeEventListener("dragover", this.dragOver.bind(this));
        this.dropzone.removeEventListener("dragleave", this.dragLeave.bind(this));
        this.dropzone.removeEventListener("drop", this.drop.bind(this));
    }

    dragOver(event) {
        event.preventDefault();
        this.dropzone.classList.add("dragover");
    }

    dragLeave() {
        this.dropzone.classList.remove("dragover");
    }

    drop(event) {
        event.preventDefault();
        this.dropzone.classList.remove("dragover");
        const files = event.dataTransfer.files;
        this.handleFiles(files);
    }

    scan_img(qr) {
        const file = qr[0];
        if (file) {
            const reader = new FileReader();

            reader.onload = () => {
                const img = new Image();
                img.onload = () => {
                    this.canvas.width = img.width;
                    this.canvas.height = img.height;
                    this.ctx.drawImage(img, 0, 0);
                    const imageData = this.ctx.getImageData(0, 0, this.canvas.width, this.canvas.height);
                    const code = jsQR(imageData.data, imageData.width, imageData.height);
                    if (code) {
                        this.qr_result.textContent = code.data;
                    } else {
                        this.qr_result.textContent = "No QR code found.";
                    }
                };
                img.src = reader.result;
            };

            reader.readAsDataURL(file);
        }
    }

    handleFiles(files) {
        if (files.length == 1) {
            const dataTransfer = new DataTransfer();
            const file = files[0];
            dataTransfer.items.add(file);
            const qr_image = dataTransfer.files;
            this.scan_img(qr_image);
        } else {
            console.error("Only one file to be selected at a time...");
        }
    }
}

let scanner = new QRScanner();
scanner.scan();
