/*
Process:
    Accept student scores and calculate averages.
    Assign grades based on predefined ranges.
 */
/*
 * get subjects amount;
 * loop to get scores for each subject
 * array to save scores
 * sum up scores 
 * get average of sum with subjects amount
 * display corresponding grade range based on average
 */
package com.java.main;

import java.util.InputMismatchException;
import java.util.Scanner;

public class App {
    private static final Scanner inputScanner = new Scanner(System.in);

    private static int final SCORES[] = [];

    public static void main(String[] args) {
        App app = new App();

    }

    private int getSubjectsAmount() {
        while (true) {
            System.out.print("How many subjects do you take this semester?: ");
            try {
                return inputScanner.nextInt();
            } catch (InputMismatchException e) {
                System.out.println("Error: Must be a number.");
                inputScanner.nextLine();
            }
        }
    }

    private void getStudentScore(int amount) {
        for (int i = 0; i < amount; i++) {
            while (true) { 
                try {
                    
                } catch (Exception e) {
                }
            }
        }
    }
}