class CMD {
    constructor(applicationName, input, resultParent) {
        this.appName = applicationName
        this.input = input
        this.resultParent = resultParent
        this.addResult = resultAppender
        this.commandHistory = []
        this.commandIndex = -1
    }

    getFunctionalities() {
        var event = window.event || event.which;
        if (event.keyCode == 13) {
            let inp = this.input.value
            let dis = this.input.style.display
            if (inp.trim() == "") {
                return
            } else {
                this.commandHistory.push(command);
                this.commandIndex = this.commandHistory.length;
                // Process the command
            }
            this.input.style.display = dis
            this.input.value = ""
            event.preventDefault();
        } else if (event.keyCode == 38) {
            if (this.commandIndex > 0) {
                this.commandIndex--;
                this.input.value = this.commandHistory[this.commandIndex];
            }
            event.preventDefault();
        } else if (event.keyCode == 40) {
            if (this.commandIndex < this.commandHistory.length - 1) {
                this.commandIndex++;
                this.input.value = this.commandHistory[commandIndex];
            }
            event.preventDefault();
        } else {
            this.input.style.height = "";
            this.input.style.height = this.input.scrollHeight + "px";
        }
    }

    addCommand(commandName, flags, callBack) {
        let command = []
    }
}