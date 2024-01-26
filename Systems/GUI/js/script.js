// resize to minimal size

let res = true;

const clearRes = () => {
  setTimeout(() => {
    res = true;
  }, 3000);
};

const resizeFunction = (e) => {
  resizeTimeout = setTimeout(() => {
    if (res) {
      let minWidth = 1080;
      let minHeight = 720;
      if (window.innerHeight < minHeight || window.innerWidth < minWidth) {
        console.log(
          window.innerWidth < minWidth ? minWidth : window.innerWidth,
          window.innerHeight < minHeight ? minHeight : window.innerHeight
        );
        res = false;
        window.resizeTo(
          window.innerWidth < minWidth ? minWidth : window.innerWidth,
          window.innerHeight < minHeight ? minHeight : window.innerHeight
        );
        clearRes();
      }
    } else return;
  }, 2000);
};

window.addEventListener("resize", resizeFunction);

// search app on typing

document.getElementById("searchAppInput").addEventListener("input", (e) => {
  if (e.target.value != "") {
    searchAppList("", true);
  }
  searchAppList(e.target.value);
});

// search bar get news

let defaultKeyWords = [
  "india",
  "AI",
  "machine",
  "Science",
  "Technology",
  "earth",
  "games",
];

const getNews = async (keyword) => {
  if (!keyword) {
    keyword =
      defaultKeyWords[Math.floor(Math.random() * defaultKeyWords.length)];
  }
  try {
    document.getElementById("news-container").innerHTML = "";
    let preloader = document.createElement("div");
    preloader.classList.add("articlePreloader");
    let loader = document.createElement("div");
    loader.classList.add("loader");
    preloader.appendChild(loader);
    document.getElementById("news-container").appendChild(preloader);
    const url = "https://eventregistry.org/api/v1/article/getArticles";
    const data = `{
      "action": "getArticles",
      "keyword": "${keyword}",
      "articlesPage": 1,
      "articlesCount": 5,
      "articlesSortBy": "date",
      "articlesSortByAsc": false,
      "articlesArticleBodyLen": -1,
      "resultType": "articles",
      "dataType": [
        "news",
        "pr"
      ],
      "apiKey": "f2bb630d-ceca-4a20-9a04-28ccf0f71b8c",
      "forceMaxDataTimeWindow": 31
    }`;
    const response = await fetch(url, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: data,
    });
    const text = await response.json();
    const articles = text.articles.results;
    document.getElementById("news-container").innerHTML = "";
    if (articles.length > 0) {
      const articlesContainer = document.getElementById("news-container");
      articles.forEach((article) => {
        const articleDiv = document.createElement("div");
        articleDiv.classList.add("article");
        const titleElement = document.createElement("h2");
        titleElement.textContent = article.title;
        const sourceElement = document.createElement("p");
        sourceElement.textContent = `Source: ${article.source.title}`;
        const bodyElement = document.createElement("p");
        bodyElement.textContent = article.body;
        const linkElement = document.createElement("a");
        linkElement.href = article.url;
        linkElement.textContent = "Read More";
        const imageElement = document.createElement("img");
        imageElement.src = article.image;
        imageElement.alt = article.title;
        imageElement.onerror = () => {
          imageElement.style.display = "none";
        };
        articleDiv.appendChild(imageElement);
        articleDiv.appendChild(titleElement);
        articleDiv.appendChild(sourceElement);
        articleDiv.appendChild(bodyElement);
        articleDiv.appendChild(linkElement);
        articlesContainer.appendChild(articleDiv);
      });
    } else {
      getNews(
        defaultKeyWords[Math.floor(Math.random() * defaultKeyWords.length)]
      );
    }
  } catch (e) {
    notifyUser(
      "Unable to load news at the moment. If problem presist then please check your internet connection.",
      "",
      false,
      false,
      true
    );
  }
};

// open or close search menu

const toggleSearchMenu = async (open = false, close = false) => {
  let search_menu = document.getElementById("search-menu");
  let inp = document.getElementById("searchAppInput");
  if (!open && !close) {
    if (search_menu.style.display == "block") {
      search_menu.style.display = "none";
    } else {
      search_menu.style.display = "block";
      inp.focus();
      await getNews();
    }
  }
  if (open) {
    search_menu.style.display = "block";
    inp.focus();
    await getNews();
  }
  if (close) {
    search_menu.style.display = "none";
  }
};

document.getElementById("searchBtn").addEventListener("click", () => {
  toggleSearchMenu();
});

// search bar functioning after some time of typing

let timer;
const waitTime = 1000;
const messageInput = document.getElementById("searchAppInput");
messageInput.addEventListener("keyup", (e) => {
  clearTimeout(timer);

  timer = setTimeout(() => {
    doneTyping(e.target.value);
  }, waitTime);
});

const doneTyping = async (value) => {
  if (value != "") {
    console.log(value);
    await getNews(value);
  } else await getNews();
};

// Setting observer to detect changes

const observer = new MutationObserver(function (mutationsList, observer) {
  for (const mutation of mutationsList) {
    if (mutation.type === "childList") {
      mutation.addedNodes.forEach(function (node) {
        node.childNodes.forEach((nd) => {
          if (nd.nodeName === "IFRAME") {
            attachEventHandlers(nd);
          }
        });
      });
    }
  }
});

observer.observe(document, { childList: true, subtree: true });
