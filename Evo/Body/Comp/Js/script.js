let minWidth = 1080
let minHeight = 607.5

// loadfn();

// document.addEventListener("keydown", function(e) {
//     if (e.keyCode === 82 || (e.ctrlKey && e.keyCode === 73)) {
//         e.preventDefault();
//     }
// });

// document.addEventListener("contextmenu", function(e) {
//     e.preventDefault();
// });

window.onload = async() => {
    console.log("opening")
    await openApp("cmd")
    document.querySelector(`.${"cmd"}`).classList.add("maximize");
    console.log("opened")
}

window.onresize = function() {
    // Calculate the new window size based on a 16:9 aspect ratio
    var newWidth = window.outerWidth;
    var newHeight = newWidth * 9 / 16;

    // Prevent the window from getting smaller than the minimum size
    if (newWidth < minWidth) {
        newWidth = minWidth;
    }
    if (newHeight < minHeight) {
        newHeight = minHeight;
    }

    // Set the new window size
    window.resizeTo(newWidth, newHeight);
};

if (window.outerWidth < minWidth || window.outerHeight < minHeight) {
    window.resizeTo(minWidth, minHeight);
}

const pt = {
    "cmd": "./Apps/CMD/cmd.html",
    "setting": "./Apps/Setting/setting.html",
    "chat": "./Apps/Chat/chat.html"
};

let appLists = document.querySelector(".iconsList").getElementsByTagName("ul")[0].querySelectorAll("li")

for (let apps of appLists) {
    apps.addEventListener("click", async(e) => {
        let name = apps.getElementsByTagName("p")[0].textContent.toLowerCase();
        if (!document.querySelector(`.${name}`)) {
            await openApp(name);
            document.querySelector(`.${name}`).classList.add("minimize");
        }
    });
}

const openApp = async(n) => {
    let p = pt[n]
    const f = await fetch(p)
    if (f.ok) {
        let h = await f.text()
        let d = document.createElement("div")
        d.classList.add(n.toLowerCase())
        d.innerHTML = h
        document.body.appendChild(d)
    }
}

const closeApp = (e) => {
    let el = e.parentElement.parentElement.parentElement.parentElement.querySelector("h3").textContent.toLowerCase()
    let h = document.querySelector(`.${el}`)
    document.body.removeChild(h)
}

const resize = (e) => {
    let s = e.parentElement.parentElement.parentElement
    if (s.classList.contains("maximize")) {
        minimize(s)
    } else {
        maximize(s)
    }
}

const maximize = (e) => {
    if (e.classList.contains("minimize")) {
        e.classList.remove("minimize")
    }
    if (e.classList.contains("maximize")) {
        return
    }
    e.classList.add("maximize")
    e.style.left = "50%"
    e.style.top = "50%"
    e.style.transform = "translate(-50%, -50%)"
}

const minimize = (e) => {
    if (e.classList.contains("maximize")) {
        e.classList.remove("maximize")
    }
    if (e.classList.contains("minimize")) {
        return
    }
    e.classList.add("minimize")
    e.style.left = "50%"
    e.style.top = "50%"
    e.style.transform = "translate(-50%, -50%)"
}

const observer = new MutationObserver((mutationsList, observer) => {
    for (let mutation of mutationsList) {
        if (mutation.type === 'childList') {
            let classes = ["cmd", "setting", "chat"]
            for (let elem of classes) {
                let e = document.querySelector(`.${elem}`)
                if (e) {
                    let n = e.querySelector("nav")
                    const mouseMoveHandler = function(e) { appDragger(e, elem); }.bind(e);
                    n.onmouseenter = () => {
                        n.onmousedown = () => {
                            if (!document.querySelector(`.${elem}`).querySelector("nav").classList.contains("active")) {
                                document.querySelector(`.${elem}`).querySelector("nav").classList.add("active")
                            }
                            n.addEventListener("mousemove", mouseMoveHandler)
                        }
                    }
                    n.onmouseup = () => {
                        if (document.querySelector(`.${elem}`).querySelector("nav").classList.contains("active")) {
                            document.querySelector(`.${elem}`).querySelector("nav").classList.remove("active")
                        }
                        n.removeEventListener("mousemove", mouseMoveHandler)
                    }
                    n.onmouseleave = () => {
                        n.removeEventListener("mouseenter", mouseMoveHandler)
                        n.removeEventListener("mousemove", mouseMoveHandler)
                        n.removeEventListener("mouseup", mouseMoveHandler)
                        n.removeEventListener("mouseleave", mouseMoveHandler)
                    }
                }
                // setting calibrations
                if (elem == classes[1]) {
                    if (document.querySelector(`.${classes[1]}`)) {
                        calibrateSettings()
                    }
                    // calibrateSettings()
                }
                // CMD input focus
                if (elem == classes[0]) {
                    if (document.querySelector("#textinput")) {
                        document.querySelector("#textinput").focus()
                    }
                }
            }
        }
    }
});

observer.observe(document.body, { childList: true, subtree: true });

const appDragger = ({ movementX, movementY }, elem) => {
    let wrapper = document.querySelector(`.${elem}`)
    let style = window.getComputedStyle(wrapper)
    let leftVal = parseInt(style.left)
    let topVal = parseInt(style.top)
    wrapper.style.left = `${leftVal + movementX}px`
    wrapper.style.top = `${topVal + movementY}px`
}

const showNotification = (heading, content) => {
    let no = document.querySelector(".notification")
    if (no) {
        closeNotification()
    }
    let n = document.createElement("div");
    n.classList.add("notification");

    let not = document.createElement("div");
    not.classList.add("navbar");

    let h = document.createElement("h3");
    h.innerHTML = heading;
    not.appendChild(h);

    let cncl = document.createElement("div");
    cncl.classList.add("cancelNotification");
    cncl.onclick = closeNotification;

    let i = document.createElement("img");
    i.src = "./assets/cross.png";
    cncl.appendChild(i);

    not.appendChild(cncl);

    let p = document.createElement("p");
    p.innerHTML = content;

    n.appendChild(not);
    n.appendChild(p);

    document.body.appendChild(n); // append the notification to the body

    setTimeout(function() {
        closeNotification(); // pass the notification element to the function
    }, 5000);
}

const closeNotification = () => {
    let n = document.querySelector(".notification")
    if (n) {
        document.body.removeChild(n)
    }
}