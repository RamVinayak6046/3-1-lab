import java.util.*;

public class Main {
    public static void main(String[] args) { 
        Scanner sc = new Scanner(System.in); 
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        Map<Integer,Integer> freq = new HashMap<>();
        for (int i = 0; i < n; i++) { 
            int x = sc.nextInt(); 
            freq.put(x, freq.getOrDefault(x, 0) + 1); 
        } 
        int bestId = Integer.MAX_VALUE, bestFreq = -1;
        for (Map.Entry<Integer,Integer> e : freq.entrySet()) {
            if (e.getValue() > bestFreq || (e.getValue() == bestFreq && e.getKey() < bestId)) { 
                bestFreq = e.getValue(); 
                bestId = e.getKey();
            }
        }
        System.out.println(bestId + " " + bestFreq);
    }
}
