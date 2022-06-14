import random
from typing import List


def swap_mutate(chromosome, mutation_rate):

    new_chromosome = chromosome[:]

    for swapped in range(len(chromosome)):
        if random.random() < mutation_rate:
            swap_with = int(random.random() * len(chromosome))

            # swap genes
            new_chromosome[swapped], new_chromosome[swap_with] = (
                new_chromosome[swap_with],
                new_chromosome[swapped],
            )

    return new_chromosome


def flip_mutate(
    chromosome: List[str | float], mutation_rate: float
) -> List[str | float]:

    new_chromosome = chromosome[:]

    for swapped in range(len(chromosome)):
        if random.random() < mutation_rate:
            new_chromosome[swapped] ^= 1

    return new_chromosome
