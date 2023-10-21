class CREngine {
    constructor() {
        this.commands = {};
        this.commandHistory = [];
        this.historyIndex = 0;
    }

    addCommand(name, flags, action) {
        let f = [];
        let r = [];
        flags.forEach(cmd => {
            f.push(cmd.flag);
            r.push(cmd.requiredValue);
        });

        // Check if the command already exists, if not, initialize an empty array
        this.commands[name] = this.commands[name] || { operations: [] };

        this.commands[name].operations.push({
            flags: f,
            requiredValue: r,
            action: action // Store the function directly
        });
    }

    executeCommand(input) {
        // const formattedCommands = {};
        // for (const command in this.commands) {
        //     formattedCommands[command] = {
        //         operations: this.commands[command].operations.map(op => ({
        //             flags: op.flags,
        //             requiredValue: op.requiredValue,
        //             action: op.action.toString()
        //         }))
        //     };
        // }
        // console.log(JSON.stringify(formattedCommands, null, 2));
        let inpArray = input.split(" ")
        let inpCMDName = inpArray[0]
        console.log(this.verifyFlags(input))


    }

    verifyFlags(inputCommand) {
        let inp = inputCommand.split(" ")
        let dataset = this.commands[inp[0]]
        if (!dataset) {
            console.error(`Command ${inp[0]} not available`)
            return false
        }
        let inpFlags = []
        for (const c of inp) {
            if (c.startsWith("--")) {
                inpFlags.push(c);
            }
        }
        let flagIndex = this.getFlagIndex(dataset.operations, inpFlags)

        if (flagIndex === undefined) {
            console.error(`Incorrect flags. Please Enter ${inp[0]} --h for help`)
            return false
        }

        let av = []

        dataset.operations[flagIndex].flags.forEach(ifl => {
            if (!inpFlags.includes(ifl)) {
                av.push("f")
            } else {
                av.push("t")
            }
        })

        let allFlagsPresent = true;

        av.forEach((stmt, ind) => {
            if (stmt == "f") {
                console.error(`Flag ${dataset.operations[flagIndex].flags[ind]} is missing`)
                allFlagsPresent = false;
            }
        })
        return allFlagsPresent
    }

    getFlagIndex(operation, inputFlags) {
        for (let i = 0; i < operation.length; i++) {
            for (let j = 0; j < operation[i].flags.length; j++) {
                for (let k = 0; k < inputFlags.length; k++) {
                    if (!(operation[i].flags.indexOf(inputFlags[k]) === -1)) {
                        return i
                    }
                }
            }
        }
    }
}

var aa = new CREngine();

aa.addCommand("Evo", [{ flag: "--h", requiredValue: false }], args => {
    // do something
    console.log("Hey from function");
});

aa.addCommand("Evo", [{ flag: "--u", requiredValue: true }, { flag: "--p", requiredValue: true }], args => {
    // do something
    console.log("Hey from function2");
});

aa.executeCommand("Evo --p --u");
// aa.executeCommand("Evo --u username");
// aa.executeCommand("Evo --u username --p password");


var storedData = {
    "Evo": {
        "operations": [{
                "flags": ["--h"],
                "requiredValue": [false],
                "action": "args => {\r\n    // do something\r\n    console.log(\"Hey from function\");\r\n}"
            },
            {
                "flags": ["--u", "--p"],
                "requiredValue": [true, true],
                "action": "args => {\r\n    // do something\r\n    console.log(\"Hey from function2\");\r\n}"
            }
        ]
    }
}