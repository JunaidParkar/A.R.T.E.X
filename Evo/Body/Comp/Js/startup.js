const loadfn = async() => {
    let settings = await eel.getSetting()();
    if (settings["appTransperacy"]) {
        document.body.classList.contains("noTransparent") ? document.body.classList.remove("noTransparent") : ""
        document.body.classList.contains("transparent") ? "" : document.body.classList.add("transparent")
    } else {
        document.body.classList.contains("noTransparent") ? "" : document.body.classList.add("noTransparent")
        document.body.classList.contains("transparent") ? document.body.classList.remove("transparent") : ""
    }
}

document.body.onload = loadfn()