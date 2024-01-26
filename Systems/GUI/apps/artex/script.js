const chat_input = document.getElementById("chat-input")
const submit_query = document.getElementById("sendQuery")
const messages_box = document.getElementById("messages-box")

const copyCode = async (event) => {
  const codeElement = event.target.parentElement.parentElement.querySelector("code");
  const code = codeElement.textContent;

  try {
      await navigator.clipboard.writeText(code);
      const copyText = event.target.querySelector("p");
      copyText.textContent = "copied!";
      setTimeout(() => {
          copyText.textContent = "copy";
      }, 2000);
  } catch (err) {
      console.error("Failed to copy code: ", err);
  }
}

const add_message = (msg) => {
  const parser = new DOMParser();

  const doc = parser.parseFromString(msg, 'text/html');

  let p = document.createElement("div");
  p.innerHTML = doc.body.innerHTML;

  let code = p.querySelectorAll("code");

  if (code.length >= 1) {
      code.forEach(cd => {
          let tg = cd.parentElement;
          let div = document.createElement("div");
          div.classList.add("code-block");
          let header = document.createElement("div");
          header.classList.add("header");
          let header_p1 = document.createElement("p");
          console.log(cd.classList[0])

          try {header_p1.textContent = cd.classList[0].split("-")[1];} catch {header_p1.textContent = "None"}
          let copy = document.createElement("div");
          copy.id = "copy";
          copy.addEventListener("click", async (e) => await copyCode(e))
          let img = document.createElement("img");
          img.src = "../../assets/apps/default/artex/assets/copy.png";
          let copy_text = document.createElement("p");
          copy_text.textContent = "copy";
          copy.appendChild(img);
          copy.appendChild(copy_text);
          copy.addEventListener("click", copyCode);
          header.appendChild(header_p1);
          header.appendChild(copy);
          let block = document.createElement("div");
          block.classList.add("block");
          let pre = document.createElement("pre");
          let code_tg = document.createElement("code");
          code_tg.innerHTML = cd.innerHTML;
          pre.appendChild(code_tg);
          block.appendChild(pre);
          div.appendChild(header);
          div.appendChild(block);
          tg.replaceWith(div);
      });
  }
  
  let md = document.createElement("div")
  md.classList.add("ai")
  let imgm = document.createElement("img")
  imgm.src = "../../assets/apps/default/artex/assets/bot.png"
  md.appendChild(imgm)
  md.appendChild(p)
  messages_box.appendChild(md)
}

const takeInput = async () => {
  let query = chat_input.value
  let response = await eel.getResponse(query)()
  add_message(response)
}

// eel.expose(add_message)

submit_query.onclick = async () => {
  if (chat_input.value != "") {
    await takeInput()
  }
}