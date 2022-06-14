
# Genetic Algorithm Framework

GAF is a Modern 🤖 Fast ⚡ Easy-to-use 🧀 flexible 🥳 Genetic Algorithm Framework.

## Installation

Make sure you have `poetry` installed. you can install it using pip:
```bash
pip install poetry
```

then install the project using `poetry`:

```bash
poetry install
```

Now you can easily import the library in your python modules:

```python
import genetic
```


## Running Tests

To run tests, first make sure you have pytest installed, then run the following command

```bash
python -m pytest
```


## Usage/Examples

In order to use the library, you need to extend the `Genetic` class and define your fitness function.

For a simple example I solve the nqueens problem using the following snippet:
```python
from genetic import Genetic
from genetic.encodings import Encoding

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

```

Now inside my main function, I determine my parameters:

```python
genetic = QueensGenetic(
    population_size,
    elitism_size,
    mutation_rate,
    generations_count,
    Encoding.PERMUTATION,
    population,
)

best = genetic.get_best_solution()
```
It's that easy!!
## License

[MIT](https://choosealicense.com/licenses/mit/)

## Authors

- [@nimaps](https://www.github.com/nimaps)
