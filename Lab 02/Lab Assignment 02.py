import numpy as np

def fitness(population, n):
    fitness = []

    for i in population:
        total = 0
        for j in range(n):
            if i[j] == 1:
                type_of_transaction = transactions[j].split()[0]
                amount_of_transaction = int(transactions[j].split()[1])
                if type_of_transaction == "d":
                    total = total + amount_of_transaction
                else:
                    total = total - amount_of_transaction

        fitness.append(abs(total))

    return fitness

def select(population, fit):
    weight = [i / np.sum(fit) for i in fit]
    selection1, selection2 = np.random.choice(len(population), 2, weight)

    return population[selection1], population[selection2]

def crossover(x, y):
    crossover_point = np.random.randint(0, n)
    child = np.concatenate((x[:crossover_point], y[crossover_point:]))

    return child

def mutate(child):
    gene_index = np.random.randint(0, len(child))

    if child[gene_index] == 0:
        child[gene_index] = 1
    else:
        child[gene_index] = 0

    return child

def GA(population, n, mutation_threshold):
    limit = 1000

    for i in range(limit):
        temp_population = []
        fit = fitness(population, n)
        for j in range(len(population)):
            x, y = select(population, fit)
            child = crossover(x, y)

            if (np.random.random()) < mutation_threshold:
                child = mutate(child)

            if all(k == 0 for k in child):
                temp_population.append(child)
                continue

            if fitness([child], n)[0] == 0:
                result = ''
                for i in child:
                    result = result + str(i)
                return result

            temp_population.append(child)
        population = temp_population
    return -1

transactions = []
with open("input1.txt") as f:
    n = int(f.readline())
    for i in range(1, n + 1):
        line = f.readline()[:-1]
        transactions.append(line)

initial_population = 16
mutation_threshold = 0.5
population = np.random.randint(0, 2, (initial_population, n))

print(GA(population, n, mutation_threshold))