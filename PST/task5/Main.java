import java.util.*;

class BankAccount {
    private long balance;

    public BankAccount(long initialBalance) {
        this.balance = initialBalance;
    }

    public void deposit(long amount) {
        if (amount > 0) {
            balance += amount;
        }
    }

    public boolean withdraw(long amount) {
        if (amount > 0 && balance >= amount) {
            balance -= amount;
            return true;
        }
        return false;
    }

    public long getBalance() {
        return balance;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();

        BankAccount account = new BankAccount(0);

        for (int i = 0; i < n; i++) {
            String op = sc.next();
            long amount = sc.nextLong();
            if (op.equalsIgnoreCase("Deposit")) {
                account.deposit(amount);
            } else if (op.equalsIgnoreCase("Withdraw")) {
                account.withdraw(amount);
            }
        }

        System.out.println(account.getBalance());
    }
}
