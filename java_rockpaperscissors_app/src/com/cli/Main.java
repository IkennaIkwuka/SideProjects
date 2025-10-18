package com.cli;

import java.util.InputMismatchException;
import java.util.Random;
import java.util.Scanner;

public class Main {

    private static final Scanner scanner = new Scanner(System.in);
    private static final String ROCK = "Rock";
    private static final String PAPER = "Paper";
    private static final String SCISSORS = "Scissors";
    private static final String[] OPTIONS = { ROCK, PAPER, SCISSORS };
    static int currentScore = 0;
    static int highScore = 0;

    public static void main(String[] args) {
        // Code Starts
        try (scanner) {
            Main app = new Main();
            Random random = new Random();

            boolean continueGameLoop;

            System.out.println("Hi, welcome to my Rock, Paper or Scissors Game");

            do {
                int userInput = app.getUserInput();

                // Handles and stores user Choices;
                String userChoice = OPTIONS[userInput];

                // Handles Computer choice;
                int computerInput = random.nextInt(1, OPTIONS.length);

                // Stores Computer choice;
                String computerChoice = OPTIONS[computerInput];

                // Determine result;
                String result = Main.getResult(userChoice, computerChoice);

                // Show Result;
                System.out.println(
                        "\nYou choose: " + userChoice + ", Computer choose: " + computerChoice + ". " + result);
                System.out.println("Score: " + currentScore + " | Current High Score: " + highScore);

                // Want to continue?;
                boolean game = app.getContinueGame();
                continueGameLoop = game;

            } while (continueGameLoop);

            System.out.println("\nThanks for playing my rock paper scissors game, Goodbye!");
        }
    }

    private boolean getContinueGame() {
        while (true) {
            System.out.print("\nDo you want to continue playing?(y / n): ");

            String continueGame = scanner.next().toLowerCase();

            if ("y".equals(continueGame)) {
                return true;
            } else if ("n".equals(continueGame)) {
                return false;
            }
            System.out.println("Please give a valid input");

        }
    }

    private int getUserInput() {
        while (true) {
            System.out.print("\nChoose '1' for Rock, '2' for Paper, '3' for Scissors: ");
            try {
                int userInput = scanner.nextInt();
                if (userInput >= 1 && userInput <= 3) {
                    return userInput - 1;
                }
                System.out.println("Please enter a valid number between 1 ~ 3 not " + userInput);
            } catch (InputMismatchException e) {
                System.out.println("Please enter a valid number.");
                scanner.next();
            }

        }
    }

    private static String getResult(String userChoice, String computerChoice) {
        String result;
        if (userChoice.equals(computerChoice)) {
            result = "It's a tie!"; // Both chose the same option
        } else if ((userChoice.equals(ROCK) && computerChoice.equals(SCISSORS))
                || (userChoice.equals(PAPER) && computerChoice.equals(ROCK))
                || (userChoice.equals(SCISSORS) && computerChoice.equals(PAPER))) {
            result = "Congratulations!, You win!";
            currentScore++;
            highScore = Math.max(currentScore, highScore); // Update high score
        } else {
            result = "Computer wins!";
            currentScore = 0; // Reset player's score to zero on loss
        }
        return result;
    }
}