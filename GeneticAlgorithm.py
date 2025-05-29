import random
from GatherData import Refined


POPULATION_SIZE = 100
GENOME_LENGHT = 3
MUTATION_RATE = 0.01
CROSSOVER_RATE = 0.7
RegressionCount = 5
ColumnCount = 11
GENERATIONS = RegressionCount * ColumnCount

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
    predicted = 0
    actual = 0

def MakeRandomGeneration():
    genomes = []
    for i in range(0, 10):
        genome = GenomeModel(0,0,0)
        genome.SandP = random.randint(0,100)
        genome.analystrating = random.randint(0,100)
        genome.affected = random.randint(0,100)
        genome.linearregslope = random.randint(0,100)
        genome.linearregline = random.randint(0,100)
        genome.levelsupport = random.randint(0,100)
        genome.movingaveragecross = random.randint(0,100)
        genome.relativestrength = random.randint(0,100)
        genome.MACDcross = random.randint(0,100)
        genome.bollinger = random.randint(0,100)
        genome.EMAsign = random.randint(0,100)
        genome.predicted = random.randint(0,100)
        genome.actual = random.randint(0,100)
        genomes.append(genome)
    return genomes


#Generating a genome
'''
def make_genome(RefindeGenome:Refined):
    return RefindeGenome
'''

def make_genome(RSI, Aup, Adown):
    return GenomeModel(RSI, Aup, Adown)


#Initial population
def init_population(population_size, genome_length, Data):
    population = []
#    for i in range(0,population_size):
#        population.append(make_genome(Data[i].RSI, Data[i].Aup, Data[i].Adown))
    for i in range(0, population_size):
        population.append(make_genome(0,0,0))
    return population

#Calculating the fitness function
def fitness(genome):
    return abs(genome.predicted - genome.actual) / genome.actual

#Selecting a parent randomly
def select_parent(population, fitness_values):
    return population[random.randint(0,5)]

#crossover, change trigger condition later!
def crossover(parent1, parent2):
    if random.random() < CROSSOVER_RATE:
        temp = parent1
        parent1.SandP = parent2.SandP
        parent2.SandP = temp.SandP
    return parent1, parent2

def mutate(genome):
    #we only want crossovers for now
    return genome

def genetic_algorithm():
    #generating data
    Data =[]
    Data.append(GenomeModel(20,90,10))
    Data.append(GenomeModel(40,40,45))
    Data.append(GenomeModel(60,23,92))
    #creating innitial population
    #population = init_population(POPULATION_SIZE, GENOME_LENGHT, Data)
    population = MakeRandomGeneration()
    #looping throught generations
    for generation in range(GENERATIONS):
        #calculating fitness values change firness to errorfitness later!
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
        best_fitness = min(fitness_values)
        #best fitness in the current generation
        print(f"{generation}:Best Fitness = {best_fitness}")
    #best found genomes
    best_index = fitness_values.index(min(fitness_values))
    best_solution = population[best_index]
    print(f'Best Solution: {best_solution}')
    print(f'Best fitness: {fitness(best_solution)}')

genetic_algorithm()
