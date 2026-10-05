import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

interface PerformOperation {
    boolean check(int a);
}

class MyMath {

    public PerformOperation isOdd() {
        return new PerformOperation() {
            public boolean check(int n) {
                return n % 2 != 0;
            }
        };
    }

    public PerformOperation isPrime() {
        return new PerformOperation() {
            public boolean check(int n) {
                if (n < 2)
                    return false;

                for (int i = 2; i * i <= n; i++) {
                    if (n % i == 0)
                        return false;
                }

                return true;
            }
        };
    }

    public PerformOperation isPalindrome() {
        return new PerformOperation() {
            public boolean check(int n) {
                int original = n;
                int reverse = 0;

                while (n > 0) {
                    reverse = reverse * 10 + n % 10;
                    n /= 10;
                }

                return original == reverse;
            }
        };
    }

    public boolean checker(PerformOperation p, int num) {
        return p.check(num);
    }
}

public class Solution {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        MyMath ob = new MyMath();

        int T = sc.nextInt();

        while (T-- > 0) {
            int ch = sc.nextInt();
            int num = sc.nextInt();

            if (ch == 1) {
                System.out.println(ob.checker(ob.isOdd(), num) ? "ODD" : "EVEN");
            } else if (ch == 2) {
                System.out.println(ob.checker(ob.isPrime(), num) ? "PRIME" : "COMPOSITE");
            } else if (ch == 3) {
                System.out.println(ob.checker(ob.isPalindrome(), num) ? "PALINDROME" : "NOT PALINDROME");
            }
        }

        sc.close();
    }
}
