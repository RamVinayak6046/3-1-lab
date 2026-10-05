import java.util.*;
class InvalidBookingException extends Exception {
    public InvalidBookingException(String message) {
        super(message);
    }
}

class Driver {
    private String name;
    public Driver(String name) { this.name = name; }
    public String getName() { return name; }
}

class Rider {
    private String name;
    public Rider(String name) { this.name = name; }
    public String getName() { return name; }
}
abstract class Vehicle {
    protected String type;
    protected double ratePerKm;

    public Vehicle(String type, double ratePerKm) {
        this.type = type;
        this.ratePerKm = ratePerKm;
    }

    public abstract long calculateFare(double distance);
}

class Bike extends Vehicle {
    public Bike() {
        super("Bike", 5.0);
    }

    @Override
    public long calculateFare(double distance) {
        return Math.round(distance * ratePerKm);
    }
}

class Auto extends Vehicle {
    public Auto() {
        super("Auto", 12.0);
    }

    @Override
    public long calculateFare(double distance) {
        return Math.round(distance * ratePerKm);
    }
}

class Cab extends Vehicle {
    public Cab() {
        super("Cab", 12.0);
    }

    @Override
    public long calculateFare(double distance) {
        return Math.round(distance * ratePerKm);
    }
}

// Trip class coordinating booking and fare calculation
class Trip {
    private Vehicle vehicle;
    private double distance;

    public Trip(String rideType, double distance) throws InvalidBookingException {
        if (distance < 0) {
            throw new InvalidBookingException("Distance cannot be negative");
        }
        this.distance = distance;
        if (rideType.equalsIgnoreCase("Bike")) {
            this.vehicle = new Bike();
        } else if (rideType.equalsIgnoreCase("Auto")) {
            this.vehicle = new Auto();
        } else if (rideType.equalsIgnoreCase("Cab")) {
            this.vehicle = new Cab();
        } else {
            throw new InvalidBookingException("Unknown ride type: " + rideType);
        }
    }

    public long getFare() {
        return vehicle.calculateFare(distance);
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();

        for (int i = 0; i < n; i++) {
            String rideType = sc.next();
            double distance = sc.nextDouble();
            try {
                Trip trip = new Trip(rideType, distance);
                System.out.println(trip.getFare());
            } catch (InvalidBookingException e) {
                System.err.println("Booking error: " + e.getMessage());
            }
        }
    }
}

