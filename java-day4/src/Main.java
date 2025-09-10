public class Main {
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
        System.out.println("\n=== Type Casting Examples ===");
        int intValue = 100;
        double doubleValue = intValue; // Implicit casting
        System.out.println("Implicit casting (int to double): " + doubleValue);
        
        double largeDouble = 99.99;
        int truncatedInt = (int) largeDouble; // Explicit casting
        System.out.println("Explicit casting (double to int): " + truncatedInt);
    }
}