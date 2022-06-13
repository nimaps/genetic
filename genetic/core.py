import random
from typing import List

from .encodings import Encoding
from .utils import cumulative_sum


def create_random_chromosome(gene_list):
    chromosome = random.sample(gene_list, len(gene_list))
    return chromosome


def initial_population(population_size: int, gene_list):
    return [create_random_chromosome(gene_list) for _ in range(population_size)]


def selection(population_ranked, elitism_size):
    selection_results = []

    fitness_array = [a[1] for a in population_ranked]
    fitness_sum = sum(fitness_array)
    cum_sum = cumulative_sum(fitness_array)
    cumulative_percentage = [100 * i / fitness_sum for i in cum_sum]

    for i in range(elitism_size):
        selection_results.append(population_ranked[i][0])

    for i in range(len(population_ranked) - elitism_size):

        pick = 100 * random.random()

        for i in range(len(population_ranked)):
            if pick <= cumulative_percentage[i]:
                selection_results.append(population_ranked[i][0])
                break

    return selection_results


def get_mating_pool(population, selection_results):
    pool = []
    for i in range(len(selection_results)):
        index = selection_results[i]
        pool.append(population[index])
    return pool


def breed(parent1, parent2):
    child = []
    child_p1 = []
    child_p2 = []

    gene_a = int(random.random() * len(parent1))
    gene_b = int(random.random() * len(parent1))

    start_gene = min(gene_a, gene_b)
    end_gene = max(gene_a, gene_b)

    for i in range(start_gene, end_gene):
        child_p1.append(parent1[i])

    child_p2 = [item for item in parent2 if item not in child_p1]

    child = child_p2[:start_gene] + child_p1 + child_p2[start_gene:]
    return child


def breed_population(mating_pool, elite_count):
    children = []
    length = len(mating_pool) - elite_count
    pool = random.sample(mating_pool, len(mating_pool))

    for i in range(elite_count):
        children.append(mating_pool[i])

    for i in range(length):
        child = breed(pool[i], pool[len(mating_pool) - i - 1])
        children.append(child)
    return children


def swap_mutate(chromosome, mutation_rate):

    new_chromosome = chromosome[:]

    if random.random() < mutation_rate:
        swapped, swap_with = 1, 1
        while swapped == swap_with:
            swapped = int(random.random() * len(chromosome))
            swap_with = int(random.random() * len(chromosome))
        new_chromosome[swap_with], new_chromosome[swapped] = (
            new_chromosome[swapped],
            new_chromosome[swap_with],
        )
    return new_chromosome


def flip_mutate(
    chromosome: List[str | float], mutation_rate: float
) -> List[str | float]:

    new_chromosome = chromosome[:]

    if random.random() < mutation_rate:
        swapped = int(random.random() * len(chromosome))
        new_chromosome[swapped] ^= 1
    return new_chromosome


def mutate_population(population, mutation_rate):
    return [swap_mutate(chromosome, mutation_rate) for chromosome in population]


class Genetic:
    def __init__(
        self,
        population,
        population_size,
        elitism_size,
        mutation_rate,
        generations_count,
        encoding: Encoding,
    ) -> None:
        self.population = population
        self.population_size = population_size
        self.elitism_size = elitism_size
        self.mutation_rate = mutation_rate
        self.generations_count = generations_count
        self.encoding = encoding

        if self.encoding == Encoding.PERMUTATION:
            self.mutate_chromosome = swap_mutate
        elif self.encoding == Encoding.BINARY:
            self.mutate_chromosome = flip_mutate
        else:
            raise NotImplementedError

    def get_best_solution(self):
        pop = initial_population(self.population_size, self.population)
        print("Initial distance: " + str(1 / self.rank_chromosomes(pop)[0][1]))

        for _ in range(0, self.generations_count):
            pop = self.next_generation(pop, self.elitism_size, self.mutation_rate)

        print("Final distance: " + str(1 / self.rank_chromosomes(pop)[0][1]))
        best_route_index = self.rank_chromosomes(pop)[0][0]
        best_route = pop[best_route_index]
        return best_route

    def rank_chromosomes(self, population):
        fitness_results = {}
        for i in range(0, len(population)):
            fitness_results[i] = self.fitness(population[i])
        return sorted(fitness_results.items(), key=lambda x: x[1], reverse=True)

    def next_generation(self, current_gen, elite_count, mutation_rate):
        population_ranked = self.rank_chromosomes(current_gen)
        selection_results = selection(population_ranked, elite_count)
        pool = get_mating_pool(current_gen, selection_results)
        children = breed_population(pool, elite_count)
        next_generations = mutate_population(children, mutation_rate)
        return next_generations

    def fitness(self, chromosome) -> float:
        raise NotImplementedError
