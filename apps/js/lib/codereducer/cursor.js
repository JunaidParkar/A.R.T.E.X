const getCursorPosition = (elem) => {
    document.getElementById(elem).onmousemove = e => {
        return [e.screenX, e.screenY]
    }
}