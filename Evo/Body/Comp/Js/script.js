// function breakText(text, maxWidth) {
//     var words = text.split(" ");
//     var newText = "";
//     var currentLine = "";
//     for (var i = 0; i < words.length; i++) {
//         if (currentLine.length + words[i].length + 1 > maxWidth) { // Add 1 for the hyphen
//             newText += currentLine + "\n-";
//             currentLine = words[i];
//         } else if (currentLine.length + words[i].length >= maxWidth) { // If the current line is already at the max width, break it and add the hyphen
//             newText += currentLine + "\n-";
//             currentLine = words[i];
//         } else {
//             currentLine += words[i] + " ";
//         }
//     }
//     if (currentLine.length > 0) {
//         newText += currentLine;
//     }
//     return newText;
// }


// document.querySelectorAll(".iconNames").forEach((elem, ind) => {
//     var textDiv = elem;
//     var text = textDiv.textContent;
//     var newText = breakText(text, 40);
//     // console.log(newText)
//     textDiv.textContent = newText;
// })

function importHtml(htmlFile) {
    var xhr = new XMLHttpRequest();
    xhr.open("GET", htmlFile, true);
    xhr.onload = function () {
        if (xhr.status === 200) {
            var html = xhr.responseText;
            var element = document.createElement("div");
            element.innerHTML = html;
            document.body.appendChild(element);
        }
    };
    xhr.send();
}  