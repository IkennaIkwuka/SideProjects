let countdown;
let timerDisplay = document.getElementById('timerDisplay');

function startTimer() {
    let seconds = document.getElementById('seconds').value;

    if (seconds <= 0) {
        alert("Please enter a valid number of seconds.");
        return;
    }

    // Update the display to show the countdown
    let timeRemaining = seconds;

    countdown = setInterval(function () {
        let minutes = Math.floor(timeRemaining / 60);
        let secondsLeft = timeRemaining % 60;

        timerDisplay.textContent = `${padZero(minutes)}:${padZero(secondsLeft)}`;

        if (timeRemaining <= 0) {
            clearInterval(countdown);
            alert("Time's up!");
        }
        timeRemaining--;
    }, 1000);
}

function pauseTimer() {
    clearInterval(countdown);
    alert("Timer stopped.");
}

function padZero(number) {
    return number < 10 ? '0' + number : number;
}
