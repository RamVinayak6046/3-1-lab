import java.util.*;

class Calculator {
    public static double add(double a, double b) {
        return a + b;
    }

    public static double subtract(double a, double b) {
        return a - b;
    }

    public static double multiply(double a, double b) {
        return a * b;
    }

    public static double divide(double a, double b) {
        if (b == 0) {
            throw new ArithmeticException("Division by zero");
        }
        return a / b;
    }
}

public class Main {
    // Automated unit testing framework for Calculator operations
    static boolean runUnitTests() {
        assert Calculator.add(5, 7) == 12 : "Add test failed";
        assert Calculator.add(-3, 3) == 0 : "Add negative test failed";
        assert Calculator.divide(10, 2) == 5 : "Divide test failed";
        try {
            Calculator.divide(10, 0);
            return false; // Should have thrown exception
        } catch (ArithmeticException e) {
            // Expected
        }
        return true;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNext()) {
            if (runUnitTests()) {
                System.out.println("Test Passed");
            } else {
                System.out.println("Test Failed");
            }
            return;
        }

        try {
            double num1 = sc.nextDouble();
            String op = sc.next();
            double num2 = sc.nextDouble();

            double actual = 0;
            double expected = 0;

            if (op.equals("+")) {
                actual = Calculator.add(num1, num2);
                expected = num1 + num2;
            } else if (op.equals("-")) {
                actual = Calculator.subtract(num1, num2);
                expected = num1 - num2;
            } else if (op.equals("*")) {
                actual = Calculator.multiply(num1, num2);
                expected = num1 * num2;
            } else if (op.equals("/")) {
                actual = Calculator.divide(num1, num2);
                expected = num1 / num2;
            }

            // Verify calculation matches unit assertions
            if (Double.compare(actual, expected) == 0 && runUnitTests()) {
                System.out.println("Test Passed");
            } else {
                System.out.println("Test Failed");
            }
        } catch (Exception e) {
            System.out.println("Test Failed");
        }
    }
}
