import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // Day 5: Conditional Statements and Decision Making
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("=== Java Conditional Statements Demo ===");
        
        // Basic if-else
        System.out.print("Enter your age: ");
        int age = scanner.nextInt();
        
        if (age >= 18) {
            System.out.println("You are an adult!");
        } else {
            System.out.println("You are a minor.");
        }
        
        // if-else if-else ladder
        System.out.print("Enter your score (0-100): ");
        int score = scanner.nextInt();
        
        if (score >= 90) {
            System.out.println("Grade: A+ (Excellent!)");
        } else if (score >= 80) {
            System.out.println("Grade: A (Great!)");
        } else if (score >= 70) {
            System.out.println("Grade: B (Good!)");
        } else if (score >= 60) {
            System.out.println("Grade: C (Average)");
        } else {
            System.out.println("Grade: F (Need to study more!)");
        }
        
        // Ternary operator
        String result = (score >= 60) ? "Pass" : "Fail";
        System.out.println("Result: " + result);
        
        // Nested if statements
        System.out.print("Enter temperature in Celsius: ");
        double temperature = scanner.nextDouble();
        
        if (temperature > 0) {
            if (temperature > 30) {
                System.out.println("It's hot outside!");
            } else {
                System.out.println("It's warm outside.");
            }
        } else if (temperature == 0) {
            System.out.println("Water freezes at this temperature.");
        } else {
            System.out.println("It's cold outside!");
        }
        
        scanner.close();
    }
}