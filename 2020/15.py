from collections import defaultdict


def solve_a(l: list) -> int:
    """Return the 2020th number in a sequence"""
    d = defaultdict(list)
    for i in range(len(l) - 1):
        d[l[i]].append(i)
    val = l.pop()
    while i < 2018:
        l.append(val)
        prev_val = val
        if l[-1] == l[-2]:
            val = 1
        elif val not in d:
            val = 0
        else:
            val = i + 1 - d[val][-1]
        d[prev_val].append(i+1)

        i += 1

    return val


def solve_b(l: list) -> int:
    """Return the 30000000th number in a sequence"""
    d = defaultdict(list)
    for i in range(len(l) - 1):
        d[l[i]].append(i)
    val = l.pop()
    while i < 30000000 - 2:
        l.append(val)
        prev_val = val
        if l[-1] == l[-2]:
            val = 1
        elif val not in d:
            val = 0
        else:
            val = i + 1 - d[val][-1]
        d[prev_val].append(i+1)

        i += 1

    return val


if __name__ == '__main__':
    assert solve_a([0, 3, 6]) == 436
    assert solve_a([1,3,2]) == 1
    assert solve_a([2,1,3]) == 10
    assert solve_a([1,2,3]) == 27
    assert solve_a([2,3,1]) == 78
    assert solve_a([3,2,1]) == 438
    assert solve_a([3,1,2]) == 1836
    print(solve_a([1,17,0,10,18,11,6]))
    print(solve_b([1,17,0,10,18,11,6]))
