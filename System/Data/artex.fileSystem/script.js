// header section starts

let header = document.getElementById("header");
let pth = document.getElementById("path");
let pthInput = document.getElementById("pathInput");

header.onclick = () => {
  if (pthInput.classList.contains("active")) {
    pthInput.classList.remove("active");
  }
  if (!pth.classList.contains("active")) {
    pth.classList.add("active");
  }
};

pth.onclick = (e) => {
  e.stopPropagation();
  if (!pthInput.classList.contains("active")) {
    pthInput.classList.add("active");
  }
  if (pth.classList.contains("active")) {
    pth.classList.remove("active");
  }
  let spans = pth.querySelectorAll("span");
  let values = [];
  spans.forEach((span) => {
    values.push(span.innerText);
  });
  pthInput.querySelector("input").value = values.join("/");
  pthInput.querySelector("input").focus();
};

pthInput.onclick = (e) => {
  e.stopPropagation();
  pthInput.querySelector("input").focus();
};

pthInput.querySelector("input").onkeyup = (e) => {
  var event = window.event || e.which;
  if (event.keyCode == 13) {
    let input = pthInput.querySelector("input").value.split("/");
    document.getElementById("path").innerHTML = "";

    let elems = [];
    input.forEach((word, index) => {
      if (word != "" && word != " ") {
        console.log(word != "", word);
        let spn = document.createElement("span");
        spn.innerText = word;
        elems.push(spn);
        let img = document.createElement("img");
        img.src = "../../assets/apps/default/fileManager/assets/forward.png";
        elems.push(img);
      }
    });

    if (
      elems[elems.length - 1] &&
      elems[elems.length - 1].tagName &&
      elems[elems.length - 1].tagName.toLowerCase() === "img"
    ) {
      elems.pop();
    }

    elems.forEach((elem) => {
      document.getElementById("path").appendChild(elem);
    });

    if (pthInput.classList.contains("active")) {
      pthInput.classList.remove("active");
    }
    if (!pth.classList.contains("active")) {
      pth.classList.add("active");
    }
  }
};

const changePath = (path) => {
  document.getElementById("path").innerHTML = "";
  path = path.trim().split("/");
  let elems = [];
  path.forEach((word, index) => {
    if (word != "" && word != " ") {
      let spn = document.createElement("span");
      spn.innerText = word;
      elems.push(spn);
      let img = document.createElement("img");
      img.src = "../../assets/apps/default/fileManager/assets/forward.png";
      elems.push(img);
    }
  });

  if (
    elems[elems.length - 1] &&
    elems[elems.length - 1].tagName &&
    elems[elems.length - 1].tagName.toLowerCase() === "img"
  ) {
    elems.pop();
  }

  elems.forEach((elem) => {
    document.getElementById("path").appendChild(elem);
  });
};

// header section ends

document.getElementById('hamburger').addEventListener('click', () => {
  document.getElementById('sidebar').style.left = 0
})

document.getElementById('close-sidebar').addEventListener('click', () => {
  document.getElementById('sidebar').style.left = "-150vw"
})


// hamberger

// hamberger end

// file manager section starts

let drives = document
  .getElementById("drives")
  .querySelector("ul")
  .querySelectorAll("li");

drives.forEach((drive) => {
  if (drive.hasAttribute("clickAble")) {
    drive.onclick = () => {
      if (!drive.classList.contains("active")) {
        drives.forEach((dr) => {
          if (dr.classList.contains("active")) {
            dr.classList.remove("active");
          }
        });
        drive.classList.add("active");
        let path = drive.getAttribute("root-path");
        changePath(path);
      }
    };
  }
});

// file manager section ends

// folder and file sorting starts

const sortBy = "folder";

const dataSorter = () => {
  const sorted = [[], []];
  const items = Array.from(
    document.getElementById("file-list").querySelectorAll("li")
  );

  for (const item of items) {
    if (item.dataset.type === sortBy) {
      sorted[0].push(item);
    } else {
      sorted[1].push(item);
    }
  }

  document.getElementById("file-list").innerHTML = "";
  sorted
    .flat()
    .forEach((item) => document.getElementById("file-list").appendChild(item));
};

dataSorter();

// folder and file sorting ends
