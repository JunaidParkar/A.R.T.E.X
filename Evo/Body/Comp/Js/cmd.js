let engine = new CREngine();

// engine.addCommand("Evo", [{ flag: "--u", requireValue: true }, { flag: "--p", requireValue: true }], true, (flags) => {
//     console.log(flags);
// });

// engine.addCommand("Evo", [{ flag: "--h", requireValue: false }], true, (flags) => {
//     console.log(flags);
// });


var commandHistory = [];
var commandIndex = -1;

function checkInput() {
    var event = window.event || event.which;
    if (event.keyCode == 13) {
        var command = document.getElementById("textinput").value;
        addLine(command, "self");
        commandHistory.push(command);
        commandIndex = commandHistory.length;
        cmdExe(command)
        document.getElementById("textinput").value = "";
        document.getElementById("textinput").style.height = "1em";
        event.preventDefault();
    } else if (event.keyCode == 38) {
        if (commandIndex > 0) {
            commandIndex--;
            document.getElementById("textinput").value = commandHistory[commandIndex];
        }
        event.preventDefault();
    } else if (event.keyCode == 40) {
        if (commandIndex < commandHistory.length - 1) {
            commandIndex++;
            document.getElementById("textinput").value = commandHistory[commandIndex];
        }
        event.preventDefault();
    } else {
        document.getElementById("textinput").style.height = "";
        document.getElementById("textinput").style.height = document.getElementById("textinput").scrollHeight + "px";
    }
}

function addLine(line, author = null, error = false) {
    var d = document.createElement("div"),
        p = document.createElement("p")
    if (error) {
        d.classList.add("error")
    }
    if (author == "self") {
        let p2 = document.createElement("p")
        p2.textContent = "Evolution AI >> "
        d.appendChild(p2)
    }
    p.innerHTML = line;
    d.appendChild(p)
    document.getElementById("consoletext").appendChild(d);
}

const cmdExe = (c) => {
    let mc = ["Evo", "exit"]
    let imc = c.split(" ")
    if (mc.includes(imc[0])) {
        document.querySelector(".cmdInpWrapper").style.display = "none"
            // cmdEngine(c)
        engine.executeCommand("Evo --u username --p password");

        document.querySelector(".cmdInpWrapper").style.display = "flex"
    } else {
        addLine(line = `<br>${imc[0]} : \nThe term '${imc[0]}' is not recognized as the name of a cmdlet, function, script file, or operable program. Check
        the spelling of the name, or if a path was included, verify that the path is correct and try again.<br><br>
        At line:1 char:1<br><br>
        + ${imc[0]}`, null, true)
    }
}

const cmdEngine = (command) => {
    let c = command.split(" ")
    let cf = []
    let co = {
        "evo": {
            "flags": ["--h"]
        },
        "exit": {
            "flags": []
        }
    }
    for (let word of c) {
        if (co[c[0].toLowerCase()].flags.includes(word)) {
            cf.push(word)
        }
    }

    if (c[0].toLowerCase() == "evo") {
        let fi
        for (const f of cf) {
            if (f == "--h") {
                fi = c.indexOf("--h")
                el = c[fi - 1].toLowerCase()
                if (el == "evo") {
                    console.log("last")
                    let d = `<br><table><tr><th>Flags</th><th>Usage</th></tr><tr><th>--h</th><td>Used to get help with all functionalities of Evolution AI CMD.</td></tr></table><br>`
                    addLine(d)
                }
            }
        }
    }
    if (c[0].toLowerCase() == "exit") {
        let s = document.querySelector(".cmd").querySelector("nav").querySelector(".actionBar").querySelectorAll("img")[1]
        console.log(s)
        closeApp(s)
            // console.log(document.querySelector("cmd"))
    }
}

class cmdParser {
    constructor() {
        this.engine = engine
        this.commandHistory = this.engine.commandHistory
        this.commandIndex = this.engine.historyIndex
        this.addResponse = addLine
    }

    handleCommand() {
        var event = window.event || event.which;
        if (event.keyCode == 13) {
            event.preventDefault();
            var command = document.getElementById("textinput").value;
            // addLine(command, "self");
            this.commandHistory.push(command);
            this.commandIndex = this.commandHistory.length;
            this.engine.executeCommand(command)
                // cmdExe(command)
                // document.getElementById("textinput").value = "";
                // document.getElementById("textinput").style.height = "1em";
        } else if (event.keyCode == 38) {
            if (this.commandIndex > 0) {
                this.commandIndex--;
                document.getElementById("textinput").value = this.commandHistory[this.commandIndex];
            }
            event.preventDefault();
        } else if (event.keyCode == 40) {
            if (this.commandIndex < this.commandHistory.length - 1) {
                this.commandIndex++;
                document.getElementById("textinput").value = this.commandHistory[this.commandIndex];
            }
            event.preventDefault();
        } else {
            document.getElementById("textinput").style.height = "";
            document.getElementById("textinput").style.height = document.getElementById("textinput").scrollHeight + "px";
        }
    }
}