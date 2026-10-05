from collections import defaultdict
import sys

# Ensure UTF-8 output encoding on Windows console
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

class Graph:
    def __init__(self, vertices): 
        self.v = vertices
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def greedy_coloring(self, max_colors=None):
        result = [-1] * self.v
        available = [True] * self.v
        for u in range(self.v):
            for i in self.graph[u]:
                if result[i] != -1:
                    available[result[i]] = False
            cr = 0
            while cr < self.v:
                if available[cr]:
                    break
                cr += 1
            result[u] = cr
            for i in self.graph[u]:
                if result[i] != -1:
                    available[result[i]] = True

        max_color_used = max(result) 
        if max_colors is not None:
            if max_color_used < max_colors:
                print(f" With {max_colors} colors: Coloring is possible!")
            else:
                print(f" With {max_colors} colors: Coloring is NOT possible!")
        else:
            print("\nColoring assignment:")
            for u in range(self.v):
                print(f"Zone {u} → Assigned color {result[u]}")
            print(f"Total colors used: {max_color_used + 1}")

if __name__ == "__main__":
    g = Graph(6)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 3)
    g.add_edge(2, 4)
    g.add_edge(3, 4)
    g.add_edge(4, 5)

    print("Robot Traversal Signal Plan with color limit check:")
    g.greedy_coloring(max_colors=2)
    print("\nRobot Traversal Signal Plan without color limit:")
    g.greedy_coloring()
