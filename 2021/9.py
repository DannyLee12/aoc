def solve_a(l: list) -> int:
    """Return first number not in sum of the 25 previous nnumbers"""
    s = set()
    c = []
    for val in l:
        if len(c) < 25:
            s.add(int(val))
            c.append(int(val))
        else:
            valid = False
            for i in c:
                if int(val) - i in s:
                    val_to_pop = c.pop(0)
                    s.remove(val_to_pop)
                    c.append(int(val))
                    s.add(int(val))
                    valid = True
                    break
            if not valid:
                return val


def solve_b(l: list, i: int) -> int:
    """Find a sequence of numbers that adds to i"""
    low, high = 0, 1
    sum_ = sum(l[low:high])
    while sum_ != i:
        if low == high:
            high += 1
        elif sum_ < i:
            high += 1
        else:
            low += 1
        sum_ = sum(l[low:high])

    return min(l[low:high]) + max(l[low:high])


if __name__ == '__main__':
    input = [int(x) for x in open("9.txt").read().split("\n")]

    print(solve_b(input, solve_a(input)))
