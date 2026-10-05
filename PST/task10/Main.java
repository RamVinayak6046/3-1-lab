import java.util.*;

class Authenticator {
    // Boundary constraints
    public static final int MIN_USER_LEN = 3;
    public static final int MAX_USER_LEN = 20;
    public static final int MIN_PASS_LEN = 6;
    public static final int MAX_PASS_LEN = 20;

    public static boolean validateCredentials(String username, String password) {
        if (username == null || password == null) {
            return false;
        }

        // Boundary value validation
        int uLen = username.length();
        int pLen = password.length();

        if (uLen < MIN_USER_LEN || uLen > MAX_USER_LEN) {
            return false;
        }

        if (pLen < MIN_PASS_LEN || pLen > MAX_PASS_LEN) {
            return false;
        }

        return true;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();

        for (int i = 0; i < n; i++) {
            String username = sc.next();
            String password = sc.next();

            boolean isValid = Authenticator.validateCredentials(username, password);
            System.out.println(isValid ? "SUCCESS" : "FAILURE");
        }
    }
}
