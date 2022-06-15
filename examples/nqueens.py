from genetic import Genetic
from genetic.encodings import Encoding
from genetic.utils import plot


class QueensGenetic(Genetic):
    def fitness(self, chromosome):

        size = len(chromosome)

        fitness = 0

        f1 = sorted([chromosome[i] - i for i in range(size)])
        f2 = sorted([chromosome[i] + i for i in range(size)])

        for i in range(1, size):
            if f1[i] == f1[i - 1]:
                fitness -= 1
            if f2[i] == f2[i - 1]:
                fitness -= 1

        return fitness


def main():

    n = 8
    population = [i for i in range(n)]
    population_size = 100
    elitism_size = 20
    mutation_rate = 0.005
    generations_count = 20

    genetic = QueensGenetic(
        population_size,
        elitism_size,
        mutation_rate,
        generations_count,
        Encoding.PERMUTATION,
        population,
    )

    best = genetic.get_best_solution()
    fitness = genetic.fitness(best)

    print("Solution: ")
    print(best)
    print(f"Fitness: {-fitness} (Zero means Best possible solution(no collisions)")

    plot(genetic.progress, change=lambda i: -i)


if __name__ == "__main__":
    main()
