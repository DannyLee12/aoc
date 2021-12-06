from collections import defaultdict

def solve(input: list) -> int:
    """Return number of values >=2 in matrix"""
    n = 1000
    m = [[0] * n for _ in range(n)]

    for points in input:
        x1, y1 = (int(x) for x in points[0].split(","))
        x2, y2 = (int(x) for x in points[1].split(","))
        m = search(m, x1, x2, y1, y2)

    total = 0
    for row in m:
        for column in row:
            if column >= 2:
                total += 1

    return total


def search(m, x1, x2, y1, y2, y=False):
    """Find values and put them in the dict"""
    if x1 == x2:
        y1, y2 = swap(y1, y2)
        for y in range(y1, y2 + 1):
            m[y][x1] += 1
    elif y1 == y2:
        x1, x2 = swap(x1, x2)
        for x in range(x1, x2 + 1):
            m[y1][x] += 1
    elif abs(y2 - y1) == abs(x2 - x1):
        dx = -1 if x2 < x1 else 1
        dy = -1 if y2 < y1 else 1
        x = x1
        i = 0
        while x != x2:
            x = x1 + dx * i
            m[y1 + dy * i][x] += 1
            i += 1

    return m


def swap(y1, y2):
    if y2 < y1:
        y1, y2 = y2, y1
    return y1, y2


if __name__ == '__main__':
    input = [x.split(" ->") for x in open("5.txt").read().split("\n")]
    print(solve(input))
