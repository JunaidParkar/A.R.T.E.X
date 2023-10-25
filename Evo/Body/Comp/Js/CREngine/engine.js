class CREngine {
    constructor() {
        this.commands = {};
        this.commandHistory = [];
        this.historyIndex = 0;
    }

    addCommand(name, flags, action, error) {
        let f = [];
        let r = [];
        flags.forEach(cmd => {
            f.push(cmd.flag);
            r.push(cmd.requiredValue);
        });

        this.commands[name] = this.commands[name] || { operations: [] };

        this.commands[name].operations.push({
            flags: f,
            requiredValue: r,
            action: action,
            error: error
        });
    }

    executeCommand(input) {
        let inpArray = input.split(" ")
        let inpCMDName = inpArray[0]
        let ds = this.commands[inpArray[0]]
        let aaa = this.verifyFlags(input)
        if (aaa[0]) {
            let val = this.verifyValues(aaa[1], input)
            let callBackArgs = []
            console.log(val)
            val.forEach(elm => {
                if (elm.requiredValue) {
                    if (elm.value) {
                        callBackArgs.push({ flag: elm.flag, value: elm.value })
                    } else {
                        callBackArgs = []
                        console.log(ds.operations[aaa[1]])
                        ds.operations[aaa[1]].error(`value not provided for ${elm.flag}`)
                    }
                } else {
                    callBackArgs.push({ flag: elm.flag, value: elm.value })
                }
            })
            if (callBackArgs.length > 0) {
                ds.operations[aaa[1]].action(callBackArgs)
            }
        } else {
            console.log("error")
        }
    }

    verifyFlags(inputCommand) {
        let inp = inputCommand.split(" ")
        let dataset = this.commands[inp[0]]
        if (!dataset) {
            dataset.operations[0].error(`Command ${inp[0]} not available`)
            return [false, `Command ${inp[0]} not available`]
        }
        let inpFlags = []
        for (const c of inp) {
            if (c.startsWith("--")) {
                inpFlags.push(c);
            }
        }
        let flagIndex = this.getFlagIndex(dataset.operations, inpFlags)

        if (flagIndex === undefined) {
            dataset.operations[flagIndex].error(`Incorrect flags. Please Enter ${inp[0]} --h for help`)
            return [false, `Incorrect flags. Please Enter ${inp[0]} --h for help`]
        }

        let av = []

        dataset.operations[flagIndex].flags.forEach(ifl => {
            if (!inpFlags.includes(ifl)) {
                av.push("f")
            } else {
                av.push("t")
            }
        })

        let allFlagsPresent = [true, flagIndex];

        av.forEach((stmt, ind) => {
            if (stmt == "f") {
                dataset.operations[flagIndex].error(`Flag ${dataset.operations[flagIndex].flags[ind]} is missing`)
                allFlagsPresent = [false, `Flag ${dataset.operations[flagIndex].flags[ind]} is missing`];
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

    verifyValues(index, input) {
        let inp = input.split(" ")
        let dataset = this.commands[inp[0]]
        let inpFlags = []
        let values = []
        for (const c of inp) {
            if (c.startsWith("--")) {
                inpFlags.push(c);
            }
        }
        let af = dataset.operations[index].flags
        for (let i = 0; i < af.length; i++) {
            let d = dataset.operations[index].requiredValue[i]
            if (d) {
                let ind = inp.indexOf(af[i])
                if (ind + 1 > inp.length - 1) {
                    values.push({ flag: af[i], value: undefined, requiredValue: true })
                } else if (inp[ind + 1].startsWith("--")) {
                    values.push({ flag: af[i], value: undefined, requiredValue: true })
                } else {
                    values.push({ flag: af[i], value: inp[ind + 1], requiredValue: true })
                }
            } else {
                values.push({ flag: af[i], value: undefined, requiredValue: false })
            }
        }
        return values
    }
}

// let engine = new CREngine();

// engine.addCommand("Evo", [{ flag: "--u", requiredValue: true }, { flag: "--p", requiredValue: true }], args => {
//     console.log(args, "from args")
// }, error => {
//     console.log(error, "from error")
// })

// engine.executeCommand("Evo --u username")

// var aa = new CREngine();

// aa.addCommand("Evo", [{ flag: "--h", requiredValue: false }], args => {
//     // do something
//     console.log("Hey from function");
// });

// aa.addCommand("Evo", [{ flag: "--u", requiredValue: true }, { flag: "--p", requiredValue: true }], args => {
//     // do something
//     console.log("Hey from function2");
// });

// aa.executeCommand("Evo --h")
// aa.executeCommand("Evo --p parkar --u junaid");
// aa.executeCommand("Evo --u username --p");
// aa.executeCommand("Evo --u username --p password");
// aa.executeCommand("Evo --i")

// var storedData = {
//     "Evo": {
//         "operations": [{
//                 "flags": ["--h"],
//                 "requiredValue": [false],
//                 "action": "args => {\r\n    // do something\r\n    console.log(\"Hey from function\");\r\n}"
//             },
//             {
//                 "flags": ["--u", "--p"],
//                 "requiredValue": [true, true],
//                 "action": "args => {\r\n    // do something\r\n    console.log(\"Hey from function2\");\r\n}"
//             }
//         ]
//     }
// }