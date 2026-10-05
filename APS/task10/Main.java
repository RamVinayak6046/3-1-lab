import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt(), m = sc.nextInt();
        List<Integer>[] adj = new ArrayList[n + 1];
        for (int i = 1; i <= n; i++) adj[i] = new ArrayList<>();
        for (int i = 0; i < m; i++) {
            int u = sc.nextInt(), v = sc.nextInt();
            adj[u].add(v);
            adj[v].add(u);
        }
        boolean[] vis = new boolean[n + 1];
        int components = 0;
        for (int s = 1; s <= n; s++) {
            if (!vis[s]) {
                components++;
                Queue<Integer> q = new ArrayDeque<>();
                q.offer(s);
                vis[s] = true;
                while (!q.isEmpty()) {
                    int u = q.poll();
                    for (int v : adj[u]) {
                        if (!vis[v]) {
                            vis[v] = true;
                            q.offer(v);
                        }
                    }
                }
            }
        }
        System.out.println("Connected Components = " + components);
    }
}
