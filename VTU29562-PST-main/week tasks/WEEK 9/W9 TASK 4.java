import java.util.*;

interface Payment {
    void pay(double amount);
}

class CreditCardPayment implements Payment {
    public void pay(double amount) {
        System.out.println("Credit Card payment");
    }
}

class UPIPayment implements Payment {
    public void pay(double amount) {
        System.out.println("UPI payment");
    }
}

class NetBankingPayment implements Payment {
    public void pay(double amount) {
        System.out.println("Net Banking payment");
    }
}

abstract class PaymentProcessor {
    abstract double processPayment(Payment payment, double amount);
}

class OnlinePaymentProcessor extends PaymentProcessor {
    double processPayment(Payment payment, double amount) {
        if (payment instanceof CreditCardPayment) {
            return amount * 1.02;
        } else if (payment instanceof UPIPayment) {
            return amount * 1.01;
        } else {
            return amount * 1.015;
        }
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();

        PaymentProcessor processor = new OnlinePaymentProcessor();

        for (int i = 0; i < n; i++) {
            int type = sc.nextInt();
            double amount = sc.nextDouble();

            Payment payment;
            String name;

            if (type == 1) {
                payment = new CreditCardPayment();
                name = "CreditCard";
            } else if (type == 2) {
                payment = new UPIPayment();
                name = "UPI";
            } else {
                payment = new NetBankingPayment();
                name = "NetBanking";
            }

            double finalAmount = processor.processPayment(payment, amount);

            System.out.printf("%s %.2f%n", name, finalAmount);
        }

        sc.close();
    }
}
