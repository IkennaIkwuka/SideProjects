package com.gui;

import java.awt.*;
import java.util.Random;
import javax.swing.*;

public class Main {

    // Main window for the game
    private JFrame frame;
    private JLabel messageLabel;
    private JLabel scoreLabel;

    // Game variables
    private int currentScore = 0; // Tracks the player's current score
    private int highScore = 0; // Tracks the highest score achieved
    private static final String ROCK = "Rock";
    private static final String PAPER = "Paper";
    private static final String SCISSORS = "Scissors";
    static final String[] OPTIONS = { ROCK, PAPER, SCISSORS };

    Random random = new Random();

    public static void main(String[] args) {
        new Main().setupGame(); // Start the game
    }

    // Initialize and set up the game GUI
    private void setupGame() {
        createFrame(); // Create the main window
        createLabels(); // Create message and score labels
        createButtons(); // Create choice and restart buttons
        frame.setVisible(true);
    }

    // Create the main game frame
    private void createFrame() {
        frame = new JFrame("Ikenna.N.Ikwuka CSC/2023/030 - Rock Paper Scissors - Java Swing Game");
        frame.setSize(400, 300);
        frame.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
        frame.setLayout(new BorderLayout());
    }

    // Create labels for messages and scores
    private void createLabels() {
        messageLabel = new JLabel("Choose Rock, Paper, or Scissors!", SwingConstants.CENTER);
        messageLabel.setFont(new Font("Arial", Font.BOLD, 14));

        scoreLabel = new JLabel("Score: 0 | High Score: 0", SwingConstants.CENTER);
        scoreLabel.setFont(new Font("Arial", Font.PLAIN, 12));

        frame.add(messageLabel, BorderLayout.NORTH);
        frame.add(scoreLabel, BorderLayout.SOUTH);
    }

    // Create buttons for user interaction
    private void createButtons() {
        JPanel buttonPanel = new JPanel(new GridLayout(1, 4));

        // Add buttons for Rock, Paper, and Scissors
        for (String option : OPTIONS) {
            JButton button = new JButton(option);
            button.addActionListener(e -> modifyGame(option));
            buttonPanel.add(button);
        }

        // Add a Restart button
        JButton resetButton = new JButton("Reset");
        resetButton.addActionListener(e -> resetGame());
        buttonPanel.add(resetButton);

        frame.add(buttonPanel, BorderLayout.CENTER);
    }

    // Handle game-play when the player chooses an option
    private void modifyGame(String playerChoice) {
        String computerChoice = OPTIONS[random.nextInt(OPTIONS.length)];
        String result;

        // Determine the game outcome
        if (playerChoice.equals(computerChoice)) {
            result = "It's a tie!";
        } else if ((playerChoice.equals(ROCK) && computerChoice.equals(SCISSORS)) ||
                (playerChoice.equals(PAPER) && computerChoice.equals(ROCK)) ||
                (playerChoice.equals(SCISSORS) && computerChoice.equals(PAPER))) {
            result = "You win!";
            currentScore++; // Increment the player's score
            highScore = Math.max(highScore, currentScore); // Update high score
        } else {
            result = "Computer wins!";
            currentScore = 0; // Reset current score on loss
        }

        // Update the message and score labels
        messageLabel.setText("Computer chose " + computerChoice + ". " + result);
        scoreLabel.setText("Score: " + currentScore + " | High Score: " + highScore);
    }

    // Reset the game state
    private void resetGame() {
        currentScore = 0; // Reset the score
        messageLabel.setText("Choose Rock, Paper, or Scissors!");
        scoreLabel.setText("Score: 0 | High Score: 0");
    }
}
