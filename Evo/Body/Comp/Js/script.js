const pt = {
    "cmd": "./Apps/CMD/cmd.html",
    "setting": "./Apps/Setting/setting.html"
};

let appLists = document.querySelector(".iconsList").getElementsByTagName("ul")[0].querySelectorAll("li")

for (let apps of appLists) {
    apps.addEventListener("click", async (e) => {
        let name = apps.getElementsByTagName("h1")[0].textContent.toLowerCase();
        if (!document.querySelector(`.${name}`)) {
            await openApp(name);
            document.querySelector(`.${name}`).classList.add("minimize");
        }
    });
}

const openApp = async (n) => {
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
    let el = e.parentElement.parentElement.parentElement.querySelector("h3").textContent.toLowerCase()
    let h = document.querySelector(`.${el}`)
    document.body.removeChild(h)
}

const resize = (e) => {
    if (e.parentElement.parentElement.parentElement.classList.contains("maximize")) {
        minimize(e)
    } else {
        maximize(e)
    }
}

const maximize = (e) => {
    if (e.parentElement.parentElement.parentElement.classList.contains("minimize")) {
        e.parentElement.parentElement.parentElement.classList.remove("minimize")
    }
    if (e.parentElement.parentElement.parentElement.classList.contains("maximize")) {
        return
    }
    e.parentElement.parentElement.parentElement.classList.add("maximize")
    e.parentElement.parentElement.parentElement.style.left = "50%"
    e.parentElement.parentElement.parentElement.style.top = "50%"
    e.parentElement.parentElement.parentElement.style.transform = "translate(-50%, -50%)"
}

const minimize = (e) => {
    if (e.parentElement.parentElement.parentElement.classList.contains("maximize")) {
        e.parentElement.parentElement.parentElement.classList.remove("maximize")
    }
    if (e.parentElement.parentElement.parentElement.classList.contains("minimize")) {
        return
    }
    e.parentElement.parentElement.parentElement.classList.add("minimize")
    e.parentElement.parentElement.parentElement.style.left = "50%"
    e.parentElement.parentElement.parentElement.style.top = "50%"
    e.parentElement.parentElement.parentElement.style.transform = "translate(-50%, -50%)"
}

const observer = new MutationObserver((mutationsList, observer) => {
    for (let mutation of mutationsList) {
        if (mutation.type === 'childList') {
            let classes = ["cmd", "setting"]
            for (let elem of classes) {
                let e = document.querySelector(`.${elem}`)
                if (e) {
                    let n = e.querySelector("nav")
                    const mouseMoveHandler = function (e) { appDragger(e, elem); }.bind(e);
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