DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
import numpy as np

def solve_a(input: list) -> int:
    """Find the cheapest way through the map"""
    n = len(input)
    visited = set()
    cost = [[float("inf")] * n for _ in range(n)]
    cost[0][0] = 0
    q = [(0, 0)]
    for _ in range(10):
        for i in range(n):
            for j in range(n):
                if i == j == 0:
                    continue
                cost[i][j] = input[i][j] + min(cost[x+i][y+j] for x,y in DIRS if 0<= x+i < n and 0 <= y+j < n)

    return cost[-1][-1]


if __name__ == '__main__':
    input = [list(map(int, list(x))) for x in open("15.txt").read().split('\n')]

    points = np.array(input)
    new_input = list(np.vstack([
        np.hstack([
            (points + i + j) - 9 * ((points + i + j) > 9)
            for i in range(5)
        ])
        for j in range(5)
    ]))

    print(solve_a(new_input))
    print(solve_a(input))

    # print(new_input)
