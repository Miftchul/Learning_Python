# Genetic Algorithm Example: Simple Optimization Problem
# This program demonstrates a genetic algorithm to solve a simple optimization problem.
# It uses selection, crossover, and mutation to evolve solutions over generations.

import random

def fitness_function(x):
    return -(x**2) + 5*x + 20

def generate_population(size, lower_bound, upper_bound):
    return [random.uniform(lower_bound, upper_bound) for _ in range(size)]

def select_parents(population):
    return random.sample(population, 2)

def crossover(parent1, parent2):
    return (parent1 + parent2) / 2

def mutate(individual, mutation_rate, lower_bound, upper_bound):
    if random.random() < mutation_rate:
        return random.uniform(lower_bound, upper_bound)
    return individual

def genetic_algorithm(generations, population_size, lower_bound, upper_bound, mutation_rate):
    population = generate_population(population_size, lower_bound, upper_bound)
    for _ in range(generations):
        population = sorted(population, key=fitness_function, reverse=True)
        new_population = []
        for _ in range(population_size // 2):
            parent1, parent2 = select_parents(population)
            child = crossover(parent1, parent2)
            child = mutate(child, mutation_rate, lower_bound, upper_bound)
            new_population.extend([parent1, child])
        population = new_population
    return max(population, key=fitness_function)

def main():
    best_solution = genetic_algorithm(50, 10, -10, 10, 0.1)
    print(f"Best solution: {best_solution} with fitness: {fitness_function(best_solution)}")

if __name__ == "__main__":
    main()