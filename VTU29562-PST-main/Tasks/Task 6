import java.util.function.IntPredicate;

public class DigitSumOpt {
    public static int digitSum(int number, IntPredicate condition) {
        return String.valueOf(number)
                     .chars()
                     .map(Character::getNumericValue)
                     .filter(condition)
                     .sum();
    }

    public static void main(String[] args) {
        int num = 123456;
        int evenSum = digitSum(num, d -> d % 2 == 0);
        int oddSum = digitSum(num, d -> d % 2 != 0);

        System.out.println("Sum of even digits: " + evenSum);
        System.out.println("Sum of odd digits: " + oddSum);
    }
}
