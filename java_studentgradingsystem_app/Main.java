package com.cli;

import java.util.ArrayList;
import java.util.InputMismatchException;
import java.util.Scanner;

// Process:
//     Accept student scores and calculate averages.
//     Assign grades based on predefined ranges.

//   loop to get scores for each subject
//  * array to save scores
//  * sum up scores
//  * get average of sum with subjects amount
//  * display corresponding grade range based on average

public class Main {
    private static final Scanner scanner = new Scanner(System.in);
    private static final String[] subjects = { "English", "Maths", "Computer Science", "Physics", "Chemistry" };

    public static void main(String[] args) {
        try (scanner) {
            ArrayList<Integer> scores = new ArrayList<>();
            Main app = new Main();

            for (String subject : subjects) {
                int score = app.getUserScores(subject);
                scores.add(score);
            }

            int sumOfScores = 0;

            for (int score : scores) {
                sumOfScores += score;
            }

            int scoreCount = scores.size();

            double average = (double) sumOfScores / scoreCount;

            System.out.println("\nCompiling results...");
            for (int i = 0; i < subjects.length; i++) {
                String subject = subjects[i];
                int score = scores.get(i); // Match the score to the subject
                System.out.println("For " + subject + " you got " + score);
            }

            System.out.println("\nMeaning you had an average of " + average);

            if (average >= 100) {
                System.out.println("Wow!. perfect score");
            } else if (average >= 70) {
                System.out.println("Wow!. A very good score");
            } else if (average >= 50) {
                System.out.println("Meh! Pretty average I guess");
            } else if (average >= 30) {
                System.out.println("You almost made average, don't give up");
            } else {
                System.out.println("Bruh!");
            }
        }
    }

    private int getUserScores(String subject) {
        while (true) {
            System.out.print("Provide the score for " + subject + ": ");
            try {
                int score = scanner.nextInt();
                if (score >= 0 && score <= 100) {
                    return score;
                }
                System.out.println("Please input a valid number between 0 ~ 100 not " + score);

            } catch (InputMismatchException e) {
                System.out.println("Please input a valid whole number");
                scanner.next();
            }
        }
    }
}
