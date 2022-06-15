from typing import Callable, List

import matplotlib.pyplot as plt


def cumulative_sum(array: List[float]) -> List[float]:
    for i in range(1, len(array)):
        array[i] += array[i - 1]
    return array


def plot(
    progress,
    change: Callable = None,
    xlabel: str = "Generation",
    ylabel: str = "Fitness",
):
    if change:
        progress = [change(item) for item in progress]
    plt.plot(progress)
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.show()
