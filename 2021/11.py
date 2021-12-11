dirs = [(-1, -1), (-1, 0), (-1, 1),
        (0, -1), (0, 1),
        (1, -1), (1, 0), (1, 1)]


def solve_a(input: list, steps: int=2000) -> int:
    """Return total number of flashes"""
    flashes = 0
    n = len(input)
    for _ in range(steps):
        flashed = set()
        q = []
        sync = True
        for i in range(n):
            for j in range(n):
                if (i, j) not in flashed:
                    input[i][j] += 1
                if input[i][j] > 9:
                    flashes += 1
                    input[i][j] = 0
                    flashed.add((i, j))
                    q.append((i, j))
                    while q:
                        a, b = q.pop()
                        for x, y in dirs:
                            if 0 <= a + x < n and 0 <= b + y < n:
                                if (a+x, b+y) not in flashed:
                                    input[a+x][b+y] += 1
                                if input[a+x][b+y] > 9:
                                    flashes += 1
                                    flashed.add((a+x, b+y))
                                    q.append((a+x, b+y))
                                    input[a+x][b+y] = 0

        # Part B
        if len(flashed) == 100:
            return _ + 1

    return flashes


if __name__ == '__main__':
    input = [list(map(int, list(x))) for x in open("11.txt").read().split('\n')]
    print(solve_a(input))
