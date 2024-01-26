// app list from sqlite3 database

const apps = [{
        name: "artex",
        image: "./assets/apps/default/artex/icon/logo.png",
        appPath: "./apps/artex/index.html",
        default: true,
    },
    {
        name: "File manager",
        image: "./assets/apps/default/fileManager/icon/logo.png",
        appPath: "./apps/fileManager/index.html",
        default: true,
    },
    {
        name: "setting",
        image: "./assets/apps/default/setting/icon/logo.png",
        appPath: "./apps/setting/index.html",
        default: true,
    },
    {
        name: "terminal",
        image: "./assets/apps/default/terminal/icon/logo.png",
        appPath: "./apps/terminal/index.html",
        default: true,
    },
    {
        name: "Artex store",
        image: "./assets/apps/default/artexStore/icon/logo.png",
        appPath: "./apps/artexstore/index.html",
        default: true,
    },
    {
        name: "bing",
        image: "https://img.icons8.com/?size=48&id=pOADWgX6vV63&format=png",
        appPath: "https://wwwtrue.bing.com/",
        default: false,
    },
    {
        name: "playgroundai",
        image: "https://yt3.googleusercontent.com/QPpa9S5D-4Bw2P9WciQyLPcp7GzHPJ7fM-SUuxaRcGUIWTLYLuiVtLjpPgI-SGrljPzvpJBlsts=s900-c-k-c0x00ffffff-no-rj",
        appPath: "https://playgroundai.com/",
        default: false,
    },
    {
        name: "Sleekpad",
        image: "https://sleekpad-0.web.app/assets/logo-d879986a.png",
        appPath: "https://sleekpad-0.web.app/notes",
        default: false,
    },
    {
        name: "PI AI",
        image: "https://pi.ai/pi-logo-32.png?v=2",
        appPath: "https://pi.ai/talk",
        default: false,
    },
    {
        name: "Deep ai",
        image: "https://deepai.org/static/images/flopsicon.svg",
        appPath: "https://deepai.org/",
        default: false,
    },
];

let mainAppList = document.getElementById("appList");
let defaultAppList = document.getElementById("default-apps");
mainAppList.innerHTML = "";
defaultAppList.innerHTML = "";

apps.forEach((app) => {
    let li = document.createElement("li");
    let img = document.createElement("img");
    img.src = app.image;
    img.dataset.default = app.default;
    img.dataset.name = app.name;
    li.appendChild(img);

    if (app.default) {
        defaultAppList.appendChild(li.cloneNode(true));
    } else {}
    let p = document.createElement("p");
    p.textContent = app.name;
    li.appendChild(p);
    mainAppList.appendChild(li.cloneNode(true));
});

// app list searching algorithm

const searchAppList = (name, byName = false) => {
    let resLi = document.getElementById("appMatched");
    resLi.innerHTML = "";
    console.log(name);
    let lis = Array.from(
        document.getElementById("appList").querySelectorAll("li")
    );
    if (byName) {
        lis.sort((a, b) =>
            a
            .querySelector("p")
            .textContent.localeCompare(b.querySelector("p").textContent)
        );
    } else {
        lis.sort((a, b) => {
            const nameA = a.querySelector("p").textContent.toLowerCase();
            const nameB = b.querySelector("p").textContent.toLowerCase();
            const matchesA = nameA.split(name.toLowerCase()).length - 1;
            const matchesB = nameB.split(name.toLowerCase()).length - 1;
            return matchesB - matchesA;
        });
    }
    const ul = document.getElementById("appList");
    ul.innerHTML = "";
    lis.forEach((li) => ul.appendChild(li));
    let res = ul.querySelector("li").querySelector("p").innerText;
    if (res.toLocaleLowerCase() == name.toLocaleLowerCase()) {
        let elem = ul.querySelector("li").cloneNode(true);
        resLi.appendChild(elem);
    } else {
        let li = document.createElement("li");
        li.classList.add("error");
        let img = document.createElement("img");
        img.src = "../assets/system/icons/logo.png";
        let p = document.createElement("p");
        p.textContent = "No App Found";
        li.appendChild(img);
        li.appendChild(p);
        resLi.appendChild(li);
    }
};

searchAppList("", true);

const manageAppState = async(li) => {
    await toggleSearchMenu(false, true);
    let mainContainer = document.getElementById("apps");
    let ifr = mainContainer.querySelectorAll("iframe");
    if (ifr.length > 0) {
        let appIfr = Array.from(ifr).find((fr) => {
            return fr.dataset.name == li.querySelector("img").dataset.name;
        });
        if (appIfr) {
            if (appIfr.parentElement.nextSibling) {
                mainContainer.removeChild(appIfr.parentElement);
            } else {
                closeApp(appIfr.parentElement);
                return false;
            }
        }
    }

    openApp(li.querySelector("img").dataset.name);
};

const openApp = (name) => {
    apps.forEach((app) => {
        if (app.name == name) {
            let div = document.createElement("div");
            div.style.background = "black"
            div.classList.add("app");
            let iframe = document.createElement("iframe");
            iframe.dataset.name = app.name;
            iframe.src = app.appPath;
            div.appendChild(iframe);
            if (app.default) {
                let defLi = document
                    .getElementById("default-apps")
                    .querySelectorAll("li");
                let defSelLi = Array.from(defLi).find((li) => {
                    return li.querySelector("img").dataset.name == app.name;
                });
                if (!defSelLi.classList.contains("select")) {
                    defSelLi.classList.add("select");
                }
            } else {
                let rufLi = document
                    .getElementById("other-apps")
                    .querySelectorAll("li");
                let rli = Array.from(rufLi).find((li) => {
                    return li.querySelector("img").dataset.name == app.name;
                });
                if (rli == undefined) {
                    let li = document.createElement("li");
                    let img = document.createElement("img");
                    img.src = app.image;
                    img.dataset.name = app.name;
                    li.appendChild(img);
                    li.classList.add("select");
                    li.addEventListener("click", async() => await manageAppState(li));
                    document.getElementById("other-apps").appendChild(li);
                }
                if (
                    document.getElementById("other-apps").querySelectorAll("li").length >
                    4
                ) {
                    document.getElementById("other-apps").classList.contains("overlap") ?
                        "" :
                        document.getElementById("other-apps").classList.add("overlap");
                } else {
                    document.getElementById("other-apps").classList.contains("overlap") ?
                        document.getElementById("other-apps").classList.remove("overlap") :
                        "";
                }
            }
            document.getElementById("apps").appendChild(div);
        }
    });
};

const closeApp = (elem) => {
    let name = elem.querySelector("iframe").dataset.name;
    let appShowcase = [
        document.getElementById("default-apps"),
        document.getElementById("other-apps"),
    ];
    let allLI = [
        ...Array.from(appShowcase[0].querySelectorAll("li")),
        ...Array.from(appShowcase[1].querySelectorAll("li")),
    ];
    let liApp = allLI.find((li) => li.querySelector("img").dataset.name == name);
    if (liApp.classList.contains("select")) {
        liApp.classList.remove("select");
    }
    if (liApp.parentElement.id == "other-apps") {
        liApp.parentElement.removeChild(liApp);
    }
    document.getElementById("apps").removeChild(elem);
};

const minimizeapp = (elem) => {
    elem.style.display = "none"
}

let allUls = document.querySelectorAll("ul");
let allAppUls = [];

allUls.forEach((ul) => {
    if (ul.dataset.applist != undefined) {
        allAppUls.push(ul);
    }
});

allAppUls.forEach((ul) => {
    let lis = ul.querySelectorAll("li");
    lis.forEach((li) => {
        li.addEventListener("click", async() => {
            await manageAppState(li);
        });
    });
});