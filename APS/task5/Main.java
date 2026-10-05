import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in); 
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt(); 
        int[] a = new int[n], ans = new int[n]; 
        for (int i = 0; i < n; i++) a[i] = sc.nextInt(); 
        Arrays.fill(ans, -1);
        Deque<Integer> st = new ArrayDeque<>(); 
        for (int i = 0; i < n; i++) {
            while (!st.isEmpty() && a[i] > a[st.peek()]) ans[st.pop()] = a[i]; 
            st.push(i);
        }
        for (int i = 0; i < n; i++) { 
            if (i > 0) System.out.print(" "); 
            System.out.print(ans[i]); 
        } 
        System.out.println();
    }
}
