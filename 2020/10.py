from collections import defaultdict


def solve_a(l: list) -> int:
    """Return differences of 1 jolt x diff of 3 jolts"""
    i = 0
    ones, threes = 0, 0
    s = set(l)
    max_val = max(s) + 3
    s.add(max_val)
    while i < max_val:
        if i + 1 in s:
            ones += 1
            i += 1
        elif i + 2 in s:
            i += 2
        elif i + 3 in s:
            i += 3
            threes += 1

    return ones * threes


def solve_b(l: list, val: int=-1) -> int:
    """Return total number of arrangements possible"""
    d = defaultdict(int)
    l.sort()
    d[0] = 1
    for x in l:
        d[x] = d[x - 1] + d[x - 2] + d[x - 3]

    return d[l[-1]]


if __name__ == '__main__':
    input = [int(x) for x in open("10.txt").read().split("\n")]
    print(solve_a(input))
    print(solve_b(input))
