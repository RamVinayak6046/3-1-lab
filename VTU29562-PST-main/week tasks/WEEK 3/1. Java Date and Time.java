import java.time.LocalDate;
import java.time.format.TextStyle;
import java.util.Locale;
import java.util.Scanner;

public class Solution {
    public static String findDay(int month, int day, int year) {
        return LocalDate.of(year, month, day)
                .getDayOfWeek()
                .getDisplayName(TextStyle.FULL, Locale.ENGLISH)
                .toUpperCase();
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int month = sc.nextInt();
        int day = sc.nextInt();
        int year = sc.nextInt();

        System.out.println(findDay(month, day, year));
    }
}

