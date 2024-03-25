import numpy as np
import random

# RL Parameters
num_states = 4  # Assuming each zone represents a unique state
num_actions = 3  # Actions: 0 = attack, 1 = defend, 2 = move resources
Q_table = np.zeros((num_states, num_actions))
alpha = 0.1 # learning rate (to what extent newly acquired information overrides old information)
gamma = 0.99 # discount factor (to what extent future rewards are considered)
epsilon = 0.1 # exploration rate (to what extent to choose random action over greedy action)

# GA Parameters
population_size = 10 # refers to the number of individual solutions (in this case strategies or configurations) that will be considered at each step of the algorithm
num_generations = 50 # refers to the number of iterations the algorithm will run for. (A generation in a GA consists of creating a new set of solutions from the current set, usually by selecting the better solutions according to some fitness criteria, and then applying crossover and mutation to generate offspring)
mutation_rate = 0.1 # introduce variance in the population by randomly modifying the individuals
num_zones = 4 # Assuming 4 zones in the game

def choose_action(state):
    if random.uniform(0, 1) < epsilon: # Exploration vs Exploitation (sometimes choose a random action to explore the environment rather than exploit the current knowledge)
        return random.randint(0, num_actions - 1) # exploration (choose random action) (returns integer)
    return np.argmax(Q_table[state]) # exploitation (returns index)

def update_q_table(state, action, reward, next_state):
    q_predict = Q_table[state, action] # former q-value estimation
    q_target = reward + gamma * np.max(Q_table[next_state]) # TD target
    Q_table[state, action] += alpha * (q_target - q_predict) # TD error

def learn_from_historical_battles(battles, zones): # simulate learning from historical battles (update q_table based on historical data)
    zone_to_state = {zone["Zone ID"]: idx for idx, zone in enumerate(zones)} # map zone id to state
    for battle in battles:
        state = zone_to_state[battle['Zone ID']] # map zone id to state
        action = choose_action(state)
        reward = 10 if battle['Outcome'] == 'Win' else -10
        next_state = (state + 1) % num_states #
        update_q_table(state, action, reward, next_state) # update the q_table based on the outcome of the battle

def initialize_population(faction_forces):
    # Assuming you're spreading faction forces evenly across zones
    total_forces = sum(faction_forces.values()) # total forces available for a given faction
    avg_force_per_zone = total_forces // num_zones # even spread
    return [[random.randint(0, avg_force_per_zone) for _ in range(num_zones)] for _ in range(population_size)] # generate a population of random strategies (where to allocate forces) (example output: [[10, 20, 30, 40], [20, 30, 40, 50], ...] i.e. for strategy 1, allocate 10 forces to zone 1, 20 forces to zone 2, etc.)

def evaluate_fitness(individual, zones): # caculate fitness of a strategy (placement of forces)
    strategic_value_sum = sum(zone["Strategic Value"] for zone in zones)
    return sum(individual) + strategic_value_sum  # Simplified fitness calculation

def select_parents(population, zones):
    fitness_scores = [evaluate_fitness(individual, zones) for individual in population]
    sorted_population = sorted(zip(population, fitness_scores), key=lambda x: x[1], reverse=True)
    return [individual for individual, score in sorted_population[:len(population) // 2]]

def crossover(parent1, parent2):
    crossover_point = random.randint(1, num_zones - 1)
    return parent1[:crossover_point] + parent2[crossover_point:], parent2[:crossover_point] + parent1[crossover_point:]

def mutate(individual):
    if random.random() < mutation_rate:
        mutation_point = random.randint(0, num_zones - 1)
        individual[mutation_point] = random.randint(0, 100)
    return individual

def run_ga(zones, faction_forces):
    population = initialize_population(faction_forces)
    for generation in range(num_generations):
        parents = select_parents(population, zones)
        next_generation = []
        while len(next_generation) < population_size:
            parent1, parent2 = random.sample(parents, 2)
            offspring1, offspring2 = crossover(parent1, parent2)
            next_generation += [mutate(offspring1), mutate(offspring2)]
        population = next_generation
    best_solution = max(population, key=lambda ind: evaluate_fitness(ind, zones))
    print(f"Best Solution: {best_solution}, Fitness: {evaluate_fitness(best_solution, zones)}")
