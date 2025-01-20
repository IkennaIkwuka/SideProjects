
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
        try (Scanner scanner = new Scanner(System.in)) {
            ArrayList<Integer> scores = new ArrayList<>();

            String[] subjects = { "English", "Maths", "Computer Science", "Physics", "Chemistry" };

            for (Object subject : subjects) {
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
            System.out.println("Scores list: " + scores);
        }

    }
}
