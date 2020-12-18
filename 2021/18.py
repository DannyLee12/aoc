from functools import reduce


def solve_a(l: list) -> int:
    """Return Sum of all answers using funny maths"""
    def solve_small(l):
        for row in l:
            vals = row.split()
            while "(" in vals:
                pass
            total = 0
            one = True
            acc = None
            for x in vals:
                if one and x.isdigit():
                    acc = x
                    one = False
                elif x in ["*", "+", "-", "/"]:
                    operator = x
                elif not one and x.isdigit():
                    total = eval(f"{acc} {operator} {x}")
                    # one = True
                    acc = total

        return total

    def solve_b(s: str) -> int:
        """Addition first"""
        total = 1
        vals = s.split("*")
        for sum in vals:
            if "+" in sum:
                total *= eval(sum)
            else:

                total *= int(sum)

        return total

    total = 0
    nl = []
    for a, row in enumerate(l):
        nl.append(None)
        while "(" in row:
            depth = 0
            max_depth = 0
            start, end = -1, -1
            deepest = False
            for i, x in enumerate(row):
                if x == "(":
                    depth += 1
                    if depth > max_depth:
                        max_depth = depth
                        start = i
                        deepest = True
                elif x == ")":
                    depth -= 1
                    if deepest:
                        end = i
                        deepest = False
            nl[a] = (row[:start] + str(solve_b(row[start + 1:end])) + row[end + 1:])
            row = nl[a]
        total += solve_b(row)

    return total






if __name__ == '__main__':
    rows = open("18.txt").read().split("\n")
    print(solve_a(rows))