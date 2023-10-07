// let ttcb = document.querySelector(".transparentCheckbox").addEventListener('')

// ttcb.addEventListener('click', () => {
//     console.log("hy")
// })

const appTranperacyToggle = () => {
    let ttcb = document.querySelector(".transparentCheckbox").classList
    if (ttcb.contains("active")) {
        ttcb.remove("active")
        let bc = document.body.classList
        if (bc.contains("noTransparent")) {
            return
        }
        if (bc.contains("transparent")) {
            bc.remove("transparent")
        }
        bc.add("noTransparent")
    } else {
        ttcb.add("active")
        let bc = document.body.classList
        if (bc.contains("noTransparent")) {
            bc.remove("noTransparent")
        }
        if (bc.contains("transparent")) {
            return
        }
        bc.add("transparent")
    }
}