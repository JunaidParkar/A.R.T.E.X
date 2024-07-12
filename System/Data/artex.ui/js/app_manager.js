// alphabetical sorting function

const sortAppList = () => {
    let ul = document.getElementById("sidebarAppList");
    let lis = Array.from(ul.querySelectorAll("li"));
    lis.sort((a, b) => {
        let aText = a.querySelector("p").innerText;
        let bText = b.querySelector("p").innerText;
        return aText.localeCompare(bText);
    });
    ul.innerHTML = "";
    lis.forEach(li => {
        ul.appendChild(li);
    });
}

// Search app from list starts

const debounce = (func, wait) => {
    let timeout;
    return function (...args) {
        clearTimeout(timeout);
        timeout = setTimeout(() => func.apply(this, args), wait);
    };
};

const searchAppList = (query) => {
    let ul = document.getElementById("sidebarAppList");
    let lis = Array.from(ul.querySelectorAll("li"));
    query = query.toLowerCase();

    if (query === "") {
        sortAppList();
        return;
    }

    lis.sort((a, b) => {
        let aText = a.querySelector("p").innerText.toLowerCase();
        let bText = b.querySelector("p").innerText.toLowerCase();
        let aIndex = aText.indexOf(query);
        let bIndex = bText.indexOf(query);
        if (aIndex === -1) return 1;
        if (bIndex === -1) return -1;
        return aIndex - bIndex;
    });
    ul.innerHTML = "";
    lis.forEach(li => {
        ul.appendChild(li);
    });
}

const handleSearchInput = debounce((e) => {
    searchAppList(e.target.value);
}, 300);

const app_list = [[2, 'Chat', 'artex.chat', '1.0.0', 1], [3, 'File system', 'artex.fileSystem', '1.0.0', 1], [4, 'QR scanner', 'artex.qrScanner', '1.0.0', 1], [5, 'Setting', 'artex.setting', '1.0.0', 1], [6, 'Artex store', 'artex.store', '1.0.0', 1], [7, 'Artex', 'artex.ui', '1.0.0', 1], [8, 'Command prompt', 'artex.cmd', '1.0.0', 1]]

const close_app = (e) => {
    document.getElementById("app_container").removeChild(e.target.parentElement.parentElement)
}

const app_window_maker = (name, path) => {
    let div1 = document.createElement("div")
    div1.classList.add("appWindow")

    let div2 = document.createElement("div")
    div2.classList.add("header")
    let h4 = document.createElement("h4")
    h4.innerText = name
    let img = document.createElement("img")
    img.src = "./assets/icons/close.png"
    img.addEventListener("click", close_app)

    div2.appendChild(h4)
    div2.appendChild(img)
    div1.appendChild(div2)

    let iframe = document.createElement("iframe")
    iframe.src = path

    div1.appendChild(iframe)

    return div1
}

const app_opener = (e) => {
    console.log(e.target.dataset.name)
    document.getElementById("app_container").appendChild(app_window_maker(e.target.dataset.name, `../${e.target.dataset.package}/index.html`))
}

const add_app_to_menubar = () => {
    let ul = document.getElementById("sidebarAppList")
    ul.innerHTML = ""
    app_list.forEach(app => {
        let li = document.createElement("li")
        let img = document.createElement("img")
        let p = document.createElement("p")
        p.textContent = app[1]
        img.src = `../${app[2]}/logo.png`
        li.appendChild(img)
        li.appendChild(p)
        li.dataset.id = app[0]
        li.dataset.name = app[1]
        li.dataset.package = app[2]
        li.dataset.version = app[3]
        li.dataset.default = app[4]
        li.addEventListener("click", app_opener)
        ul.appendChild(li)
    })
    sortAppList()
}

add_app_to_menubar()