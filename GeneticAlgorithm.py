import random

POPULATION_SIZE = 100
GENOME_LENGHT = 5
MUTATION_RATE = 0.01
CROSSOVER_RATE = 0.7
GENERATIONS = 50

#Generating a genome
def random_genome():
    #genome = [random.randint(0,100) for _ in range(GENOME_LENGHT)]
    genome = []
    genome.append(random.randint(0,100))
    genome.append(-1 * random.randint(0,100))
    genome.append(random.randint(0,100))
    genome.append(random.randint(0,100))
    genome.append(random.randint(0,100))
    return genome

#Initial population
def init_population(population_size, genome_length):
    return [random_genome() for _ in range(population_size)]

#Calculating the fitness function
def fitness(genome):
    return sum(genome)

#Selecting a parent randomly
def select_parent(population, fitness_values):
    total_fitness = sum(fitness_values)
    pick = random.uniform(0,total_fitness)
    current = 0
    for individual, fitness_value in zip(population,fitness_values):
        current += fitness_value
        if current > pick:
            return individual

def crossover(parent1, parent2):
    if random.random() < CROSSOVER_RATE:
        crossover_point = random.randint(1,len(parent1) -1)
        return parent1[:crossover_point] + parent2[crossover_point:], parent2[:crossover_point] + parent1[crossover_point:]
    else:
        return parent1, parent2

def mutate(genome):
    for i in range(len(genome)):
        if random.random() < MUTATION_RATE:
            genome[0] -= 10
    return genome

def genetic_algorithm():
    population = init_population(POPULATION_SIZE, GENOME_LENGHT)
    for generation in range(GENERATIONS):
        fitness_values = [fitness(genome) for genome in population]
        new_population = []
        for _ in range(POPULATION_SIZE // 2):
            parent1 = select_parent(population, fitness_values)
            parent2 = select_parent(population,fitness_values)
            offspring1, offspring2 = crossover(parent1, parent2)
            new_population.extend([mutate(offspring1), mutate(offspring2)])
        population = new_population

        fitness_values = [fitness(genome) for genome in population]
        best_fitness = max(fitness_values)
        print(f"{generation}:Best Fitness = {best_fitness}")
    best_index = fitness_values.index(max(fitness_values))
    best_solution = population[best_index]
    print(f'Best Solution: {best_solution}')
    print(f'Best fitness: {fitness(best_solution)}')

genetic_algorithm()
