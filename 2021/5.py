from collections import defaultdict

def solve_a(input: list) -> int:
    """Return number of values >=2 in matrix"""
    n = 1000
    m = [[0] * n for x in range(n)]

    def search(m, x1, x2, y1, y2, y=False):
        """Find values and put them in the dict"""
        if x1 == x2:
            if y2 < y1:
                y1, y2 = y2, y1
            for y in range(y1, y2 + 1):
                m[y][x1] += 1
        elif y1 == y2:
            if x2 < x1:
                x1, x2 = x2, x1
            for x in range(x1, x2 + 1):
                m[y1][x] += 1
        return m

    for points in input:
        x1, y1 = (int(x) for x in points[0].split(","))
        x2, y2 = (int(x)for x in points[1].split(","))
        # print(x1, y1, x2, y2)
        m = search(m, x1, x2, y1, y2)
        # m = search(m, y1, y2, x1, x2)

    total = 0
    for row in m:
        for column in row:
            if column >= 2:
                total += 1

    return total


if __name__ == '__main__':
    input = [x.split(" ->") for x in open("5.txt").read().split("\n")]
    # print(input)
    print(solve_a(input))
