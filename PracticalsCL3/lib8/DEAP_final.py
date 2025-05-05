import random
import multiprocessing
import matplotlib.pyplot as plt
from deap import base, creator, tools, algorithms

# Evaluation Function (Sphere Function)
def eval_func(individual):
    return sum(x ** 2 for x in individual),

# ----- DEAP Setup -----
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

toolbox = base.Toolbox()
toolbox.register("attr_float", random.uniform, -5.0, 5.0)
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_float, n=3)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

toolbox.register("evaluate", eval_func)
toolbox.register("mate", tools.cxBlend, alpha=0.5)
toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=1, indpb=0.2)
toolbox.register("select", tools.selTournament, tournsize=3)

if __name__ == '__main__':
    # Multiprocessing pool for parallelism
    pool = multiprocessing.Pool()
    toolbox.register("map", pool.map)

    population = toolbox.population(n=50)
    generations = 20
    best_fitnesses = []

    for gen in range(generations):
        offspring = algorithms.varAnd(population, toolbox, cxpb=0.5, mutpb=0.1)
        fitnesses = toolbox.map(toolbox.evaluate, offspring)

        for fit, ind in zip(fitnesses, offspring):
            ind.fitness.values = fit

        population = toolbox.select(offspring, k=len(population))

        # Track best fitness
        best_ind = tools.selBest(population, k=1)[0]
        best_fitness = best_ind.fitness.values[0]
        best_fitnesses.append(best_fitness)
        print(f"Generation {gen+1}: Best fitness = {best_fitness:.4f}")

    # Final output
    print("\nBest individual:", best_ind)
    print("Best fitness:", best_fitness)

    # Clean up
    pool.close()
    pool.join()

    # Plot convergence
    plt.plot(range(1, generations + 1), best_fitnesses, marker='o')
    plt.title("Convergence Curve")
    plt.xlabel("Generation")
    plt.ylabel("Best Fitness")
    plt.grid(True)
    plt.show()