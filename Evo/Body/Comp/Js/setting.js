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
            // eel.updateSetting("appTransperacy", false)
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
            // eel.updateSetting("appTransperacy", true)
    }
}

const calibrateSettings = () => {
    let cl = document.querySelector(".transparentCheckbox")
    if (cl) {
        if (document.body.classList.contains("noTransparent")) {
            cl.classList.contains("active") ? cl.classList.remove("active") : ""
            console.log("1")
        } else {
            cl.classList.contains("active") ? "" : cl.classList.add("active")
            console.log("2")
        }
    }
}

const checkUpdate = () => {
    let u = document.querySelector("#updateBtn")
    let ur = document.querySelector(".updateResult")
    u.classList.add("none")
    ur.classList.remove("none")
    showNotification("Update", "Please do not close Evolution AI untill update is completed.")
}