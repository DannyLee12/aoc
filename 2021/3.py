from collections import defaultdict

def inverse(number: str) -> str:
    """Return a 1s compliment of a number"""
    d = {'0': '1', '1': '0'}
    s = ""
    for x in number:
        s += d[x]

    return s


def solve_a(input, part_b=False):
    """Return most and least common bits multiplied together"""
    n = len(input[0])
    m = len(input)//2 if len(input) % 2 == 0 else len(input)//2 + 1
    a = [0] * n
    for row in input:
        for i, char in enumerate(row):
            a[i] += int(char)

    b = "".join([str(int(x)//m) for x in a])

    if part_b:
        return b

    return int(b, 2) * int(inverse(b), 2)


def solve_b(input):
    """Keep values based on most common/least common criteria"""

    def get_most_common(input, pos, c02=False):
        d = defaultdict(int)
        for row in input:
            d[row[pos]] += 1
        if d['0'] == d['1']:
            return '1'
        if d['0'] > d['1']:
            return '0'
        else:
            return '1'

    def solve_o2(input, pos=0, c02=False):
        if len(input) == 1:
            return input[0]
        i = []
        val = get_most_common(input, pos, c02)
        for row in input:
            if not c02:
                if row[pos] == val:
                    i.append(row)
            else:
                if row[pos] != val:
                    i.append(row)
        return solve_o2(i, pos + 1, c02=c02)

    return int(solve_o2(input), 2) * int(solve_o2(input, c02=True), 2)


if __name__ == '__main__':
    input = open("3.txt").read().split("\n")
    print(solve_a(input))
    b = solve_a(input, True)
    print(solve_b(input))
