import java.util.*;
import java.util.stream.Collectors;

public class Main {
    static class SensorReading {
        String id;
        double temp;

        SensorReading(String id, double temp) {
            this.id = id;
            this.temp = temp;
        }

        public String getId() {
            return id;
        }

        public double getTemp() {
            return temp;
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        List<SensorReading> readings = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            String id = sc.next();
            double temp = sc.nextDouble();
            readings.add(new SensorReading(id, temp));
        }

        // 1. Filter temperatures greater than 50
        // 2. Group readings by sensor ID
        // 3. Compute average temperature per sensor
        Map<String, Double> avgMap = readings.stream()
                .filter(r -> r.getTemp() > 50)
                .collect(Collectors.groupingBy(
                        SensorReading::getId,
                        Collectors.averagingDouble(SensorReading::getTemp)
                ));

        // 4. Sort sensors based on average temperature in descending order
        avgMap.entrySet().stream()
                .sorted((e1, e2) -> {
                    int cmp = Double.compare(e2.getValue(), e1.getValue());
                    if (cmp != 0) return cmp;
                    return e1.getKey().compareTo(e2.getKey());
                })
                .forEach(e -> System.out.println(e.getKey() + " " + e.getValue()));
    }
}
