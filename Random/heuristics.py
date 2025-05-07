# Heuristics Example: A* Algorithm (Simplified)
# This program demonstrates the A* algorithm, a heuristic-based search algorithm.
# It finds the shortest path from a start node to a goal node using a cost function.

from queue import PriorityQueue

def a_star_algorithm(start, goal, graph, heuristic):
    open_set = PriorityQueue()
    open_set.put((0, start))
    came_from = {}
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0

    while not open_set.empty():
        _, current = open_set.get()

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]

        for neighbor, cost in graph[current].items():
            tentative_g_score = g_score[current] + cost
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + heuristic[neighbor]
                open_set.put((f_score, neighbor))

    return None

def main():
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }
    heuristic = {'A': 7, 'B': 6, 'C': 2, 'D': 0}
    start, goal = 'A', 'D'
    path = a_star_algorithm(start, goal, graph, heuristic)
    print(f"Path from {start} to {goal}: {path}")

if __name__ == "__main__":
    main()