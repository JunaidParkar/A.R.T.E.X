// Search app from list starts

const debounce = (func, wait) => {
    let timeout;
    return function(...args) {
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

let app = new AppHandler()

const app_list = [
    [2, 'Chat', 'artex.chat', '1.0.0', 1],
    [3, 'File system', 'artex.fileSystem', '1.0.0', 1],
    [4, 'QR scanner', 'artex.qrScanner', '1.0.0', 1],
    [5, 'Setting', 'artex.setting', '1.0.0', 1],
    [6, 'Artex store', 'artex.store', '1.0.0', 1],
    [7, 'Artex', 'artex.ui', '1.0.0', 1],
    [8, 'Command prompt', 'artex.cmd', '1.0.0', 1]
]

app.add_to_menubar(app_list)