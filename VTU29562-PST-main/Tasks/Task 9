import java.util.function.BinaryOperator;

public class Main {

    static int sumLastDigits(int a, int b) {
        return (a % 10) + (b % 10);
    }

    public static void main(String[] args) {

        int num1 = 123;
        int num2 = 456;

        BinaryOperator<Integer> obj = Main::sumLastDigits;

        System.out.println("Sum = " + obj.apply(num1, num2));
    }
}
