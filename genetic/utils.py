from typing import List


def cumulative_sum(array: List[float]) -> List[float]:
    for i in range(1, len(array)):
        array[i] += array[i - 1]
    return array
