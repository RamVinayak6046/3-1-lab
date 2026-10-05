import java.util.*;

class UndergroundSystem {

    // customerId -> [station, checkInTime]
    HashMap<Integer, String[]> checkInMap;

    // route -> [totalTime, numberOfTrips]
    HashMap<String, double[]> routeMap;

    public UndergroundSystem() {
        checkInMap = new HashMap<>();
        routeMap = new HashMap<>();
    }

    public void checkIn(int id, String stationName, int t) {
        checkInMap.put(id, new String[]{stationName, String.valueOf(t)});
    }

    public void checkOut(int id, String stationName, int t) {

        String[] data = checkInMap.get(id);

        String startStation = data[0];
        int startTime = Integer.parseInt(data[1]);

        String route = startStation + "#" + stationName;

        double[] info = routeMap.getOrDefault(route, new double[]{0, 0});

        info[0] += t - startTime;
        info[1]++;

        routeMap.put(route, info);

        checkInMap.remove(id);
    }

    public double getAverageTime(String startStation, String endStation) {

        String route = startStation + "#" + endStation;

        double[] info = routeMap.get(route);

        return info[0] / info[1];
    }
}
