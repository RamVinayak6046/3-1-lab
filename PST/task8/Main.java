import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int m = sc.nextInt();

        // Graph representation using nested collections (Map of Lists)
        Map<Integer, List<Integer>> graph = new HashMap<>();
        for (int i = 1; i <= n; i++) {
            graph.put(i, new ArrayList<>());
        }

        for (int i = 0; i < m; i++) {
            int u = sc.nextInt();
            int v = sc.nextInt();
            graph.computeIfAbsent(u, k -> new ArrayList<>()).add(v);
            graph.computeIfAbsent(v, k -> new ArrayList<>()).add(u);
        }

        int src = sc.nextInt();
        int dst = sc.nextInt();

        // BFS to check connectivity
        boolean routeExists = false;
        Set<Integer> visited = new HashSet<>();
        Queue<Integer> queue = new ArrayDeque<>();

        queue.offer(src);
        visited.add(src);

        while (!queue.isEmpty()) {
            int curr = queue.poll();
            if (curr == dst) {
                routeExists = true;
                break;
            }
            for (int neighbor : graph.getOrDefault(curr, Collections.emptyList())) {
                if (!visited.contains(neighbor)) {
                    visited.add(neighbor);
                    queue.offer(neighbor);
                }
            }
        }

        System.out.println(routeExists ? "YES" : "NO");
    }
}
