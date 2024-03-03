import numpy as np
import random

# RL Parameters
num_states = 4  # Assuming each zone represents a unique state
num_actions = 3  # Actions: 0 = attack, 1 = defend, 2 = move resources
Q_table = np.zeros((num_states, num_actions))
alpha = 0.1
gamma = 0.99
epsilon = 0.1

# GA Parameters
population_size = 10
num_generations = 50
mutation_rate = 0.1
num_zones = 4

def choose_action(state):
    if random.uniform(0, 1) < epsilon:
        return random.randint(0, num_actions - 1)
    return np.argmax(Q_table[state])

def update_q_table(state, action, reward, next_state):
    q_predict = Q_table[state, action]
    q_target = reward + gamma * np.max(Q_table[next_state])
    Q_table[state, action] += alpha * (q_target - q_predict)

def learn_from_historical_battles(battles, zones):
    zone_to_state = {zone["Zone ID"]: idx for idx, zone in enumerate(zones)}
    for battle in battles:
        state = zone_to_state[battle['Zone ID']]
        action = choose_action(state)
        reward = 10 if battle['Outcome'] == 'Win' else -10
        next_state = (state + 1) % num_states
        update_q_table(state, action, reward, next_state)

def initialize_population(faction_forces):
    # Assuming you're spreading faction forces evenly across zones
    total_forces = sum(faction_forces.values())
    avg_force_per_zone = total_forces // num_zones
    return [[random.randint(0, avg_force_per_zone) for _ in range(num_zones)] for _ in range(population_size)]

def evaluate_fitness(individual, zones):
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
            parent1, parent2 = [p[0] for p in random.sample(parents, 2)]
            offspring1, offspring2 = crossover(parent1, parent2)
            next_generation += [mutate(offspring1), mutate(offspring2)]
        population = next_generation
    best_solution = max(population, key=lambda ind: evaluate_fitness(ind, zones))
    print(f"Best Solution: {best_solution}, Fitness: {evaluate_fitness(best_solution, zones)}")
