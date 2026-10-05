import java.util.*;

public class Main {
    public static void main(String[] args) { 
        Scanner sc = new Scanner(System.in); 
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt(); 
        int[] a = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = sc.nextInt();
        }
        int k = sc.nextInt();
        long sum = 0, max = Long.MIN_VALUE; 
        for (int i = 0; i < k; i++) sum += a[i];
        max = sum;
        for (int i = k; i < n; i++) { 
            sum += a[i] - a[i-k]; 
            max = Math.max(max, sum);
        }
        System.out.println(max);
    }
}
