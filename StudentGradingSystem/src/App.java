
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

public class App {
    public static void main(String[] args) {
        final String[] subjects = { "English", "Maths", "Computer Science", "Physics", "Chemistry" };

        ArrayList<Integer> scores = new ArrayList<>();

        try (Scanner scanner = new Scanner(System.in)) {

            for (String subject : subjects) {
                while (true) {
                    System.out.print("Provide the score for " + subject + ": ");
                    try {
                        int score = scanner.nextInt();
                        scores.add(score);
                        break;
                    } catch (InputMismatchException e) {
                        System.out.println("Please input a number");
                        scanner.next();
                    }
                }
            }
        }
        int sumOfScores = 0;

        for (int score : scores) {
            sumOfScores += score;
        }

        double scoreCount = scores.size();

        double average = sumOfScores / scoreCount;

        System.out.println("\nCompiling results...");
        for (int i = 0; i < subjects.length; i++) {
            String subject = subjects[i];
            int score = scores.get(i); // Match the score to the subject
            System.out.println("For " + subject + " you got " + score);
        }

        System.out.println("Meaning you had an average of " + average);

        if (average >= 100) {
            System.out.println("Wow!. perfect score");
        } else if (average >= 70 && average < 100) {
            System.out.println("Wow!. A very good score");
        } else if (average >= 50 && average < 70) {
            System.out.println("Meh! Pretty average I guess");
        } else if (average >= 30 && average < 50) {
            System.out.println("You almost made average, don't give up");
        } else if (average < 30) {
            System.out.println("Bruh!");
        }
    }
}
