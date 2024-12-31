/*
* Process:
* Accept height and weight as input.
* Calculate BMI using a formula.
* Display the result and categorize (underweight, normal, overweight)
* 
ask if user prefers metric or imperial system
* metric:
*  get weight(kg) 
*  get height(m)
* imperial:
*  get weight(lbs)
*  get height(inches)
* Underweight: < 18.5
* Normal weight: 18.5 - 24.9
* Overweight: 25 - 29.9
* Obese: ≥ 30
*/
package com.main;

import java.util.InputMismatchException;
import java.util.Scanner;

public class App {

    private static final Scanner inputScanner = new Scanner(System.in);

    private static final String ERRORMSG = "Error: Must be a number (integer)\n";

    public static void main(String[] args) {
        App app = new App();

        System.out.println("Hi!, this is a Body Mass Index (BMI) Calculator");

        int systemType = app.getSystemType();

        if (systemType == 1) {
            int weight = app.getMetricSystemWeight();

            double height = app.getMetricSystemHeight();

            double bmi = app.metricBMICalculator(weight, height);

            System.out.println(app.getBMIResult(bmi));

        } else if (systemType == 2) {
            int weight = app.getImperialSystemWeight();

            int height = app.getImperialSystemHeight();

            double bmi = app.imperialBMICalculator(weight, height);

            System.out.println(app.getBMIResult(bmi));
        }
    }

    private int getSystemType() {
        while (true) {
            System.out.print("1. Metric \n2. Imperial system\nWhat do you prefer?: ");
            try {
                int systemType = inputScanner.nextInt();

                if (systemType == 1 || systemType == 2) {
                    return systemType;
                } else {
                    System.out.println("Please choose between 1 and 2\n");
                }

            } catch (InputMismatchException e) {
                System.out.println(ERRORMSG);
                // Clears invalid input
                inputScanner.nextLine();
            }
        }
    }

    private int getMetricSystemWeight() {
        while (true) {
            System.out.print("Please provide your weight in kilogram (kg): ");
            try {
                return inputScanner.nextInt();
            } catch (InputMismatchException e) {
                System.out.println(ERRORMSG);
                inputScanner.nextLine();
            }
        }
    }

    private double getMetricSystemHeight() {
        while (true) {
            System.out.print("Please provide your height in meters (m): ");
            try {
                return inputScanner.nextFloat();
            } catch (InputMismatchException e) {
                System.out.println(ERRORMSG);
                inputScanner.nextLine();
            }
        }

    }

    private int getImperialSystemWeight() {
        while (true) {
            System.out.print("Please provide your weight in pounds (lbs): ");
            try {
                return inputScanner.nextInt();
            } catch (InputMismatchException e) {
                System.out.println(ERRORMSG);
                inputScanner.nextLine();
            }
        }

    }

    private int getImperialSystemHeight() {
        while (true) {
            System.out.print("Please provide your height in inches (in): ");
            try {
                return inputScanner.nextInt();
            } catch (InputMismatchException e) {
                System.out.println(ERRORMSG);
                inputScanner.nextLine();
            }
        }

    }

    private double metricBMICalculator(int weight, double height) {
        return weight / Math.pow(height, 2);
    }

    private double imperialBMICalculator(int weight, int height) {
        return (weight * 703) / Math.pow(height, 2);
    }

    private String getBMIResult(double bmi) {
        String msg = "With a Body Mass Index of ";
        String result = "Placeholder text";

        if (bmi < 18.5) {
            result = msg + bmi
                    + " you are Underweight as classified by the (WHO) World Health Organization. Try eating some shit.";
        } else if (bmi >= 18.5 && bmi <= 24.9) {
            result = msg + bmi
                    + " you are at the Normal Weight as classified by the (WHO) World Health Organization. Good shit.";
        } else if (bmi >= 25 && bmi <= 29.9) {
            result = msg + bmi
                    + " you are Overweight as classified by the (WHO) World Health Organization. Maybe you should stop eating so much bro.";
        } else if (bmi >= 30) {
            result = msg + bmi
                    + " you are Obese as classified by the (WHO) World Health Organization. You're fat bro lmao. ";
        }
        return result;
    }
}
