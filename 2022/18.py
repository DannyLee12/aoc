from collections import deque
from functools import cache

dirs = [[0, 0, -1], [0, 0, 1], [0, -1, 0], [0, 1, 0], [1, 0, 0], [-1, 0, 0]]


def solve_a(blocks):
    total = 0
    for i, j, k in blocks:
        for x, y, z in dirs:
            if (i + x, y + j, k + z) not in blocks:
                total += 1

    return total


def solve_b(blocks, max_x, max_y, max_z):
    total = 0

    @cache
    def is_trapped(a, b, c):

        q = deque([(a, b, c)])
        visited = set()

        while q:
            a, b, c = q.popleft()
            if (a, b, c) not in visited:
                visited.add((a, b, c))
                if 0 <= a <= max_x and 0 <= b <= max_y and 0 <= c <= max_z:
                    for x, y, z in dirs:
                        if (a + x, b + y, c + z) not in blocks:
                            q.append((a + x, b + y, c + z))
                else:
                    return False

        return True

    for i, j, k in blocks:
        for x, y, z in dirs:
            if (i + x, y + j, k + z) not in blocks and not is_trapped(i + x, y + j, k + z):
                total += 1

    return total


if __name__ == '__main__':
    blocks = set([tuple(map(int, x.split(','))) for x in open("18.txt").read().split("\n")])
    print(solve_a(blocks))
    max_x = max([x[0] for x in blocks])
    max_y = max([x[1] for x in blocks])
    max_z = max([x[2] for x in blocks])
    print(solve_b(blocks, max_x, max_y, max_z))
