const closeApp = id => {
    let elem = document.getElementById(id)
        // if (elem.dataset.appWindow) {

    // }
    // console.log( ? "yes" : "no")
    if (elem.dataset.appWindow == id) {
        elem.parentElement.removeChild(elem)
    }
}