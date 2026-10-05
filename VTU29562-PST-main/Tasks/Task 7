import java.util.function.IntUnaryOperator;

public class Main {
    public static void main(String[] args) {

        int n = 7;

        IntUnaryOperator fib = num -> {
            if (num == 0) return 0;
            if (num == 1) return 1;

            int a = 0, b = 1, c = 0;
            for (int i = 2; i <= num; i++) {
                c = a + b;
                a = b;
                b = c;
            }
            return c;
        };

        System.out.println("Nth Fibonacci = " + fib.applyAsInt(n));
    }
}
