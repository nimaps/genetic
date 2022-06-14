import random


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
