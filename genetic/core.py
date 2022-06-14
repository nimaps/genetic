import random
from typing import List

from .encodings import Encoding
from .utils import cumulative_sum


def create_random_permutation(gene_list):
    chromosome = random.sample(gene_list, len(gene_list))
    return chromosome


def create_random_byte_array(chromosome_size: int):
    num = random.randint(0, (2**chromosome_size) - 1)
    chromosome = [int(gene) for gene in format(num, f"0{chromosome_size}b")]
    return chromosome


def initial_population(
    population_size: int, gene_list: List[str | float] = None, chromosome_size: int = 0
):
    if gene_list:
        return [create_random_permutation(gene_list) for _ in range(population_size)]

    if chromosome_size is None:
        raise ValueError

    return [
        create_random_byte_array(chromosome_size=chromosome_size)
        for _ in range(population_size)
    ]


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


def ordered_crossover(parent1, parent2):
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


def one_point_crossover(parent1, parent2):
    crossover_point = int(random.random() * len(parent1))
    return parent1[:crossover_point] + parent2[crossover_point:]


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


class Genetic:
    def __init__(
        self,
        population_size,
        elitism_size,
        mutation_rate,
        generations_count,
        encoding: Encoding,
        population=None,
        chromosome_size: int = None,
    ) -> None:
        self.population = population
        self.population_size = population_size
        self.elitism_size = elitism_size
        self.mutation_rate = mutation_rate
        self.generations_count = generations_count
        self.encoding = encoding
        self.chromosome_size = chromosome_size

        if self.encoding == Encoding.PERMUTATION:
            self.mutate_chromosome = swap_mutate
            self.crossover = ordered_crossover
        elif self.encoding == Encoding.BINARY:
            self.mutate_chromosome = flip_mutate
            self.crossover = one_point_crossover
        else:
            raise NotImplementedError

    def get_best_solution(self):

        if self.encoding == Encoding.PERMUTATION:
            pop = initial_population(self.population_size, gene_list=self.population)
        elif self.encoding == Encoding.BINARY:
            pop = initial_population(
                self.population_size, chromosome_size=self.chromosome_size
            )

        for _ in range(0, self.generations_count):
            pop = self.next_generation(pop, self.elitism_size, self.mutation_rate)

        best_solution_index = self.rank_chromosomes(pop)[0][0]
        best_chromosome = pop[best_solution_index]
        return best_chromosome

    def rank_chromosomes(self, population):
        fitness_results = {}
        for i in range(len(population)):
            fitness_results[i] = self.fitness(population[i])
        return sorted(fitness_results.items(), key=lambda x: x[1], reverse=True)

    def next_generation(self, current_gen, elite_count, mutation_rate):
        population_ranked = self.rank_chromosomes(current_gen)
        selection_results = selection(population_ranked, elite_count)
        pool = get_mating_pool(current_gen, selection_results)
        children = self.breed_population(pool, elite_count)
        next_generations = self.mutate_population(children, mutation_rate)
        return next_generations

    def mutate_population(self, population, mutation_rate):
        return [
            self.mutate_chromosome(chromosome, mutation_rate)
            for chromosome in population
        ]

    def breed_population(self, mating_pool, elite_count):
        children = []
        length = len(mating_pool) - elite_count
        pool = random.sample(mating_pool, len(mating_pool))

        for i in range(elite_count):
            children.append(mating_pool[i])

        for i in range(length):
            child = self.crossover(pool[i], pool[len(mating_pool) - i - 1])
            children.append(child)
        return children

    def fitness(self, chromosome) -> float:
        raise NotImplementedError
