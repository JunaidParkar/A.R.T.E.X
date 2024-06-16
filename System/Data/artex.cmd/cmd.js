// initialize codereducer

let engine = new CREngine((e) => {
  submitResponse(e, false, true);
});

// add the terms for commands example command is "artex --h" here artex is called term
engine.addTerm("artex");
engine.addTerm("cloud");

// add the command and what should be performed when this command is entered
// remember the name i.e first argument i.e term is added by previous line
// second argument is an array with all the flags required for particular command
// eg: for authentication the command should look like "artex --u username --p password"
// here for flag --u and --p for both flags values are required. So for this the second argument will look like [{flag: "--u", requiredValue: true}, {flag: "--p", requiredValue: true}]
// third argument is an callback to define a function which  should execute on trigerring that specific command. it returns an argument which is the values of that flags which is set to true. examples are given below in second command
engine.addCommand("artex", [{ flag: "--h", requiredValue: false }], (args) => {
  let p1 = document.createElement("p");
  p1.textContent = "artex help here";
  submitResponse(p1);
});

engine.addCommand(
  "cloud",
  [
    { flag: "--u", requiredValue: true },
    { flag: "--p", requiredValue: true },
  ],
  (args) => {
    console.log(args);
    let p1 = document.createElement("p");
    p1.textContent = "help here";
    submitResponse(p1);
  }
);

// command prompt functionalities here

var commandHistory = [];
var commandIndex = -1;

function checkInput() {
  var event = window.event || event.which;
  // if enter is pressed
  if (event.keyCode == 13) {
    var command = document.getElementById("cmdInp").value;
    submitResponse(command, true);
    commandHistory.push(command);
    commandIndex = commandHistory.length;
    engine.executeCommand(command); // Execute command from codereducer
    document.getElementById("cmdInp").value = "";
    document.getElementById("cmdInp").style.height = "1em";
    event.preventDefault();
  } else if (event.keyCode == 38) {
    // if up arrow is pressed
    if (commandIndex > 0) {
      commandIndex--;
      document.getElementById("cmdInp").value = commandHistory[commandIndex];
    }
    event.preventDefault();
  } else if (event.keyCode == 40) {
    // if down arrow is pressed
    if (commandIndex < commandHistory.length - 1) {
      commandIndex++;
      document.getElementById("cmdInp").value = commandHistory[commandIndex];
    }
    event.preventDefault();
  }
}

// function that appends data as response in command prompt
// here data can be html or string. pass HTML only if author and error both are set to false else it should be an String
// author is by default set to false. it is true only when appending command written by user
// error is only true when you append any error
const submitResponse = (data, author = false, error = false) => {
  let cont = document.getElementById("history");
  let div = document.createElement("div");
  author ? div.classList.add("inp") : div.classList.add("output");
  if (author) {
    let p1 = document.createElement("p");
    p1.textContent = "artex >";
    let p2 = document.createElement("p");
    p2.textContent = data;
    div.appendChild(p1);
    div.appendChild(p2);
  } else {
    if (error) {
      let p3 = document.createElement("p");
      p3.classList.add("error");
      p3.textContent = data;
      div.appendChild(p3);
    } else {
      div.appendChild(data);
    }
  }
  cont.appendChild(div);
};
