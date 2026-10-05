import numpy as np
import random
import sys

# Ensure UTF-8 output encoding on Windows console
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

cities = [
    "Depot", "Mumbai", "Delhi", "Chennai", "Kolkata", 
    "Bangalore", "Hyderabad", "Pune", "Ahmedabad", "Jaipur", "Lucknow"
]

dist_matrix = [
    [0, 14, 12, 10, 16, 9, 7, 11, 5, 11, 9],
    [12, 0, 15, 10, 22, 13, 12, 11, 9, 10, 13],
    [10, 13, 0, 22, 17, 3, 6, 9, 12, 9, 12],
    [16, 16, 13, 0, 17, 19, 16, 13, 9, 11, 12],
    [9, 1, 9, 21, 0, 19, 15, 7, 9, 17, 18],
    [7, 7, 19, 6, 16, 0, 10, 5, 18, 14, 15],
    [1, 1, 10, 9, 13, 7, 0, 15, 4, 9, 10],
    [5, 15, 9, 12, 19, 9, 8, 0, 14, 3, 9],
    [11, 11, 3, 19, 11, 17, 14, 9, 0, 10, 3],
    [9, 9, 6, 21, 12, 18, 15, 10, 9, 0, 8],
    [9, 13, 12, 12, 18, 15, 10, 9, 3, 8, 0]
]

dist_matrix = np.array(dist_matrix)
n_locations = len(cities)
n_ants = 20
n_iterations = 100
alpha = 1.0
beta = 5.0
rho = 0.5
Q = 100
pheromone = np.ones((n_locations, n_locations))

def route_length(route):
    return sum(dist_matrix[route[i], route[i + 1]] for i in range(len(route) - 1))

def ant_tour():
    start = 0
    tour = [start]
    unvisited = list(range(1, n_locations))
    while unvisited:
        i = tour[-1]
        probs = []
        for j in unvisited:
            tau = pheromone[i, j] ** alpha
            eta = (1.0 / dist_matrix[i, j]) ** beta
            probs.append(tau * eta)
        probs = np.array(probs) / np.sum(probs)
        next_city = random.choices(unvisited, weights=probs, k=1)[0]
        tour.append(next_city)
        unvisited.remove(next_city)
    tour.append(start)
    return tour

best_route = None
best_length = float("inf")

for it in range(n_iterations):
    all_routes = []
    all_lengths = []
    for ant in range(n_ants):
        tour = ant_tour()
        length = route_length(tour)
        all_routes.append(tour)
        all_lengths.append(length)
        if length < best_length:
            best_length = length
            best_route = tour
    pheromone *= (1 - rho)
    for route, length in zip(all_routes, all_lengths):
        for i in range(len(route) - 1):
            pheromone[route[i], route[i + 1]] += Q / length

try:
    arrow = "→"
    print("Best Route found:", f" {arrow} ".join(cities[i] for i in best_route))
except UnicodeEncodeError:
    arrow = "->"
    print("Best Route found:", f" {arrow} ".join(cities[i] for i in best_route))

print("Best Route length:", best_length)
