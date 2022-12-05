def solve_a(rows):
    overlaps = 0
    for i in range(len(rows)):
        a, b = rows[i].strip().split(",")
        [a, b], [c, d] = list(map(int, a.split("-"))), list(map(int, b.split("-")))
        overlaps += (a <= c and b >= d) or (c <= a and d >= b)

    return overlaps


def solve_b(rows):
    overlaps = 0
    for i in range(len(rows)):
        a, b = rows[i].strip().split(",")
        [a, b], [c, d] = list(map(int, a.split("-"))), list(map(int, b.split("-")))
        overlaps += (a <= c <= b) or (c <= b <= d) or (a <= d <= b) or (c <= a <= d)

    return overlaps


if __name__ == '__main__':
    rows = open("4.txt").readlines()
    print(solve_a(rows))
    print(solve_b(rows))