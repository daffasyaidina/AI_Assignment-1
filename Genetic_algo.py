import random   

distance_matrix = {
    'Start': {'a': 12, 'b': 17, 'c': 10},
    'a': {'Start': 12, 'b': 12, 'c': 11, 'd': 10, 'e': 17},
    'b': {'Start': 17, 'a': 12, 'c': 9, 'd': 12, 'e': float('inf')}, 
    'c': {'Start': 10, 'a': 11, 'b': 9, 'd': 11, 'e': 12},
    'd': {'a': 10, 'b': 12, 'c': 11, 'e': 10},
    'e': {'a': 17, 'c': 12, 'd': 10}
}
cities = list(distance_matrix.keys())

def path_length(path, matrix):
    distance = 0
    for i in range(len(path) - 1):
        try:
            distance += matrix[path[i]][path[i+1]]
        except KeyError:
            print(f"Error with path: {path}")
            print(f"Trying to access matrix[{path[i]}][{path[i+1]}]")
            raise
    try:
        distance += matrix[path[-1]][path[0]]
    except KeyError:
        print(f"Error with path: {path}")
        print(f"Trying to access matrix[{path[-1]}][{path[0]}]")
        raise
    return distance

def crossover(parent1, parent2):
    start_index = random.randint(0, len(parent1)-2)
    end_index = random.randint(start_index, len(parent1)-1)

    child = [None]*len(parent1)
    child[start_index:end_index] = parent1[start_index:end_index]

    pointer = end_index
    for i in range(len(parent2)):
        if pointer == len(parent1):
            pointer = 0
        if parent2[i] not in child:
            child[pointer] = parent2[i]
            pointer += 1
    return child

def mutate(child):
    index1 = random.randint(0, len(child)-1)
    index2 = random.randint(0, len(child)-1)
    child[index1], child[index2] = child[index2], child[index1]
    return child

def make_matrix_symmetric(matrix):
    cities = list(matrix.keys())
    for city in cities:
        for destination, distance in matrix[city].items():
            matrix[destination][city] = distance
    return matrix

def genetic_algorithm(cities, matrix, population_size=100, generations=500, mutation_rate=0.05):
    population = [random.sample(cities[1:], len(cities)-1) for _ in range(population_size)]
    
    for generation in range(generations):
        population.sort(key=lambda x: path_length(['Start'] + x, matrix))
        
        new_population = []
        for i in range(0, population_size, 2):
            parent1 = population[i]
            parent2 = population[i+1]
            child1 = crossover(parent1, parent2)
            child2 = crossover(parent2, parent1)

            if random.random() < mutation_rate:
                child1 = mutate(child1)
            if random.random() < mutation_rate:
                child2 = mutate(child2)

            new_population.append(child1)
            new_population.append(child2)
        
        population = new_population

    best_path = population[0]
    best_distance = path_length(['Start'] + best_path, matrix)
    return best_path, best_distance

def complete_distance_matrix(matrix):
    cities = list(matrix.keys())
    for city1 in cities:
        for city2 in cities:
            if city2 not in matrix[city1]:
                matrix[city1][city2] = float('inf')
    return matrix

distance_matrix = complete_distance_matrix(distance_matrix)

best_path, best_distance = genetic_algorithm(cities, distance_matrix)

best_path_with_start = ['Start'] + best_path + ['Start']
print("Best Path:", best_path_with_start)
print("Best Distance:", best_distance)


