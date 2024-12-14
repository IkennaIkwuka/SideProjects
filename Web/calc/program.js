let screen = document.getElementById("screen");
let action = document.getElementById("action");
let invisiText = document.getElementById("invisiText");
let answer = document.getElementById("answer");
function one() {
    screen.append(1);
}
function two() {
    screen.append(2);
}
function three() {
    screen.append(3);
}
function four() {
    screen.append(4);
}
function five() {
    screen.append(5);
}
function six() {
    screen.append(6);
}
function seven() {
    screen.append(7);
}
function eight() {
    screen.append(8);
}
function nine() {
    screen.append(9);
}
function zero() {
    screen.append(0);
}
function point() {
    screen.append(".")
}
function exponential() {
    answer.innerHTML = screen.innerHTML * 2.71828;
    screen.innerHTML = "";
}
function plus() {
    action.append("+");
    invisiText.innerHTML = screen.innerHTML;
    screen.innerHTML = "";
}
function minus() {
    action.append("-");
    invisiText.innerHTML = screen.innerHTML;
    screen.innerHTML = "";
}
function divide() {
    action.append("/");
    invisiText.innerHTML = screen.innerHTML;
    screen.innerHTML = "";
}
function times() {
    action.append("x");
    invisiText.innerHTML = screen.innerHTML;
    screen.innerHTML = "";
}
function percent() {
    answer.innerHTML = screen.innerHTML / 100;
    screen.innerHTML = "";
    action.innerHTML = "";
}
function cube() {
    answer.innerHTML = screen.innerHTML * screen.innerHTML * screen.innerHTML;
    screen.innerHTML = "";
    action.innerHTML = "";
}
function square() {
    answer.innerHTML = screen.innerHTML * screen.innerHTML;
    screen.innerHTML = "";
    action.innerHTML = "";
}
function root() {
    answer.innerHTML = Math.sqrt(screen.innerHTML);
    screen.innerHTML = "";
    action.innerHTML = "";
}
function cRoot() {
    answer.innerHTML = Math.cbrt(screen.innerHTML);
    screen.innerHTML = "";
    action.innerHTML = "";
}
function equal() {
    if (action.innerHTML === "+") {
        answer.innerHTML = (parseFloat(invisiText.innerHTML) + parseFloat(screen.innerHTML));
        screen.innerHTML = "";
        action.innerHTML = "";
    } else if (action.innerHTML === "-") {
        answer.innerHTML = (parseFloat(invisiText.innerHTML) - parseFloat(screen.innerHTML));
        screen.innerHTML = "";
        action.innerHTML = "";
    } else if (action.innerHTML === "/") {
        answer.innerHTML = parseFloat(invisiText.innerHTML) / parseFloat(screen.innerHTML);
        screen.innerHTML = "";
        action.innerHTML = "";
    } else if (action.innerHTML === "x") {
        answer.innerHTML = parseFloat(invisiText.innerHTML) * parseFloat(screen.innerHTML);
        screen.innerHTML = "";
        action.innerHTML = "";
    }
}
function cos() {
    var radianFormular = 0.01745329252;
    let answer2 = screen.innerHTML * radianFormular;
    answer.innerHTML = 1 - ((answer2 * answer2) / 2) + ((answer2 * answer2 * answer2 * answer2) / 24) - ((answer2 * answer2 * answer2 * answer2 * answer2 * answer2) / 720) + ((answer2 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2) / 40320) - ((answer2 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2) / 3628800) + ((answer2 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2) / 479001600);
    screen.innerHTML = "";
}
function sin() {
    var radianFormular = 0.01745329252;
    let answer1 = screen.innerHTML * radianFormular;
    answer.innerHTML = answer1 - ((answer1 * answer1 * answer1) / 6) + ((answer1 * answer1 * answer1 * answer1 * answer1) / 120) - ((answer1 * answer1 * answer1 * answer1 * answer1 * answer1 * answer1) / 5040) + ((answer1 * answer1 * answer1 * answer1 * answer1 * answer1 * answer1 * answer1 * answer1) / 362880) - ((answer1 * answer1 * answer1 * answer1 * answer1 * answer1 * answer1 * answer1 * answer1 * answer1 * answer1) / 39916800) + ((answer1 * answer1 * answer1 * answer1 * answer1 * answer1 * answer1 * answer1 * answer1 * answer1 * answer1 * answer1 * answer1) / 6227020800);
    screen.innerHTML = "";
}
function tan() {
    var radianFormular = 0.01745329252;
    let answer2 = screen.innerHTML * radianFormular;
    answer.innerHTML = answer2 + ((answer2 * answer2 * answer2) / 3) + ((2 * answer2 * answer2 * answer2 * answer2 * answer2) / 15) + ((17 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2) / 315) + ((62 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2) / 2835) + ((1382 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2) / 155925) + ((21844 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2) / 6081075) + ((929569 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2) / 22143325) + ((6404582 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2) / 87279625) + ((9132976 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2) / 235381435) + ((1065298864 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2) / 929354445) + ((672721170 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2) / 4043699775) + ((11321228864 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2 * answer2) / 19293714695);
    screen.innerHTML = "";
}
function log() {
    answer.innerHTML = Math.log10(screen.innerHTML)
    screen.innerHTML = "";
}
function anti() {
    answer.innerHTML = Math.pow(10, screen.innerHTML);
    screen.innerHTML = "";
}

