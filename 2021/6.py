from collections import defaultdict

def solve_a(input: list, days: int) -> int:
    """Return the number of fish on day days"""
    l = input[:]
    while days:
        for i, x in enumerate(l):
            if l[i] == 0:
                l.append(9)
                l[i] = 6
            else:
                l[i] -= 1
        days -= 1

    return len(l)


def solve_b(input: list, days: int) -> int:
    """Record the number of fish at each stage"""
    d = defaultdict(int)
    for x in range(10):
        d[x] = 0
    for x in input:
        d[x] += 1

    for _ in range(days):

        for k in d.keys():
            if k == 0:
                d[9] += d[k]
                d[7] += d[k]
                d[k] = 0
            else:
                d[k - 1] += d[k]
                d[k] = 0

    total = 0
    for v in d.values():
        total += v

    return total


if __name__ == '__main__':
    input = [int(x) for x in open("6.txt").read().split(",")]
    input = list(map(int, open("6.txt").read().split(",")))
    print(input)
    print(solve_a(input, 80))
    print(solve_b(input, 256))
