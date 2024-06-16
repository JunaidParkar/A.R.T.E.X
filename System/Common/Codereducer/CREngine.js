class CREngine {
    constructor(defError) {
      this.commands = {};
      this.commandHistory = [];
      this.historyIndex = 0;
      this.defError = defError;
      this.flagIndex = null;
    }
  
    addTerm(name) {
      let nm = this.commands[name];
      if (!nm) {
        this.commands[name] = {};
      } else {
        console.warn(`Term ${name} already exist`);
      }
    }
  
    addCommand(name, flags, action) {
      let nm = this.commands[name];
      if (!nm) {
        console.warn(
          `Term ${name} does't exist. please add the term by method addTerm`
        );
        return;
      }
      let f = [];
      let r = [];
      flags.forEach((cmd) => {
        f.push(cmd.flag);
        r.push(cmd.requiredValue);
      });
  
      this.commands[name] = this.commands[name] || { operations: [] };
      let op = this.commands[name].operations;
  
      if (!op) {
        this.commands[name].operations = [];
      }
  
      this.commands[name].operations.push({
        flags: f,
        requiredValue: r,
        action: action,
      });
    }
  
    executeCommand(input) {
      let inpArray = input.split(" ");
      let nm = this.commands[inpArray[0]];
      if (!nm) {
        this.defError(
          `'${inpArray[0]}' is not recognized as an internal or external command, operable program or batch file.`
        );
        return;
      }
      let ds = this.commands[inpArray[0]];
      let aaa = this.verifyFlags(input);
      if (aaa) {
        let val = this.verifyValues(input);
        let callBackArgs = [];
        val.forEach((elm) => {
          if (elm.requiredValue) {
            if (elm.value) {
              callBackArgs.push({ flag: elm.flag, value: elm.value });
            } else {
              callBackArgs = [];
              this.defError(`value not provided for ${elm.flag}`);
            }
          } else {
            callBackArgs.push({ flag: elm.flag, value: elm.value });
          }
        });
        if (callBackArgs.length > 0) {
          ds.operations[this.flagIndex].action(callBackArgs);
        }
      }
    }
  
    verifyFlags(inputCommand) {
      let inp = inputCommand.split(" ");
      let dataset = this.commands[inp[0]];
      let inpFlags = [];
      for (const c of inp) {
        if (c.startsWith("--")) {
          inpFlags.push(c);
        }
      }
      let flagIndex = this.getFlagIndex(dataset.operations, inpFlags);
      if (flagIndex === undefined) {
        this.defError(`Incorrect flags. Please Enter ${inp[0]} --h for help`);
        return false;
      }
  
      let av = [];
  
      dataset.operations[flagIndex].flags.forEach((ifl) => {
        if (!inpFlags.includes(ifl)) {
          av.push("f");
        } else {
          av.push("t");
        }
      });
  
      this.flagIndex = flagIndex;
  
      av.forEach((stmt, ind) => {
        if (stmt == "f") {
          this.defError(
            `Flag ${dataset.operations[flagIndex].flags[ind]} is missing`
          );
          return false;
        }
      });
      return true;
    }
  
    getFlagIndex(operation, inputFlags) {
      for (let i = 0; i < operation.length; i++) {
        for (let j = 0; j < operation[i].flags.length; j++) {
          for (let k = 0; k < inputFlags.length; k++) {
            if (!(operation[i].flags.indexOf(inputFlags[k]) === -1)) {
              return i;
            }
          }
        }
      }
    }
  
    verifyValues(input) {
      let inp = input.split(" ");
      let dataset = this.commands[inp[0]];
      let inpFlags = [];
      let values = [];
      for (const c of inp) {
        if (c.startsWith("--")) {
          inpFlags.push(c);
        }
      }
      let af = dataset.operations[this.flagIndex].flags;
      for (let i = 0; i < af.length; i++) {
        let d = dataset.operations[this.flagIndex].requiredValue[i];
        if (d) {
          let ind = inp.indexOf(af[i]);
          console.log(ind);
          if (ind + 1 > inp.length - 1 || ind <= 0) {
            values.push({ flag: af[i], value: undefined, requiredValue: true });
          } else if (inp[ind + 1].startsWith("--")) {
            values.push({ flag: af[i], value: undefined, requiredValue: true });
          } else {
            values.push({
              flag: af[i],
              value: inp[ind + 1],
              requiredValue: true,
            });
          }
        } else {
          values.push({ flag: af[i], value: undefined, requiredValue: false });
        }
        //   console.log(values);
      }
      return values;
    }
  }