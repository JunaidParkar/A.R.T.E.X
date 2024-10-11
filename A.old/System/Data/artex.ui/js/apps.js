class AppManager {
    constructor() {}

    close_app(e) {
        document.getElementById("app_container").removeChild(document.getElementById("app_container").getElementsByClassName(e)[0]);
        document.getElementById("recentMenu").removeChild(document.getElementById("recentMenu").getElementsByClassName(e)[0]);
    }

    add_recent_app(data) {
        let div = document.createElement("div");
        div.classList.add("recentApp");
        div.classList.add(data[0]);

        let div1 = document.createElement("div");
        let h3 = document.createElement("h3");
        h3.textContent = data[1];

        let img = document.createElement("img");
        img.src = "./assets/icons/close.png";
        img.addEventListener("click", () => this.close_app(data[0]));

        let div2 = document.createElement("div");
        let iframe = document.createElement("iframe");
        iframe.src = `../${data[2]}/index.html`;

        div1.appendChild(h3);
        div1.appendChild(img);
        div2.appendChild(iframe);
        div.appendChild(div1);
        div.appendChild(div2);

        document.getElementById("recentMenu").appendChild(div);
    }

    create_app(name, path, id) {
        let div1 = document.createElement("div");
        div1.classList.add("appWindow");
        div1.classList.add(id);

        let div2 = document.createElement("div");
        div2.classList.add("header");

        let h4 = document.createElement("h4");
        h4.innerText = name;

        let img = document.createElement("img");
        img.src = "./assets/icons/close.png";
        img.addEventListener("click", () => this.close_app(id));

        div2.appendChild(h4);
        div2.appendChild(img);
        div1.appendChild(div2);

        let iframe = document.createElement("iframe");
        iframe.src = path;
        div1.appendChild(iframe);

        document.getElementById("app_container").appendChild(div1);
    }

    open_app(event) {
        const { name, package: pkg, id } = event.target.dataset;
        this.create_app(name, `../${pkg}/index.html`, id);
        this.add_recent_app([id, name, pkg]);
    }
}

class AppHandler extends AppManager {
    sort_app() {
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

    add_to_menubar(app_list) {
        let ul = document.getElementById("sidebarAppList");
        ul.innerHTML = "";
        app_list.forEach(app => {
            let li = document.createElement("li");
            let img = document.createElement("img");
            let p = document.createElement("p");
            p.textContent = app[1];
            img.src = `../${app[2]}/logo.png`;
            li.appendChild(img);
            li.appendChild(p);
            li.dataset.id = app[0];
            li.dataset.name = app[1];
            li.dataset.package = app[2];
            li.dataset.version = app[3];
            li.dataset.default = app[4];
            li.addEventListener("click", (e) => this.open_app(e)); // Use arrow function to preserve `this`
            ul.appendChild(li);
        });
        this.sort_app();
    }
}