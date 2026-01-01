package com.cli;

import java.util.InputMismatchException;
import java.util.Scanner;

public class Main {
    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        try (scanner) {
            int principal = getUserInput("Enter Principal: "); // Principal

            // Monthly interest rate
            double interest = getUserInput("Enter your Monthly interest rate: ");
            interest = (interest / 100) / 12;

            // Number of Payment
            double numberOfPayment = getUserInput("Enter the number of years you will be paying the loan: ");
            numberOfPayment = numberOfPayment * 12;

            double numerator = interest * (Math.pow((1 + interest), numberOfPayment));
            double denominator = Math.pow((1 + interest), numberOfPayment) - 1;

            // Mortgage Payment
            double mortgage = principal * (numerator / denominator);

            // Principal
            System.out.printf("Monthly payment: $%.2f", mortgage);
        }
    }

    public static int getUserInput(String prompt) {
        while (true) {
            try {
                System.out.print(prompt);
                return scanner.nextInt();
            } catch (InputMismatchException e) {
                System.out.println("Please input a valid number");
                scanner.next();
            }
        }
    }
}