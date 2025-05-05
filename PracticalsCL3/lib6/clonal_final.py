import numpy as np
import matplotlib.pyplot as plt
# Sphere objective function (to minimize)
def objective_function(x):
    return np.sum(x ** 2)

# Initialize the population
def initialize_population(pop_size, dim, bounds):
    return np.random.uniform(bounds[0], bounds[1], (pop_size, dim))

# Calculate affinity (higher = better)
def calculate_affinity(population):
    return np.array([1 / (1 + objective_function(ind)) for ind in population])

# Select top antibodies based on affinity
def select_antibodies(population, affinity, num_selected):
    sorted_indices = np.argsort(-affinity)
    return population[sorted_indices[:num_selected]]

# Clone antibodies (more clones for higher-affinity)
def clone_antibodies(selected, affinity, num_clones):
    clones = []
    for i, antibody in enumerate(selected):
        n_clones = max(1, int(affinity[i] * num_clones))  # Ensure at least 1 clone
        clones.extend([antibody.copy() for _ in range(n_clones)])
    return np.array(clones)

# Mutate antibodies
def mutate_antibodies(clones, mutation_rate, bounds):
    mutated = clones.copy()
    for i in range(len(mutated)):
        for j in range(len(mutated[i])):
            if np.random.rand() < mutation_rate:
                mutated[i][j] += np.random.uniform(-1, 1)
                mutated[i][j] = np.clip(mutated[i][j], bounds[0], bounds[1])
    return mutated

# Select best individuals for next generation
def select_next_generation(original, mutated, pop_size):
    combined = np.vstack((original, mutated))
    affinity = calculate_affinity(combined)
    sorted_indices = np.argsort(-affinity)
    return combined[sorted_indices[:pop_size]]

# Main CSA algorithm
def clonal_selection_algorithm(pop_size, dim, bounds, mutation_rate, num_generations):
    population = initialize_population(pop_size, dim, bounds)
    best_fitness_per_generation = []  # 📊 Store best fitness

    for generation in range(num_generations):
        affinity = calculate_affinity(population)
        num_selected = int(pop_size * 0.3)
        selected = select_antibodies(population, affinity, num_selected=num_selected)
        clones = clone_antibodies(selected, affinity[:num_selected], num_clones=10)
        mutated = mutate_antibodies(clones, mutation_rate, bounds)
        population = select_next_generation(population, mutated, pop_size)

        best = population[np.argmax(calculate_affinity(population))]
        best_fitness = objective_function(best)
        best_fitness_per_generation.append(best_fitness)  # 📌 Save best fitness
        print(f"Generation {generation + 1} - Best Fitness: {best_fitness:.6f}")

    # 📈 Plot convergence
    plt.plot(best_fitness_per_generation, marker='o')
    plt.title('Convergence Plot of CSA')
    plt.xlabel('Generation')
    plt.ylabel('Best Fitness')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    return best

# Run the algorithm
if __name__ == "__main__":
    pop_size = 50
    dim = 5
    bounds = (-5, 5)
    mutation_rate = 0.2
    num_generations = 20

    best_solution = clonal_selection_algorithm(pop_size, dim, bounds, mutation_rate, num_generations)
    print("\nOptimized Solution:", best_solution)
    print("Final Fitness (Objective Value):", objective_function(best_solution))


    