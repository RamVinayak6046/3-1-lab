import java.util.*;

public class Main {
    static class Node { 
        int data; 
        Node next; 
        Node(int d) { data = d; } 
    } 

    static Node build(int[] a, int cyclePos) {
        if (a.length == 0) return null;
        Node head = new Node(a[0]), cur = head, cycle = null; 
        if (cyclePos == 0) cycle = head;
        for (int i = 1; i < a.length; i++) { 
            cur.next = new Node(a[i]); 
            cur = cur.next; 
            if (i == cyclePos) cycle = cur; 
        } 
        if (cyclePos >= 0) cur.next = cycle;
        return head;
    }

    static void removeCycle(Node head) {
        Node slow = head, fast = head;
        do { 
            if (fast == null || fast.next == null) return;
            slow = slow.next; 
            fast = fast.next.next; 
        } while (slow != fast); 

        slow = head;
        while (slow != fast) { 
            slow = slow.next; 
            fast = fast.next; 
        } 
        Node entry = slow, p = entry;
        while (p.next != entry) p = p.next; 
        p.next = null;
    }

    static Node reverseK(Node head, int k) {
        Node cur = head, prevTail = null, newHead = null; 
        while (cur != null) {
            Node check = cur; 
            int c = 0;
            while (check != null && c < k) { 
                check = check.next; 
                c++; 
            } 
            Node groupHead = cur, prev = null;
            for (int i = 0; i < c; i++) {
                Node next = cur.next;
                cur.next = prev;
                prev = cur;
                cur = next;
            } 
            if (newHead == null) newHead = prev; 
            else prevTail.next = prev; 
            prevTail = groupHead;
        }
        return newHead;
    }

    static void print(Node h) {
        boolean first = true; 
        while (h != null) {
            if (!first) System.out.print(" "); 
            System.out.print(h.data); 
            first = false; 
            h = h.next;
        } 
        System.out.println();
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in); 
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt(), k = sc.nextInt();
        int[] a = new int[n]; 
        for (int i = 0; i < n; i++) a[i] = sc.nextInt(); 
        int pos = sc.nextInt();
        Node head = build(a, pos); 
        if (pos >= 0) removeCycle(head); 
        head = reverseK(head, k); 
        print(head);
    }
}
