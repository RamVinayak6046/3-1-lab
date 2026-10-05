import java.util.*;

public class Main {
    static class Task { 
        char id; 
        int ready; 
        Task(char i, int r) { id = i; ready = r; } 
    } 

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in); 
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt(), k = sc.nextInt(); 
        Map<Character, Integer> count = new HashMap<>();
        for (int i = 0; i < n; i++) {
            char c = sc.next().charAt(0);
            count.put(c, count.getOrDefault(c, 0) + 1);
        } 
        PriorityQueue<Character> pq = new PriorityQueue<>((a, b) -> Integer.compare(count.get(b), count.get(a))); 
        pq.addAll(count.keySet());
        Queue<Task> cool = new ArrayDeque<>(); 
        int time = 0; 
        while (!pq.isEmpty() || !cool.isEmpty()) {
            time++;
            while (!cool.isEmpty() && cool.peek().ready <= time) {
                pq.offer(cool.poll().id); 
            }
            if (!pq.isEmpty()) {
                char c = pq.poll(); 
                int left = count.get(c) - 1; 
                count.put(c, left); 
                if (left > 0) cool.offer(new Task(c, time + k + 1));
            }
        }
        System.out.println(time);
    }
}
