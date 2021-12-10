from statistics import median

pens = {")": 3, "]": 57, "}": 1197, ">": 25137}
vals = {")": 1, "]": 2, "}": 3, ">": 4}
opens = "([{<"
closes = ")]}>"


def solve_a(input: list) -> int:
    """Return the sum of the first invalid chars"""
    total = 0
    total_incomplete = []
    for row in input:
        stack = []
        corrupt = False
        for x in row:
            if x in opens:
                stack.append(x)
            elif x in closes:
                # find opens val to pop
                i = closes.index(x)
                if stack[-1] == opens[i]:
                    stack.pop()
                else:
                    total += pens[x]
                    corrupt = True
                    break
        if not corrupt:
            val = 0
            for item in stack[::-1]:
                i = opens.index(item)
                val *= 5
                val += vals[closes[i]]
            total_incomplete.append(val)

    return total, median(total_incomplete)


if __name__ == '__main__':
    input = open("10.txt").read().split("\n")

    print(solve_a(input))