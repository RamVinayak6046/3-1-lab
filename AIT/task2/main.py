import random

def generate_random_route(num_customers):
    customers = list(range(1, num_customers + 1))
    random.shuffle(customers)
    return [0] + customers + [0]

def generate_neighbors(route):
    neighbors = []
    n = len(route)
    for i in range(1, n - 1):
        for j in range(i + 1, n - 1):
            neighbor = route.copy()
            neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
            neighbors.append(neighbor)
    return neighbors

def calculate_total_distance(route, dist_matrix):
    total_dist = 0
    for i in range(len(route) - 1):
        total_dist += dist_matrix[route[i]][route[i + 1]]
    return total_dist

def hill_climbing(dist_matrix, initial_route):
    current_route = initial_route
    current_distance = calculate_total_distance(current_route, dist_matrix)
    improving = True
    while improving:
        improving = False
        neighbors = generate_neighbors(current_route)
        for neighbor in neighbors:
            neighbor_distance = calculate_total_distance(neighbor, dist_matrix)
            if neighbor_distance < current_distance:
                current_route = neighbor
                current_distance = neighbor_distance
                improving = True
                break
    return current_route, current_distance

if __name__ == "__main__":
    num_customers = 5
    dist_matrix = [
        [0, 12, 9, 10, 7, 3],
        [20, 0, 6, 4, 3, 8],
        [9, 6, 0, 18, 5, 7],
        [10, 4, 18, 0, 6, 5],
        [7, 3, 5, 6, 0, 4],
        [3, 8, 7, 5, 4, 0]
    ]
    initial_route = generate_random_route(num_customers)
    print("Initial route:", initial_route)
    print("Initial distance:", calculate_total_distance(initial_route, dist_matrix))
    optimized_route, optimized_distance = hill_climbing(dist_matrix, initial_route)
    print("Optimized route:", optimized_route)
    print("Optimized distance:", optimized_distance)
