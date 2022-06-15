from genetic import Genetic
from genetic.encodings import Encoding
from genetic.utils import plot


class QuadraticGenetic(Genetic):
    def fitness(self, chromosome):
        num = 0
        for bit in chromosome:
            num = (num << 1) | bit
        return (num**2) / 65500


def main():

    population_size = 30
    elitism_size = 6
    mutation_rate = 0.005
    generations_count = 12

    genetic = QuadraticGenetic(
        population_size,
        elitism_size,
        mutation_rate,
        generations_count,
        Encoding.BINARY,
        chromosome_size=8,
    )

    best = genetic.get_best_solution()

    print("Solution:")
    print(best)

    plot(genetic.progress, change=lambda i: 1 / i)


if __name__ == "__main__":
    main()
