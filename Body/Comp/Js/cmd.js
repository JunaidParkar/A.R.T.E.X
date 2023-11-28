let addError = (line) => {
    addLine(line, false, null, true)
}

let engine = new CREngine((e) => addError(e));

engine.addTerm("Evo")

engine.addCommand("Evo", [{ flag: "--h", requiredValue: false }], args => {
    let table = document.createElement("table")
    let row1 = document.createElement("tr")
    let tr1th1 = document.createElement("th")
    tr1th1.textContent = "Flags"
    let tr1th2 = document.createElement("th")
    tr1th2.textContent = "Usage"
    row1.appendChild(tr1th1)
    row1.appendChild(tr1th2)
    let row2 = document.createElement("tr")
    let tr2th1 = document.createElement("th")
    tr2th1.textContent = "--h"
    let tr2td2 = document.createElement("td")
    tr2td2.textContent = "Used to get help with all functionalities of Evolution AI CMD."
    row2.appendChild(tr2th1)
    row2.appendChild(tr2td2)
    table.appendChild(row1)
    table.appendChild(row2)
    console.log(table)
    addLine(table, true)
})

engine.addCommand("Evo", [{ flag: "--getVoices", requiredValue: false }], args => {
    eel.get_available_voices()().then(function (voices) {
        let table = document.createElement("table")
        let row1 = document.createElement("tr")
        let tr1th1 = document.createElement("th")
        tr1th1.textContent = "Id"
        let tr1th2 = document.createElement("th")
        tr1th2.textContent = "Name"
        row1.appendChild(tr1th1)
        row1.appendChild(tr1th2)
        table.appendChild(row1)
        voices.forEach(function (voice) {
            let row2 = document.createElement("tr")
            let tr2th1 = document.createElement("th")
            tr2th1.textContent = voice.index
            let tr2td2 = document.createElement("td")
            tr2td2.textContent = voice.name
            row2.appendChild(tr2th1)
            row2.appendChild(tr2td2)
            table.appendChild(row2)
        });
        addLine(table, true)
    })
})

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
        addLine(command, false, "self");
        commandHistory.push(command);
        commandIndex = commandHistory.length;
        // cmdExe(command)
        engine.executeCommand(command)
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

function addLine(line, isHTML = false, author = null, error = false) {
    let d = document.createElement("div");
    let p = document.createElement("p");

    if (error) {
        d.classList.add("error");
    }

    if (author == "self") {
        let p2 = document.createElement("p");
        p2.textContent = "Evolution AI >> ";
        d.appendChild(p2);
    }

    if (isHTML) {
        p.appendChild(line);
    } else {
        p.innerHTML = line;
    }
    d.appendChild(p);

    console.log(line)
    console.log(p)

    document.getElementById("consoletext").appendChild(d);
}