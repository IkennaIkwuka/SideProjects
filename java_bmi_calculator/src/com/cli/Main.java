package com.cli;

import java.util.InputMismatchException;
import java.util.Scanner;

/*
* Process:
 * Accept height and weight as input.
 * Calculate BMI using a formula.
 * Display the result and categorize (underweight, normal, overweight)
 *
 * ask if user prefers metric or imperial system
 * metric:
 * get weight(kg)
 * get height(m)
 * imperial:
 * get weight(lbs)
 * get height(inches)
 * Underweight: < 18.5
 * Normal weight: 18.5 - 24.9
 * Overweight: 25 - 29.9
 * Obese: ≥ 30
 */
public class Main {

    private static final Scanner userInput = new Scanner(System.in);

    public static void main(String[] args) {
        Main app = new Main();

        System.out.println("Hi!, this is a Body Mass Index (BMI) Calculator");

        int systemType = app.getSystemType();

        if (systemType == 1) {
            int weight = app.getUserInput("Please provide your weight in kilogram (kg): ");

            double height = app.getUserInput("Please provide your height in meters (m): ");

            double bmi = weight / Math.pow(height, 2);

            System.out.println(app.getBMIResult(bmi));

        } else if (systemType == 2) {
            int weight = app.getUserInput("Please provide your weight in pounds (lbs): ");

            int height = app.getUserInput("Please provide your height in inches (in): ");

            double bmi = (weight * 703) / Math.pow(height, 2);

            System.out.println(app.getBMIResult(bmi));
        }
    }

    private int getSystemType() {
        while (true) {
            System.out.print("1. Metric\t2. Imperial system\nWhat do you prefer?: ");
            try {
                int systemType = userInput.nextInt();
                if (systemType == 1 || systemType == 2) {
                    return systemType;
                }
                System.out.println("Please choose between 1 and 2");
            } catch (InputMismatchException e) {
                System.out.println("Error: Must be a number (integer)");
                userInput.next();
            }
        }
    }

    private int getUserInput(String prompt) {
        while (true) {
            System.out.print(prompt);
            try {
                return userInput.nextInt();
            } catch (InputMismatchException e) {
                System.out.println("Error: Must be a number (integer)");
                userInput.next();
            }
        }
    }

    private String getBMIResult(double bmi) {
        String msg = "With a Body Mass Index of ";
        String result = "\n";

        if (bmi < 18.5) {
            result = msg + String.format("%.2f", bmi)
                    + " you are Underweight as classified by the (WHO) World Health Organization. Try eating some shit.";
        } else if (bmi >= 18.5 && bmi <= 24.9) {
            result = msg + String.format("%.2f", bmi)
                    + " you are at the Normal Weight as classified by the (WHO) World Health Organization. Good shit.";
        } else if (bmi >= 25 && bmi <= 29.9) {
            result = msg + String.format("%.2f", bmi)
                    + " you are Overweight as classified by the (WHO) World Health Organization. Maybe you should stop eating so much bro.";
        } else if (bmi >= 30) {
            result = msg + String.format("%.2f", bmi)
                    + " you are Obese as classified by the (WHO) World Health Organization. You're fat bro lmao. ";
        }
        return result;
    }
}