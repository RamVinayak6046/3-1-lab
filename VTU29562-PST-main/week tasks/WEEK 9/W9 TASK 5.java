import java.util.*;

interface Payment {
    void pay(double amount);
}

class CreditCardPayment implements Payment {
    public void pay(double amount) {
    }
}

class UPIPayment implements Payment {
    public void pay(double amount) {
    }
}

class NetBankingPayment implements Payment {
    public void pay(double amount) {
    }
}

abstract class PaymentProcessor {
    abstract double processPayment(Payment payment, double amount);
}

class OnlinePaymentProcessor extends PaymentProcessor {
    public double processPayment(Payment payment, double amount) {
        payment.pay(amount);

        if (payment instanceof CreditCardPayment) {
            return amount + (amount * 0.02);
        }

        if (payment instanceof UPIPayment) {
            return amount + (amount * 0.01);
        }

        return amount + (amount * 0.015);
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
            String paymentType;

            switch (type) {
                case 1:
                    payment = new CreditCardPayment();
                    paymentType = "CreditCard";
                    break;

                case 2:
                    payment = new UPIPayment();
                    paymentType = "UPI";
                    break;

                default:
                    payment = new NetBankingPayment();
                    paymentType = "NetBanking";
            }

            double result = processor.processPayment(payment, amount);

            System.out.printf("%s %.2f%n", paymentType, result);
        }

        sc.close();
    }
}
