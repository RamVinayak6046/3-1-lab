import java.io.*;
import java.util.*;
public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        Set<String> set = new HashSet<>();
        for (int i = 0; i < T; i++) {
            String first = sc.next();
            String second = sc.next();
            String pair = first + " " + second;
            set.add(pair);
            System.out.println(set.size());
        }
        sc.close();
    }
}
