import heapq
import sys

# Ensure UTF-8 output encoding on Windows console
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

graph = {
    'A': {'B': 6, 'F': 3},
    'B': {'C': 1, 'G': 6, 'F': 3},
    'C': {'D': 1, 'E': 5},
    'D': {'E': 8},
    'E': {'I': 5, 'J': 5},
    'F': {'G': 1, 'H': 7},
    'G': {'H': 3},
    'H': {'I': 2},
    'I': {'H': 2, 'J': 3},
    'J': {}
}

position = {
    'A': 10,
    'B': 8,
    'C': 5,
    'D': 7,
    'E': 3,
    'F': 6,
    'G': 5,
    'H': 3,
    'I': 1,
    'J': 0
}

def heuristic(a, b):
    return abs(position[a] - position[b])

def a_star(graph, start, goal):
    open_set = []
    heapq.heappush(open_set, (heuristic(start, goal), 0, start))
    came_from = {}
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0

    while open_set:
        f, g, current = heapq.heappop(open_set)
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1], g_score[goal]

        for neighbor, cost in graph[current].items():
            tentative_g = g_score[current] + cost
            if tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score = tentative_g + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_score, tentative_g, neighbor))

    return None, float('inf')

if __name__ == "__main__":
    start_node = 'H'
    goal_node = 'J'
    path, total_cost = a_star(graph, start_node, goal_node)
    if path:
        print("→".join(path))
        print("Total cost:", total_cost)
    else:
        print("No path!")
