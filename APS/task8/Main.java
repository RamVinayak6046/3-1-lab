import java.util.*;

public class Main {
    static class Node { 
        int v; 
        Node l, r; 
        Node(int v) { this.v = v; } 
    }

    static Node build(int[] a) {
        if (a.length == 0 || a[0] == -1) return null;
        Node root = new Node(a[0]);
        Queue<Node> q = new ArrayDeque<>();
        q.offer(root);
        int i = 1;
        while (!q.isEmpty() && i < a.length) {
            Node p = q.poll();
            if (i < a.length && a[i] != -1) { 
                p.l = new Node(a[i]); 
                q.offer(p.l); 
            }
            i++;
            if (i < a.length && a[i] != -1) { 
                p.r = new Node(a[i]); 
                q.offer(p.r); 
            }
            i++;
        }
        return root;
    }

    static boolean path(Node n, int x, List<Node> p) {
        if (n == null) return false;
        p.add(n);
        if (n.v == x || path(n.l, x, p) || path(n.r, x, p)) return true;
        p.remove(p.size() - 1);
        return false;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++) a[i] = sc.nextInt();
        int x = sc.nextInt(), y = sc.nextInt();
        Node root = build(a);
        List<Node> p1 = new ArrayList<>(), p2 = new ArrayList<>();
        path(root, x, p1);
        path(root, y, p2);
        int ans = -1;
        for (int i = 0; i < Math.min(p1.size(), p2.size()); i++) {
            if (p1.get(i).v != p2.get(i).v) break;
            ans = p1.get(i).v;
        }
        System.out.println("LCA = " + ans);
    }
}
