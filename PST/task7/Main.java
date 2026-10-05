import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();

        // LinkedHashMap preserves first insertion order
        Map<String, Integer> freqMap = new LinkedHashMap<>();

        for (int i = 0; i < n; i++) {
            String tag = sc.next();
            freqMap.put(tag, freqMap.getOrDefault(tag, 0) + 1);
        }

        for (Map.Entry<String, Integer> entry : freqMap.entrySet()) {
            System.out.println(entry.getKey() + " " + entry.getValue());
        }
    }
}
