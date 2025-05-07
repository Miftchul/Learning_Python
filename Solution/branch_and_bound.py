# Branch and Bound Example: Traveling Salesman Problem (Simplified)
# This program solves a simplified version of the Traveling Salesman Problem (TSP).
# It uses the branch and bound method to find the shortest possible route that visits each city exactly once and returns to the origin city.

import itertools

def calculate_cost(path, graph):
    cost = 0
    for i in range(len(path) - 1):
        cost += graph[path[i]][path[i + 1]]
    cost += graph[path[-1]][path[0]]  # Return to the starting point
    return cost

def traveling_salesman(graph):
    n = len(graph)
    vertices = list(range(n))
    min_cost = float('inf')
    best_path = None

    for perm in itertools.permutations(vertices):
        cost = calculate_cost(perm, graph)
        if cost < min_cost:
            min_cost = cost
            best_path = perm

    return best_path, min_cost

def main():
    graph = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]
    path, cost = traveling_salesman(graph)
    print(f"Best path: {path} with cost: {cost}")

if __name__ == "__main__":
    main()