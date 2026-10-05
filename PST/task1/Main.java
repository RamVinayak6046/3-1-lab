import java.util.*;
import java.util.stream.Collectors;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        List<Long> salaries = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            salaries.add(sc.nextLong());
        }

        List<Long> updatedSalaries = salaries.stream()
                .map(salary -> Math.round(salary * 1.10))
                .collect(Collectors.toList());

        // Print updated salaries
        for (int i = 0; i < updatedSalaries.size(); i++) {
            if (i > 0) System.out.print(" ");
            System.out.print(updatedSalaries.get(i));
        }
        System.out.println();
    }
}
