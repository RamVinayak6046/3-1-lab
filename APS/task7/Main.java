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

    static int height(Node n) {
        return n == null ? -1 : 1 + Math.max(height(n.l), height(n.r));
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++) a[i] = sc.nextInt();
        int h = height(build(a));
        System.out.println("Height = " + h);
        System.out.println("Levels = " + (h + 1));
    }
}
