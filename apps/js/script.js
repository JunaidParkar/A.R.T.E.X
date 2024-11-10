let bg_lisy = ["bg1, bg2, bg3, bg4"]

document.querySelector("#window_screen").classList.add("bg4")

listApp()

fetchTime()

get_background_image_matching_colours("#window_screen")
    .then((maxBgColor) => {
        console.log("colouring")
        if (!maxBgColor) {
            maxBgColor = [255, 255, 255, 255]
        }
        maxBgColor = [maxBgColor[0], maxBgColor[1], maxBgColor[2], map_numbers(maxBgColor[3], 0, 1, 0, 255)]
        document.getElementById("taskbar").style.background = `rgba(${maxBgColor[0]}, ${maxBgColor[1]}, ${maxBgColor[2]}, ${maxBgColor[3]})`
            // document.getElementById("menu_screen_section").style.background = `rgba(${maxBgColor[0]}, ${maxBgColor[1]}, ${maxBgColor[2]}, ${maxBgColor[3]})`
        document.getElementById("time").style.color = `rgba(${maxBgColor[0]}, ${maxBgColor[1]}, ${maxBgColor[2]}, ${maxBgColor[3]})`
        document.getElementById("date").style.color = `rgba(${maxBgColor[0]}, ${maxBgColor[1]}, ${maxBgColor[2]}, ${maxBgColor[3]})`
        let app_elements = []
            // Array.from(document.querySelectorAll(".taskbar-icon")).forEach(dom => app_elements.push(dom))
        Array.from(document.querySelectorAll(".app_container")).forEach(dom => dom.style.background = `rgba(${maxBgColor[0]}, ${maxBgColor[1]}, ${maxBgColor[2]}, ${maxBgColor[3]})`)
    })
    .catch((error) => {
        console.error(error);
    });

console.log("This code runs without waiting for the image to process");

const screenMenuToggler = () => {
    document.getElementById("menu_main_section").style.display = document.getElementById("menu_main_section").style.display == "none" ? "flex" : "none"
}

// let c = getCursorPosition("window_screen")

// console.log(c)

openApp("junaid8468")