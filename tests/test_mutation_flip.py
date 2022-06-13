from unittest import TestCase

from genetic.core import flip_mutate


class TestMutation(TestCase):
    def test_always_mutate(self):
        chromosome = [0, 0, 1, 0, 1, 1, 1, 0, 1]
        chromosome_mutated = flip_mutate(chromosome, mutation_rate=1)
        self.assertFalse(chromosome == chromosome_mutated)

    def test_never_mutate(self):
        chromosome = [0, 0, 1, 0, 1, 1, 1, 0, 1]
        chromosome_mutated = flip_mutate(chromosome, mutation_rate=0)
        self.assertTrue(chromosome == chromosome_mutated)
