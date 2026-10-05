from collections import deque

print("=== Task 1a: Stock Market Prediction using BFS ===")
graph = {
    "Company A": ["Company B", "Company C"],
    "Company B": ["Company D"],
    "Company C": ["Company D"],
    "Company D": ["Company E", "Company F"],
    "Company E": [],
    "Company F": [],
    "Company G": []
}

def bfs_influence(graph, start_company, max_depth=2):
    queue = deque([[start_company, 0]])
    visited = set([start_company])
    impacted_companies = []
    while queue:
        current_company, depth = queue.popleft()
        if depth == max_depth:
            continue
        for neighbor in graph.get(current_company, []):
            if neighbor not in visited:
                visited.add(neighbor)
                impacted_companies.append(neighbor)
                queue.append([neighbor, depth + 1])
    return impacted_companies

starting_company = "Company A"
impacted = bfs_influence(graph, starting_company, max_depth=2)
print(f"If {starting_company} experiences a significant event, companies may be impacted:")
for company in impacted:
    print(company)

print("\n=== Task 1b: Weather Forecasting using DFS ===")
weather_graph = {
    'station A': ['station B', 'station C'],
    'station B': ['station D'],
    'station C': ['station F'],
    'station D': ['station E'],
    'station E': [],
    'station F': [],
    'station P': []
}
weather_data = {
    'station A': 'sunny',
    'station B': 'cloudy',
    'station C': 'rainy',
    'station D': 'stormy',
    'station E': 'windy',
    'station F': 'snowy'
}

def dfs(graph, node, visited):
    if node not in visited:
        print(f"{node} reports: {weather_data[node]}")
        visited.add(node)
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)

visited = set()
print("Weather forecast (DFS):")
dfs(weather_graph, 'station A', visited)
