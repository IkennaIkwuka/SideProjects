// Get references to the display and answer elements
let screen = document.getElementById('screen');
let answer = document.getElementById('answer');

// Insert values (numbers and operators) to the screen
function insert(value) {
    screen.innerHTML += value;
}

// Clear the screen and answer
function clearScreen() {
    screen.innerHTML = '';
    answer.innerHTML = '';
}

// Calculate the percentage
function percent() {
    let result = eval(screen.innerHTML) / 100;
    answer.innerHTML = result;
}

// Evaluate the current expression on the screen
function calculate() {
    try {
        let result = eval(screen.innerHTML);
        answer.innerHTML = result;
    } catch (e) {
        answer.innerHTML = "Error";
    }
}

// Trigonometric functions (input is assumed to be in degrees)
function sin() {
    let result = Math.sin(eval(screen.innerHTML) * Math.PI / 180);
    answer.innerHTML = result;
}

function cos() {
    let result = Math.cos(eval(screen.innerHTML) * Math.PI / 180);
    answer.innerHTML = result;
}

function tan() {
    let result = Math.tan(eval(screen.innerHTML) * Math.PI / 180);
    answer.innerHTML = result;
}
