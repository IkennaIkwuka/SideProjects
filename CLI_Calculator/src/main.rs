#![allow(unused)]
/*
process:
get what operation that the user wants to do
functions for said operations
*/

use std::{io, process::id};

fn main() {
    println!("Hi!, this is a Command-Line Calculator\n");
    println!("Here are arithmetic operations you can do:");
    println!("1. Addition");
    println!("2. Subtraction");
    println!("3. Division");
    println!("4. Multiplication");

    loop {
        println!("Choose an operation (x to quit)");

        let mut user_input = String::new();
        io::stdin()
            .read_line(&mut user_input)
            .expect("Failed to read line");
        let user_input = user_input.trim();

        if user_input.to_lowercase() == "x" {
            println!("Quitting...");
            break;
        }
        loop {
            println!("Provide the first value: ");
            let mut value = String::new();
            io::stdin()
                .read_line(&mut value)
                .expect("Failed to read line");

            let value1: i32 = value.trim().parse().;
            match value1 {
                
            }
        }

        match user_input.trim().to_lowercase().as_str() {
            "1" => print!(""),
            _ => println!("Not"),
        }
    }

    //     let mut user_input =
}
