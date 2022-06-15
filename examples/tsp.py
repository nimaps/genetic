import math
import random
from typing import Tuple

from genetic import Genetic
from genetic.encodings import Encoding
from genetic.utils import plot


def distance(point_a: Tuple[float, float], point_b: Tuple[float, float]):

    x_dis = abs(point_a[0] - point_b[0])
    y_dis = abs(point_a[1] - point_b[1])
    distance = math.sqrt((x_dis**2) + (y_dis**2))
    return distance


class TSPGenetic(Genetic):
    def fitness(self, chromosome):

        path_distance = 0
        size = len(chromosome)

        for i in range(size):

            from_city = chromosome[i]

            if i + 1 < size:
                to_city = chromosome[i + 1]
            else:
                to_city = chromosome[0]

            path_distance += distance(from_city, to_city)

        return 1 / path_distance


def main():

    population = []

    # read cities from file
    with open("./tsp.txt", mode="r") as stream:
        while city := stream.readline():
            idx, x, y = (int(num) for num in city.split(" "))
            population.append((x, y, idx))

    random.shuffle(population)

    population_size = 1000
    elitism_size = 90
    mutation_rate = 0.01
    generations_count = 500

    genetic = TSPGenetic(
        population_size,
        elitism_size,
        mutation_rate,
        generations_count,
        Encoding.PERMUTATION,
        population=population,
    )

    best_route = genetic.get_best_solution()

    print("Solution: (These are indexes given from file)")
    print([idx for _, _, idx in best_route])
    print(f"distance: {int(1 / genetic.fitness(best_route))}")

    plot(genetic.progress, change=lambda i: 1 / i)


if __name__ == "__main__":
    main()
