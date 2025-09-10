#!/usr/bin/env python3
"""
Daily Java Streak Automation Script

This script helps maintain a daily coding streak by:
1. Automatically determining the next day number
2. Generating educational Java programs for DSA learning
3. Creating proper folder structure
4. Committing and pushing changes to GitHub

Usage: python daily_streak.py
"""

import os
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path

class DailyJavaStreak:
    def __init__(self):
        self.repo_path = Path(__file__).parent
        self.day_number = self._get_next_day_number()
        
    def _get_next_day_number(self):
        """Find the highest existing day number and return the next one."""
        max_day = 0
        
        # Check for existing day folders and files
        for item in self.repo_path.iterdir():
            if item.name.startswith('java-day'):
                # Extract day number from folder/file name
                match = re.search(r'java-day(\d+)', item.name)
                if match:
                    day_num = int(match.group(1))
                    max_day = max(max_day, day_num)
        
        return max_day + 1
    
    def _get_java_program_content(self, day):
        """Generate Java program content based on day number and DSA topics."""
        programs = {
            4: {
                "topic": "Variables and Data Types",
                "content": '''public class Main {
    public static void main(String[] args) {
        // Day 4: Understanding Variables and Data Types in Java
        
        // Integer types
        byte smallNumber = 127;
        short mediumNumber = 32000;
        int regularNumber = 2147483647;
        long bigNumber = 9223372036854775807L;
        
        // Floating point types
        float floatNumber = 3.14f;
        double doubleNumber = 3.14159265359;
        
        // Character and Boolean
        char character = 'A';
        boolean isJavaFun = true;
        
        // String (reference type)
        String message = "Hello, Java Day 4!";
        
        // Display all variables
        System.out.println("=== Java Data Types Demo ===");
        System.out.println("Byte: " + smallNumber);
        System.out.println("Short: " + mediumNumber);
        System.out.println("Int: " + regularNumber);
        System.out.println("Long: " + bigNumber);
        System.out.println("Float: " + floatNumber);
        System.out.println("Double: " + doubleNumber);
        System.out.println("Char: " + character);
        System.out.println("Boolean: " + isJavaFun);
        System.out.println("String: " + message);
        
        // Type casting examples
        System.out.println("\\n=== Type Casting Examples ===");
        int intValue = 100;
        double doubleValue = intValue; // Implicit casting
        System.out.println("Implicit casting (int to double): " + doubleValue);
        
        double largeDouble = 99.99;
        int truncatedInt = (int) largeDouble; // Explicit casting
        System.out.println("Explicit casting (double to int): " + truncatedInt);
    }
}'''
            },
            5: {
                "topic": "Conditional Statements (if-else)",
                "content": '''import java.util.Scanner;

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
}'''
            },
            6: {
                "topic": "Loops (for, while, do-while)",
                "content": '''import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // Day 6: Loops in Java - for, while, and do-while
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("=== Java Loops Demo ===");
        
        // For loop example - Print numbers 1 to 10
        System.out.println("\\n1. For Loop - Numbers 1 to 10:");
        for (int i = 1; i <= 10; i++) {
            System.out.print(i + " ");
        }
        System.out.println();
        
        // For loop - Multiplication table
        System.out.print("\\nEnter a number for multiplication table: ");
        int number = scanner.nextInt();
        System.out.println("Multiplication table of " + number + ":");
        for (int i = 1; i <= 10; i++) {
            System.out.println(number + " x " + i + " = " + (number * i));
        }
        
        // While loop example - Sum of natural numbers
        System.out.print("\\nEnter a number to find sum of natural numbers: ");
        int n = scanner.nextInt();
        int sum = 0;
        int i = 1;
        
        while (i <= n) {
            sum += i;
            i++;
        }
        System.out.println("Sum of first " + n + " natural numbers: " + sum);
        
        // Do-while loop example - Menu driven program
        int choice;
        do {
            System.out.println("\\n=== Simple Calculator ===");
            System.out.println("1. Add");
            System.out.println("2. Subtract");
            System.out.println("3. Multiply");
            System.out.println("4. Divide");
            System.out.println("5. Exit");
            System.out.print("Enter your choice: ");
            choice = scanner.nextInt();
            
            if (choice >= 1 && choice <= 4) {
                System.out.print("Enter first number: ");
                double num1 = scanner.nextDouble();
                System.out.print("Enter second number: ");
                double num2 = scanner.nextDouble();
                
                switch (choice) {
                    case 1:
                        System.out.println("Result: " + (num1 + num2));
                        break;
                    case 2:
                        System.out.println("Result: " + (num1 - num2));
                        break;
                    case 3:
                        System.out.println("Result: " + (num1 * num2));
                        break;
                    case 4:
                        if (num2 != 0) {
                            System.out.println("Result: " + (num1 / num2));
                        } else {
                            System.out.println("Error: Division by zero!");
                        }
                        break;
                }
            } else if (choice != 5) {
                System.out.println("Invalid choice! Please try again.");
            }
            
        } while (choice != 5);
        
        System.out.println("Thank you for using the calculator!");
        scanner.close();
    }
}'''
            },
            7: {
                "topic": "Arrays - Introduction",
                "content": '''import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // Day 7: Arrays in Java - Introduction and Basic Operations
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("=== Java Arrays Demo ===");
        
        // 1. Array Declaration and Initialization
        System.out.println("\\n1. Array Declaration and Initialization:");
        
        // Different ways to declare arrays
        int[] numbers1 = new int[5]; // Array of size 5, initialized with 0s
        int[] numbers2 = {1, 2, 3, 4, 5}; // Array literal
        int[] numbers3 = new int[]{10, 20, 30, 40, 50}; // Another way
        
        System.out.println("numbers1 (default values): " + Arrays.toString(numbers1));
        System.out.println("numbers2 (initialized): " + Arrays.toString(numbers2));
        System.out.println("numbers3 (initialized): " + Arrays.toString(numbers3));
        
        // 2. Taking array input from user
        System.out.print("\\nEnter the size of array: ");
        int size = scanner.nextInt();
        int[] userArray = new int[size];
        
        System.out.println("Enter " + size + " integers:");
        for (int i = 0; i < size; i++) {
            userArray[i] = scanner.nextInt();
        }
        
        // 3. Display array elements
        System.out.println("\\nYour array: " + Arrays.toString(userArray));
        
        // 4. Basic array operations
        System.out.println("\\n=== Array Operations ===");
        
        // Find sum and average
        int sum = 0;
        for (int num : userArray) {
            sum += num;
        }
        double average = (double) sum / userArray.length;
        
        System.out.println("Sum of elements: " + sum);
        System.out.println("Average: " + average);
        
        // Find maximum and minimum
        int max = userArray[0];
        int min = userArray[0];
        
        for (int i = 1; i < userArray.length; i++) {
            if (userArray[i] > max) {
                max = userArray[i];
            }
            if (userArray[i] < min) {
                min = userArray[i];
            }
        }
        
        System.out.println("Maximum element: " + max);
        System.out.println("Minimum element: " + min);
        
        // 5. Search for an element
        System.out.print("\\nEnter a number to search: ");
        int searchNum = scanner.nextInt();
        boolean found = false;
        int position = -1;
        
        for (int i = 0; i < userArray.length; i++) {
            if (userArray[i] == searchNum) {
                found = true;
                position = i;
                break;
            }
        }
        
        if (found) {
            System.out.println(searchNum + " found at index " + position);
        } else {
            System.out.println(searchNum + " not found in the array");
        }
        
        // 6. Reverse the array
        System.out.println("\\nOriginal array: " + Arrays.toString(userArray));
        
        // Reverse array elements
        for (int i = 0; i < userArray.length / 2; i++) {
            int temp = userArray[i];
            userArray[i] = userArray[userArray.length - 1 - i];
            userArray[userArray.length - 1 - i] = temp;
        }
        
        System.out.println("Reversed array: " + Arrays.toString(userArray));
        
        scanner.close();
    }
}'''
            },
            8: {
                "topic": "Methods and Functions",
                "content": '''import java.util.Scanner;

public class Main {
    
    // Day 8: Methods and Functions in Java
    
    // Method to add two numbers
    public static int add(int a, int b) {
        return a + b;
    }
    
    // Method to find factorial (recursive)
    public static long factorial(int n) {
        if (n <= 1) {
            return 1;
        }
        return n * factorial(n - 1);
    }
    
    // Method to check if a number is prime
    public static boolean isPrime(int n) {
        if (n <= 1) {
            return false;
        }
        if (n <= 3) {
            return true;
        }
        if (n % 2 == 0 || n % 3 == 0) {
            return false;
        }
        
        for (int i = 5; i * i <= n; i += 6) {
            if (n % i == 0 || n % (i + 2) == 0) {
                return false;
            }
        }
        return true;
    }
    
    // Method to find maximum of three numbers
    public static int findMax(int a, int b, int c) {
        return Math.max(Math.max(a, b), c);
    }
    
    // Method to print array elements
    public static void printArray(int[] arr) {
        System.out.print("[");
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i]);
            if (i < arr.length - 1) {
                System.out.print(", ");
            }
        }
        System.out.println("]");
    }
    
    // Method to calculate power (iterative)
    public static double power(double base, int exponent) {
        double result = 1;
        for (int i = 0; i < Math.abs(exponent); i++) {
            result *= base;
        }
        return exponent < 0 ? 1.0 / result : result;
    }
    
    // Method to reverse a string
    public static String reverseString(String str) {
        StringBuilder reversed = new StringBuilder();
        for (int i = str.length() - 1; i >= 0; i--) {
            reversed.append(str.charAt(i));
        }
        return reversed.toString();
    }
    
    // Method with variable arguments (varargs)
    public static double average(double... numbers) {
        if (numbers.length == 0) {
            return 0;
        }
        
        double sum = 0;
        for (double num : numbers) {
            sum += num;
        }
        return sum / numbers.length;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("=== Java Methods and Functions Demo ===");
        
        // 1. Basic method usage
        System.out.println("\\n1. Basic Method Usage:");
        int num1 = 15, num2 = 25;
        System.out.println(num1 + " + " + num2 + " = " + add(num1, num2));
        
        // 2. Recursive method
        System.out.print("\\nEnter a number to find factorial: ");
        int n = scanner.nextInt();
        System.out.println("Factorial of " + n + " = " + factorial(n));
        
        // 3. Boolean returning method
        System.out.print("\\nEnter a number to check if prime: ");
        int primeCheck = scanner.nextInt();
        if (isPrime(primeCheck)) {
            System.out.println(primeCheck + " is a prime number");
        } else {
            System.out.println(primeCheck + " is not a prime number");
        }
        
        // 4. Method with multiple parameters
        System.out.println("\\nEnter three numbers to find maximum:");
        System.out.print("First number: ");
        int a = scanner.nextInt();
        System.out.print("Second number: ");
        int b = scanner.nextInt();
        System.out.print("Third number: ");
        int c = scanner.nextInt();
        System.out.println("Maximum of " + a + ", " + b + ", " + c + " is: " + findMax(a, b, c));
        
        // 5. Method that works with arrays
        int[] testArray = {10, 20, 30, 40, 50};
        System.out.println("\\nArray elements: ");
        printArray(testArray);
        
        // 6. Method with mathematical operations
        System.out.print("\\nEnter base for power calculation: ");
        double base = scanner.nextDouble();
        System.out.print("Enter exponent: ");
        int exp = scanner.nextInt();
        System.out.println(base + "^" + exp + " = " + power(base, exp));
        
        // 7. String manipulation method
        scanner.nextLine(); // consume newline
        System.out.print("\\nEnter a string to reverse: ");
        String inputString = scanner.nextLine();
        System.out.println("Reversed string: " + reverseString(inputString));
        
        // 8. Variable arguments method
        System.out.println("\\nAverage of 10, 20, 30: " + average(10, 20, 30));
        System.out.println("Average of 5, 15, 25, 35, 45: " + average(5, 15, 25, 35, 45));
        
        scanner.close();
    }
}'''
            }
        }
        
        # Default program for days not specifically defined
        default_program = {
            "topic": f"DSA Concept - Day {day}",
            "content": f'''public class Main {{
    public static void main(String[] args) {{
        // Day {day}: Exploring Java Programming and DSA Concepts
        
        System.out.println("=== Java Day {day} ===");
        System.out.println("Welcome to Day {day} of Java programming!");
        System.out.println("Today we continue our journey in Data Structures and Algorithms.");
        
        // Add your code here to practice new concepts
        // This is a template for Day {day}
        
        System.out.println("Keep coding and building your GitHub streak! 🚀");
    }}
}}'''
        }
        
        return programs.get(day, default_program)
    
    def create_daily_program(self):
        """Create a new daily Java program."""
        program_info = self._get_java_program_content(self.day_number)
        folder_name = f"java-day{self.day_number}"
        folder_path = self.repo_path / folder_name
        src_path = folder_path / "src"
        
        # Create directory structure
        src_path.mkdir(parents=True, exist_ok=True)
        
        # Create Main.java file
        main_java_path = src_path / "Main.java"
        main_java_path.write_text(program_info["content"])
        
        # Create README.md for the day
        readme_content = f"""# Java Day {self.day_number}

## Topic: {program_info["topic"]}

This folder contains Java code for Day {self.day_number} of the daily coding streak, focusing on {program_info["topic"]}.

## Structure
- `src/Main.java` — Main Java file with examples and exercises

## How to Run
1. Navigate to the src directory:
   ```bash
   cd {folder_name}/src
   ```
2. Compile the Java file:
   ```bash
   javac Main.java
   ```
3. Run the program:
   ```bash
   java Main
   ```

## Learning Objectives
- Understanding {program_info["topic"]}
- Practical implementation in Java
- Building problem-solving skills

## Requirements
- Java JDK 8 or higher

## About This Series
This is part of a daily coding streak to improve Java programming and DSA skills. Each day introduces new concepts and provides hands-on practice.

---
*Day {self.day_number} completed on {datetime.now().strftime('%Y-%m-%d')}*
"""
        
        readme_path = folder_path / "README.md"
        readme_path.write_text(readme_content)
        
        return folder_name, program_info["topic"]
    
    def test_compilation(self, folder_name):
        """Test if the created Java program compiles successfully."""
        src_path = self.repo_path / folder_name / "src"
        try:
            result = subprocess.run(
                ["javac", "Main.java"],
                cwd=src_path,
                capture_output=True,
                text=True
            )
            return result.returncode == 0, result.stderr
        except Exception as e:
            return False, str(e)
    
    def commit_and_push(self, folder_name, topic):
        """Commit and push the new daily program."""
        try:
            # Add files to git
            subprocess.run(["git", "add", folder_name], cwd=self.repo_path, check=True)
            
            # Commit with meaningful message
            commit_message = f"Add Day {self.day_number}: {topic}"
            subprocess.run(
                ["git", "commit", "-m", commit_message],
                cwd=self.repo_path,
                check=True
            )
            
            print(f"✅ Committed: {commit_message}")
            return True
            
        except subprocess.CalledProcessError as e:
            print(f"❌ Error during git operations: {e}")
            return False
    
    def run_daily_streak(self):
        """Main method to run the daily streak automation."""
        print(f"🚀 Starting Daily Java Streak - Day {self.day_number}")
        
        # Create the daily program
        folder_name, topic = self.create_daily_program()
        print(f"📁 Created folder: {folder_name}")
        print(f"📚 Topic: {topic}")
        
        # Test compilation
        compiles, error_msg = self.test_compilation(folder_name)
        if compiles:
            print("✅ Java program compiles successfully!")
        else:
            print(f"❌ Compilation error: {error_msg}")
            return False
        
        # Commit changes
        if self.commit_and_push(folder_name, topic):
            print(f"🎉 Day {self.day_number} completed successfully!")
            print(f"📈 GitHub streak continues! Keep it up!")
            return True
        else:
            return False

def main():
    """Main function to run when script is called."""
    if len(sys.argv) > 1 and sys.argv[1] == "help":
        print("""
Daily Java Streak Automation

Usage:
  python daily_streak.py        - Create and commit today's Java program
  python daily_streak.py help   - Show this help message

This script automatically:
1. Determines the next day number
2. Creates a new Java program with educational content
3. Sets up proper folder structure
4. Tests compilation
5. Commits changes to git

The programs follow a DSA learning path with progressively complex topics.
        """)
        return
    
    streak = DailyJavaStreak()
    success = streak.run_daily_streak()
    
    if success:
        print("\\n" + "="*50)
        print("Daily streak completed! 🌟")
        print("Remember to push to GitHub with: git push origin main")
        print("="*50)
        sys.exit(0)
    else:
        print("\\n" + "="*50)
        print("Failed to complete daily streak. ❌")
        print("Please check the errors above and try again.")
        print("="*50)
        sys.exit(1)

if __name__ == "__main__":
    main()