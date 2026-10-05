import java.util.*;

public class Main {
    static boolean match(char o, char c) {
        return (o == '(' && c == ')') || (o == '[' && c == ']') || (o == '{' && c == '}') || (o == '<' && c == '>');
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextLine()) return;
        String s = sc.nextLine().trim();
        Deque<Character> st = new ArrayDeque<>();
        boolean ok = true;
        for (char c : s.toCharArray()) {
            if ("([{<".indexOf(c) >= 0) {
                st.push(c);
            } else if (")]}>".indexOf(c) >= 0) {
                if (st.isEmpty() || !match(st.pop(), c)) {
                    ok = false;
                    break;
                }
            }
        }
        if (!st.isEmpty()) ok = false;
        System.out.println(ok ? "VALID" : "INVALID");
    }
}
