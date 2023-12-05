from collections import defaultdict

SYMBOLS = "!@#$%^&*()_-+={}[]/"


def solve_b(rows):
    total = 0

    gear_map = defaultdict(list)

    def dfs(start, end, value):
        for x in range(start[0] - 1, end[0] + 2):
            for y in range(start[1] - 1, end[1] + 1):
                if 0 <= x < len(rows[0]) and 0 <= y < len(rows):
                    if rows[x][y] == '*':
                        gear_map[f"{x}_{y}"].append(value)
        return False

    for i, row in enumerate(rows):
        value = 0
        start, end = None, None
        for j, val in enumerate(row):
            if val.isdigit():
                value = value * 10 + int(val)
                if not start:
                    start = (i, j)
            if not val.isdigit() and start:
                end = (i, j)
                dfs(start, end, value)
                value = 0
                start, end = None, None
        end = i, j
        if start:
            dfs(start, end, value)

    for key, value in gear_map.items():
        if len(value) == 2:
            total += value[0] * value[1]

    return total

def solve_a(rows):
    value = 0

    def dfs(start, end):
        # above, below left + right
        for x in range(start[0] - 1, end[0] + 2):
            for y in range(start[1] - 1, end[1] + 1):
                if 0 <= x < len(rows[0]) and 0 <= y < len(rows):
                    if rows[x][y] in SYMBOLS:
                        return True
        return False

    total = 0
    for i, row in enumerate(rows):
        start, end = None, None
        for j, val in enumerate(row):
            if val.isdigit():
                value = (value * 10) + int(val)
                if not start:
                    start = (i, j)
            if not val.isdigit() and start:
                end = (i, j)
                if dfs(start, end):
                    total += value
                value = 0
                start, end = None, None
        end = (i, j)
        if start and dfs(start, end):
            total += value
        value = 0

    return total


if __name__ == '__main__':
    with open("3.txt") as f:
        rows = f.read().split('\n')

    print(solve_a(rows))
    print(solve_b(rows))
