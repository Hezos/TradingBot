import random
from GatherData import Refined


POPULATION_SIZE = 100
GENOME_LENGHT = 3
MUTATION_RATE = 0.01
CROSSOVER_RATE = 0.7
GENERATIONS = 50

#Use the refined model
class GenomeModel:
    def __init__(self, RSI, Aup, Adown):
        self.RSI = RSI
        self.Aup = Aup
        self.Adown = Adown
    SandP = 0
    analystrating = 0
    affected = 0
    linearregslope = 0
    linearregline = 0
    levelsupport = 0
    movingaveragecross = 0
    relativestrength = 0
    MACDcross = 0
    bollinger = 0
    EMAsign = 0


#Generating a genome
'''
def make_genome(RefindeGenome:Refined):
    return RefindeGenome
'''

def make_genome(RSI, Aup, Adown):
    return GenomeModel(RSI, Aup, Adown);


#Generating a genome with random data
def make_random_genome(RSI, Aup, Adown):
    #genome = [random.randint(0,100) for _ in range(GENOME_LENGHT)]
    genome = []
    genome.append(random.randint(0,100))
    genome.append(-1 * random.randint(0,100))
    genome.append(random.randint(0,100))
    return genome

#Initial population
def init_population(population_size, genome_length, Data):
    population = []
#    for i in range(0,population_size):
#        population.append(make_genome(Data[i].RSI, Data[i].Aup, Data[i].Adown))
    for i in range(0, population_size):
        population.append(make_genome(0,0,0))
    return population

def errorFitness(predicteds:[], actuals:[]):
    sum_error = 0
    for i in range(0, len(predicteds)):
        sum_error += (abs((predicteds[i] - actuals[i])) / actuals)
    return sum_error/len(predicteds)

#Calculating the fitness function
def fitness(genome):
    return genome.RSI + genome.Aup + genome.Adown

#Selecting a parent randomly
def select_parent(population, fitness_values):
    return population[random.randint(0,1)]

#crossover, change trigger condition later!
def crossover(parent1, parent2):
    if random.random() < CROSSOVER_RATE:
        temp = parent1
        parent1.SandP = parent2.SandP
        parent2.SandP = temp.SandP
    return parent1, parent2

def mutate(genome):
    genome.RSI += MUTATION_RATE
    return genome

def genetic_algorithm():
    #generating data
    Data =[]
    Data.append(GenomeModel(20,90,10))
    Data.append(GenomeModel(40,40,45))
    Data.append(GenomeModel(60,23,92))
    #creating innitial population
    population = init_population(POPULATION_SIZE, GENOME_LENGHT, Data)
    #looping throught generations
    for generation in range(GENERATIONS):
        #calculating fitness values
        fitness_values = []
        for genome in population:
            fitness_values.append(fitness(genome))
        #making a new population
        new_population = []
        for _ in range(POPULATION_SIZE // 2):
            parent1 = select_parent(population, fitness_values)
            parent2 = select_parent(population,fitness_values)
            offspring1, offspring2 = crossover(parent1, parent2)
            new_population.extend([mutate(offspring1), mutate(offspring2)])
        #switching old population to the new one
        population = new_population
        #collecting fitness values.
        fitness_values = [fitness(genome) for genome in population]
        best_fitness = max(fitness_values)
        #best fitness in the current generation
        print(f"{generation}:Best Fitness = {best_fitness}")
    #best found genomes
    best_index = fitness_values.index(max(fitness_values))
    best_solution = population[best_index]
    print(f'Best Solution: {best_solution}')
    print(f'Best fitness: {fitness(best_solution)}')

genetic_algorithm()
