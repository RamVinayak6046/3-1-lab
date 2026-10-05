import java.util.*;

public class Main {
    // Compute Longest Proper Prefix which is also Suffix (LPS) array for KMP
    static int[] computeLPSArray(String pattern) {
        int m = pattern.length();
        int[] lps = new int[m];
        int len = 0;
        int i = 1;
        lps[0] = 0;

        while (i < m) {
            if (pattern.charAt(i) == pattern.charAt(len)) {
                len++;
                lps[i] = len;
                i++;
            } else {
                if (len != 0) {
                    len = lps[len - 1];
                } else {
                    lps[i] = 0;
                    i++;
                }
            }
        }
        return lps;
    }

    // KMP Search Algorithm
    static List<Integer> kmpSearch(String text, String pattern) {
        List<Integer> occurrences = new ArrayList<>();
        int n = text.length();
        int m = pattern.length();
        if (m == 0 || n == 0 || m > n) return occurrences;

        int[] lps = computeLPSArray(pattern);
        int i = 0; // index for text
        int j = 0; // index for pattern

        while (i < n) {
            if (pattern.charAt(j) == text.charAt(i)) {
                i++;
                j++;
            }
            if (j == m) {
                occurrences.add(i - j);
                j = lps[j - 1];
            } else if (i < n && pattern.charAt(j) != text.charAt(i)) {
                if (j != 0) {
                    j = lps[j - 1];
                } else {
                    i++;
                }
            }
        }
        return occurrences;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextLine()) return;
        String text = sc.nextLine().trim();
        if (!sc.hasNextLine()) return;
        String pattern = sc.nextLine().trim();

        List<Integer> matches = kmpSearch(text, pattern);
        for (int k = 0; k < matches.size(); k++) {
            if (k > 0) System.out.print(" ");
            System.out.print(matches.get(k));
        }
        System.out.println();
    }
}
