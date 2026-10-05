import java.io.*;
import java.util.*;

public class Solution {

    static int[] manacher(char[] s) {
        int n = s.length;
        int[] p = new int[n];

        int center = 0;
        int right = 0;

        for (int i = 0; i < n; i++) {
            int mirror = 2 * center - i;

            if (i < right) {
                p[i] = Math.min(right - i, p[mirror]);
            }

            while (i - p[i] - 1 >= 0 &&
                   i + p[i] + 1 < n &&
                   s[i - p[i] - 1] == s[i + p[i] + 1]) {
                p[i]++;
            }

            if (i + p[i] > right) {
                center = i;
                right = i + p[i];
            }
        }

        return p;
    }

    static class RMQ {
        int[][] table;
        int[] log;

        RMQ(int[] a) {
            int n = a.length;

            log = new int[n + 1];
            for (int i = 2; i <= n; i++) {
                log[i] = log[i / 2] + 1;
            }

            int k = log[n] + 1;
            table = new int[k][n];

            System.arraycopy(a, 0, table[0], 0, n);

            for (int j = 1; j < k; j++) {
                for (int i = 0; i + (1 << j) <= n; i++) {
                    table[j][i] = Math.max(
                        table[j - 1][i],
                        table[j - 1][i + (1 << (j - 1))]
                    );
                }
            }
        }

        int query(int l, int r) {
            if (l > r) {
                return 0;
            }

            int len = r - l + 1;
            int k = log[len];

            return Math.max(
                table[k][l],
                table[k][r - (1 << k) + 1]
            );
        }
    }

    public static List<Integer> circularPalindromes(String s) {
        int n = s.length();

        char[] doubled = new char[2 * n];

        for (int i = 0; i < 2 * n; i++) {
            doubled[i] = s.charAt(i % n);
        }

        char[] transformed = new char[4 * n + 1];

        for (int i = 0; i < transformed.length; i++) {
            if ((i & 1) == 0) {
                transformed[i] = '#';
            } else {
                transformed[i] = doubled[i / 2];
            }
        }

        int[] radius = manacher(transformed);
        RMQ rmq = new RMQ(radius);

        List<Integer> result = new ArrayList<>();

        for (int start = 0; start < n; start++) {
            int left = 2 * start + 1;
            int right = 2 * (start + n - 1) + 1;

            int low = 1;
            int high = n;
            int answer = 1;

            while (low <= high) {
                int mid = (low + high) / 2;

                int l = left + mid - 1;
                int r = right - mid + 1;

                if (l <= r && rmq.query(l, r) >= mid) {
                    answer = mid;
                    low = mid + 1;
                } else {
                    high = mid - 1;
                }
            }

            result.add(answer);
        }

        return result;
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(
            new InputStreamReader(System.in)
        );

        int n = Integer.parseInt(br.readLine().trim());
        String s = br.readLine().trim();

        List<Integer> result = circularPalindromes(s);

        StringBuilder out = new StringBuilder();

        for (int x : result) {
            out.append(x).append('\n');
        }

        System.out.print(out);
    }
}
