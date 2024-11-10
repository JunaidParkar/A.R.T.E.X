const appList = [{
        name: "Junaid Parkar",
        id: "junaid468",
        icon: "appTry/home.png",
        isDefault: true,
        version: "1.0.0",
        appPkg: "https://junaid-parkar.web.app"
    },
    {
        name: "sleek pad",
        id: "sleekpad8468",
        icon: "appTry/home.png",
        isDefault: true,
        version: "1.0.0",
        appPkg: "https://sleekpad-0.web.app/"
    },
    {
        name: "Zestlark",
        id: "ZestLark878956",
        icon: "appTry/home.png",
        isDefault: true,
        version: "1.0.0",
        appPkg: "https://zestlark-0.web.app/"
    },
    {
        name: "Github",
        id: "github846897",
        icon: "appTry/home.png",
        isDefault: true,
        version: "1.0.0",
        appPkg: "https://github.com/JunaidParkar"
    }
]

const appFrameBuilder = app => {
    let mainDiv = document.createElement("div")
    mainDiv.classList.add("app_frame")
    mainDiv.id = app.id
    mainDiv.dataset.appWindow = app.id

    let headerDiv = document.createElement("div")
    headerDiv.classList.add("header")
    let headerh3 = document.createElement("h3")
    headerh3.innerText = app.name
    let control_center_div = document.createElement("div")
    control_center_div.classList.add("control_center")
    let img = document.createElement("img")
    img.src = "./assets/icons/close.svg"
    img.onclick = () => closeApp(app.id)
    control_center_div.appendChild(img)
    headerDiv.appendChild(headerh3)
    headerDiv.appendChild(control_center_div)

    let frameDiv = document.createElement("div")
    frameDiv.classList.add("frame")
    let iframe = document.createElement("iframe")
    iframe.src = app.appPkg
    iframe.frameBorder = 0
    frameDiv.appendChild(iframe)

    mainDiv.appendChild(headerDiv)
    mainDiv.appendChild(frameDiv)

    return mainDiv
}

const taskbarAppBuilder = app => {
    let div = document.createElement("div")
    div.classList.add("taskbar-icon", "pinned")
    let img = document.createElement("img")
    img.src = app.icon
    img.alt = app.id
    img.title = app.name
    div.appendChild(img)
    return div
}

const menuBarAppBuilder = app => {
    let mainDiv = document.createElement("div")
    mainDiv.classList.add("app_container")
    let img = document.createElement("img")
    img.src = app.icon
    mainDiv.appendChild(img)

    let div = document.createElement("div")
    div.classList.add("app_information")
    let p = document.createElement("p")
    p.innerText = app.name
    let span = document.createElement("span")
    span.innerText = app.version
    div.appendChild(p)
    div.appendChild(span)
    mainDiv.appendChild(div)
    return mainDiv
}

const listApp = () => {
    appList.forEach(app => {
        let taskbarApp = taskbarAppBuilder(app)
        let menuApp = menuBarAppBuilder(app)
        taskbarApp.onclick = () => openApp(app.id)
        menuApp.onclick = () => openApp(app.id)
        document.getElementById("pinned-apps").appendChild(taskbarApp)
        document.getElementById("all_apps_container").appendChild(menuApp)
    });
    console.log("made App")
}

const openApp = id => {
    let app = appList.find(app => app.id == id)
    if (!app) {
        console.log("no app")
        return
    }
    console.log(app)
    let frame = appFrameBuilder(app)
    document.getElementById("window_screen").appendChild(frame)

}

const closeApp = id => {
    let elem = document.getElementById(id)
        // if (elem.dataset.appWindow) {

    // }
    // console.log( ? "yes" : "no")
    if (elem.dataset.appWindow == id) {
        elem.parentElement.removeChild(elem)
    }
}