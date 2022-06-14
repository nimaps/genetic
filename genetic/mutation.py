import random
from typing import List


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
