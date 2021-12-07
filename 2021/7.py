from functools import lru_cache
from statistics import mean


def solve(input: list) -> int:
    """Determine the value that requires the fewest moves"""
    m = int(mean(input))
    min_total = float("inf")

    @lru_cache
    def cache(n: int) -> int:
        total = 0
        for i, x in enumerate(range(n)):
            total += 1 + i
        return total

    for x in range(m-10, m+10):
        total = 0
        for i in input:
            total += cache(abs(x - i))
        min_total = min(min_total, total)

    return min_total


if __name__ == '__main__':
    input = list(map(int, open("7.txt").read().split(",")))
    print(solve(input))
