import java.util.function.IntPredicate;

public class Main {
    public static void main(String[] args) {

        int num = 121;

        IntPredicate isPalindrome = n -> {
            int temp = n, rev = 0;

            while (temp > 0) {
                rev = rev * 10 + temp % 10;
                temp /= 10;
            }

            return rev == n;
        };

        if (isPalindrome.test(num))
            System.out.println("Palindrome");
        else
            System.out.println("Not Palindrome");
    }
}
