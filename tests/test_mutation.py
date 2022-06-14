from unittest import TestCase

from genetic.mutation import flip_mutate, swap_mutate


class TestSwapMutation(TestCase):
    def test_always_mutate(self):
        chromosome = [1, 2, 3, 4, 5, 6]
        chromosome_mutated = swap_mutate(chromosome, mutation_rate=1)
        self.assertFalse(chromosome == chromosome_mutated)

    def test_never_mutate(self):
        chromosome = [1, 2, 3, 4, 5, 6]
        chromosome_mutated = swap_mutate(chromosome, mutation_rate=0)
        self.assertTrue(chromosome == chromosome_mutated)


class TestFlipMutation(TestCase):
    def test_always_mutate(self):
        chromosome = [0, 0, 1, 0, 1, 1, 1, 0, 1]
        chromosome_mutated = flip_mutate(chromosome, mutation_rate=1)
        self.assertFalse(chromosome == chromosome_mutated)

    def test_never_mutate(self):
        chromosome = [0, 0, 1, 0, 1, 1, 1, 0, 1]
        chromosome_mutated = flip_mutate(chromosome, mutation_rate=0)
        self.assertTrue(chromosome == chromosome_mutated)
