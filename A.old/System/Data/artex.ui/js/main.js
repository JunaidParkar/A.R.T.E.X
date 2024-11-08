// sidebar toggler start

sidebarToggler()
app.sort_app()

document.getElementById("sidebarToggler").onclick = () => {
    sidebarActive = !sidebarActive
    sidebarToggler()
}

// sidebar toggler ends

// taskbar starts

let sideBarBtns = Array.from(document.querySelectorAll(".sidebarBtn"))

sideBarBtns.forEach(btn => {
    btn.onclick = () => {
        btn.classList.toggle("active")
    }
})

// taskbar ends

// sidebar app search starts

document.getElementById("appSearchInput").addEventListener("input", handleSearchInput);

// sidebar app search ends

// handle right and left click starts

window.addEventListener("contextmenu", rightClick)
window.addEventListener("click", leftClick)

// handle right and left click ends


// display date on home screen start

setInterval(time(), 1000);

// display date on home screen end

// window.onbeforeunload = e => {
//     e.preventDefault()
//     eel.closeApp()
// }