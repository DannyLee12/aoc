from functools import reduce
l = []

with open("3.txt") as f:
    for k, row in enumerate(f):
        l.append([])
        # read the row into the list 100 times
        for i in range(100):
            l[k].extend([x for x in row if x != '\n'])


def solve_a(l: list, route: (int, int)) -> int:
    """
    Solve part a
    move 3right, 1down and count trees (#s)
    """
    trees = 0
    # (vertical, horizonal)
    pos = (0, 0)
    n = len(l)
    while pos[0] < n - 1:
        pos = pos[0] + route[0], pos[1] + route[1]
        if l[pos[0]][pos[1]] == "#":
            trees += 1

    return trees


def solve_b():
    """Solve for various paths through the trees"""
    routes = ((1, 1), (1, 3), (1, 5), (1, 7), (2, 1))
    totals = []
    for route in routes:
        totals.append(solve_a(l, route))

    v = 1

    print(reduce(lambda x, y: x * y, totals))


if __name__ == '__main__':
    print(solve_a(l, (1, 3)))
    solve_b()
