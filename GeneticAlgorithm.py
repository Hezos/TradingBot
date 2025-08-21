import random
from GatherData import Refined
import json

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

parent2 = GenomeModel(0,0,0)
parent2.actual = 1

def GenerateIndexMatrix(genomes:[]):
    print("Generating index matrix.")
    IndexMatrix = []



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
        genome.actual = random.randint(1,100)
        genomes.append(genome)
    return genomes


#Generating a genome
'''
def make_genome(RefindeGenome:Refined):
    return RefindeGenome
'''

def CalculatePredicted(factorRatios, factorAverages):
    result = []
    for i in len(0,factorRatios):
        result.append(factorRatios * factorAverages)
    return result

#Calculating the fitness function, change this to a list later
def fitness(genome, actuals:[]):
    actualdifference = 0
    for actual in actuals:
        actualdifference += abs(genome.predicted - actual) / actual
    return actualdifference

#crossover, change trigger condition later!
def crossover(population, fitness_values):
    testParent1 = population[0]
    testParent2 = population[0]
    parent1 = population[0]
    parent2 = population[0]
    for i in range(0, len(population)):
        for j in range(0, len(population)):
            didswitch = False
            if(i != j):
                if population[i].RSI != 0:
                #Do not hardcode numbers, use percentages instead!
                    if(abs(population[i].RSI - population[j].RSI) / population[i].RSI < 0.08):
                        testParent1 = population[i]
                        testParent2 = population[j]
                        testParent1.RSI = testParent2.RSI
                        testParent2.RSI = population[i].RSI
                        if testParent1 in population or testParent2 in population:
                            break
                        parent1 = testParent1
                        parent2 = testParent2
                if population[i].SandP != 0:
                    if(abs(population[i].SandP - population[j].SandP) / population[i].SandP < 0.08):
                        testParent1 = population[i]
                        testParent2 = population[j]
                        testParent1.SandP = testParent2.SandP
                        testParent2.SandP = population[i].SandP            
                        if testParent1 in population or testParent2 in population:
                            break
                        parent1 = testParent1
                        parent2 = testParent2
                if population[i].analystrating != 0:
                    if(abs(population[i].analystrating - population[j].analystrating) / population[i].analystrating < 0.08):
                        testParent1 = population[i]
                        testParent2 = population[j]
                        testParent1.analystrating = testParent2.analystrating
                        testParent2.analystrating = population[i].analystrating            
                        if testParent1 in population or testParent2 in population:
                            break
                        parent1 = testParent1
                        parent2 = testParent2
                if population[i].affected != 0:
                    if(abs(population[i].affected - population[j].affected) / population[i].affected < 0.08):
                        testParent1 = population[i]
                        testParent2 = population[j]
                        testParent1.affected = testParent2.affected
                        testParent2.affected = population[i].affected            
                        if testParent1 in population or testParent2 in population:
                            break
                        parent1 = testParent1
                        parent2 = testParent2            
                if population[i].linearregslope != 0:
                    if(abs(population[i].linearregslope - population[j].linearregslope) / population[i].linearregslope< 0.08):
                        testParent1 = population[i]
                        testParent2 = population[j]
                        testParent1.linearregslope = testParent2.linearregslope
                        testParent2.linearregslope = population[i].linearregslope            
                        if testParent1 in population or testParent2 in population:
                            break
                        parent1 = testParent1
                        parent2 = testParent2
                if population[i].linearregline != 0:  
                    if(abs(population[i].linearregline - population[j].linearregline) / population[i].linearregline < 0.08):
                        testParent1 = population[i]
                        testParent2 = population[j]
                        testParent1.linearregline = testParent2.linearregline
                        testParent2.linearregline = population[i].linearregline            
                        if testParent1 in population or testParent2 in population:
                            break
                        parent1 = testParent1
                        parent2 = testParent2
                if population[i].levelsupport != 0: 
                    if(abs(population[i].levelsupport - population[j].levelsupport) / population[i].levelsupport < 0.08):
                        testParent1 = population[i]
                        testParent2 = population[j]
                        testParent1.levelsupport = testParent2.levelsupport
                        testParent2.levelsupport = population[i].levelsupport            
                        if testParent1 in population or testParent2 in population:
                            break
                        parent1 = testParent1
                        parent2 = testParent2
                if population[i].movingaveragecross != 0:   
                    if(abs(population[i].movingaveragecross - population[j].movingaveragecross) / population[i].movingaveragecross < 0.11):
                        testParent1 = population[i]
                        testParent2 = population[j]
                        testParent1.movingaveragecross = testParent2.movingaveragecross
                        testParent2.movingaveragecross = population[i].movingaveragecross            
                        if testParent1 in population or testParent2 in population:
                            break
                        parent1 = testParent1
                        parent2 = testParent2
                if population[i].relativestrength != 0:
                    if(abs(population[i].relativestrength - population[j].relativestrength) / population[i].relativestrength < 0.08):
                        testParent1 = population[i]
                        testParent2 = population[j]
                        testParent1.relativestrength = testParent2.relativestrength
                        testParent2.relativestrength = population[i].relativestrength            
                        if testParent1 in population or testParent2 in population:
                            break
                        parent1 = testParent1
                        parent2 = testParent2
                if population[i].MACDcross != 0:            
                    if(abs(population[i].MACDcross - population[j].MACDcross) / population[i].MACDcross < 0.08):
                        testParent1 = population[i]
                        testParent2 = population[j]
                        testParent1.MACDcross = testParent2.MACDcross
                        testParent2.MACDcross = population[i].MACDcross            
                        if testParent1 in population or testParent2 in population:
                            break
                        parent1 = testParent1
                        parent2 = testParent2
                if population[i].bollinger != 0:
                    if(abs(population[i].bollinger - population[j].bollinger) / population[i].bollinger < 0.08):
                        testParent1 = population[i]
                        testParent2 = population[j]
                        testParent1.bollinger = testParent2.bollinger
                        testParent2.bollinger = population[i].bollinger            
                        if testParent1 in population or testParent2 in population:
                            break
                        parent1 = testParent1
                        parent2 = testParent2
                if population[i].EMAsign != 0:
                    if(abs(population[i].EMAsign - population[j].EMAsign) / population[i].EMAsign < 0.08):
                        testParent1 = population[i]
                        testParent2 = population[j]
                        testParent1.EMAsign = testParent2.EMAsign
                        testParent2.EMAsign = population[i].EMAsign            
                        if testParent1 in population or testParent2 in population:
                            break
                        parent1 = testParent1
                        parent2 = testParent2
    #Do a linear regression result recalculation before passing the parents
    return parent1, parent2

def mutate(genome, factorAverages):
    #This function is used to calculate the predictions
    factors = []
    factors.append(genome.RSI)
    factors.append(genome.EMAsign)
    factors.append(genome.movingaveragecross)
    factors.append(genome.bollinger)
    factors.append(genome.bollinger)
    genome.predicted = CalculatePredicted(factors, factorAverages)
    return genome

def genetic_algorithm():
    #creating innitial population
    #population = init_population(POPULATION_SIZE, GENOME_LENGHT, Data)
    population = MakeRandomGeneration()
    f = open("FactorAverages.txt")
    factorAverages = json.loads(f.read())
    f.close()
    Actuals = []
    for element in population:
        Actuals.append(element.actual)
    #looping throught generations
    for generation in range(GENERATIONS):
        #calculating fitness values change firness to errorfitness later!
        fitness_values = []
        for genome in population:
            fitness_values.append(fitness(genome= genome, actuals= Actuals))
        #making a new population
        for genome in population:
            offspring1, offspring2 = crossover(population, fitness_values)
        if offspring1 not in population or offspring2 not in population:
            population.extend([mutate(offspring1, factorAverages), mutate(offspring2, factorAverages)])
        #collecting fitness values.
        fitness_values = [fitness(genome, Actuals) for genome in population]
        #for fitness_v in fitness_values:
        #    print(fitness_v)
        best_fitness = min(fitness_values)
        print(f"{generation}:Best Fitness = {best_fitness}")
    #best found genomes
    best_index = fitness_values.index(min(fitness_values))
    best_solution = population[best_index]
    print(f'Best Solution: {best_solution}')
    print(f'Best fitness: {fitness(best_solution, Actuals)}')

genetic_algorithm()
