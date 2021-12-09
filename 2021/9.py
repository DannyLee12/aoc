def solve_a(input: list, b: bool=False) -> int:
    """Return the sum of local mins"""
    l_mins = []
    n, m = len(input), len(input[0])

    def solve_b(input: list, i: int, j: int, visited: set=None) -> int:
        """Return the size of a local basin"""
        total = 1
        if not visited:
            visited = set()
        for (x, y) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if i+x >= 0 and i + x < n and j+y >= 0 and j + y < m:
                if input[i+x][j+y] == '9':
                    continue
                if int(input[i+x][j+y]) > int(input[i][j]):
                    if (i+x, j + y) not in visited:
                        visited.add((i+x, j +y))
                        total += solve_b(input, i+x, j+y, visited)

        return total

    total_b = []
    for i, row in enumerate(input):
        for j, _ in enumerate(row):
            l_min = True
            for (x, y) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    if i+x >= 0 and i + x < n and j+y >= 0 and j + y < m:
                        if input[i][j] >= input[i+x][j+y]:
                            l_min = False
                            break
            if l_min:
                l_mins.append(input[i][j])
                total_b.append(solve_b(input, i, j))
    if b:
        total = 1
        total_b.sort()
        for x in total_b[-3:]:
            total *= x
        return total
    return sum(map(int, l_mins)) + len(l_mins)


if __name__ == '__main__':
    input = open("9.txt").read().split("\n")
    print(solve_a(input))
    print(solve_a(input, True))
