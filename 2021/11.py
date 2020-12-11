import copy

directions = ((-1, -1), (-1, 0), (-1, 1),
              (0, -1), (0, 1),
              (1, -1), (1, 0), (1, 1))


def solve_a(l: list) -> int:
    """Return count # once map has stabilized"""
    nl = copy.deepcopy(l)
    n = len(l)
    m = len(l[0])
    i, j = 0, 0
    while i < n:
        if l[i][j] == "L":
            occupied = False
            for x, y in directions:
                if 0 <= i + x < n and 0 <= j + y < m:
                    if l[i+x][j+y] == "#":
                        occupied = True
                        break
            if not occupied:
                nl[i][j] = "#"
        elif l[i][j] == "#":
            counter = 0
            for x, y in directions:
                if 0 <= i + x < n and 0 <= j + y < m:
                    if l[i + x][j + y] == "#":
                        counter += 1
                if counter == 4:
                    nl[i][j] = "L"
                    break
        if j == m - 1:
            j = 0
            i += 1
        else:
            j += 1

    if nl == l:
        return sum(x.count("#") for x in ["".join(x) for x in nl])
    return solve_a(nl)


def solve_b(l: list) -> int:
    """Similar rules, but different rules"""
    nl = copy.deepcopy(l)
    n = len(l)
    m = len(l[0])
    i, j = 0, 0
    while i < n:
        if l[i][j] == "L":
            occupied = False
            for x, y in directions:
                a, b = 0, 0
                while 0 <= i + a + x < n and 0 <= j + b + y < m:
                    if l[i+a+x][j+b+y] == "#":
                        occupied = True
                        break
                    elif l[i + a + x][j + b + y] == "L":
                        break
                    a += x
                    b += y
            if not occupied:
                nl[i][j] = "#"
        elif l[i][j] == "#":
            counter = 0
            for x, y in directions:
                a, b = 0, 0
                while 0 <= i + a + x < n and 0 <= j + b + y < m:
                    if l[i + a + x][j + b + y] == "#":
                        counter += 1
                        break
                    elif l[i + a + x][j + b + y] == "L":
                        break
                    a += x
                    b += y
                if counter == 5:
                    nl[i][j] = "L"
                    break
        if j == m - 1:
            j = 0
            i += 1
        else:
            j += 1

    if nl == l:
        return sum(x.count("#") for x in ["".join(x) for x in nl])
    return solve_b(nl)


if __name__ == '__main__':
    input = [list(x) for x in open("11.txt").read().split("\n")]
    print(solve_a(input))
    print(solve_b(input))
