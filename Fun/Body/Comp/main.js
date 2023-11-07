let navbar = document.getElementById("navbar")
let li = navbar.querySelector("ul").querySelectorAll("li")

li.forEach(elem => {
    let routeName = elem.querySelector("img").getAttribute("to")
    elem.querySelector("img").onclick = () => {
        window.location.href = `/main/${routeName}`
    }
})