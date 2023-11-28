let input = document.getElementById("inp")
let cmd = document.getElementById("cmd")

window.onload = () => {
    focusInput()
    resizeInput()
}

input.addEventListener('input', () => resizeInput());

cmd.addEventListener("click", () => focusInput())

const resizeInput = () => {
    let contentWidth = input.scrollWidth;
    input.style.width = contentWidth + 'px';
}

const focusInput = () => {
    input.focus()
}