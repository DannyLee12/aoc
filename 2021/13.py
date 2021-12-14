def solve_a(map: list, instructions: list, b: bool=True) -> int:
    """Return the number of dots after one fold"""
    n = len(map)
    m = len(map[0])
    for instruction in instructions:
        ins = instruction.lstrip("fold along").split("=")
        if ins[0] == 'y':
            v = int(ins[-1])
            new_map = [["_"] * m for _ in range(v)]
            for i in range(n):
                for j in range(m):
                    if i < v:
                        new_map[i][j] = map[i][j]
                    elif i > v:
                        if map[i][j] == "#":
                            # pass
                            new_map[v*2 - i][j] = "#"
        elif ins[0] == 'x':
            v = int(ins[-1])
            new_map = [["_"] * v for _ in range(n)]
            for i in range(n):
                for j in range(m):
                    if j < v:
                        new_map[i][j] = map[i][j]
                    elif j > v:
                        if map[i][j] == "#":
                            # pass
                            new_map[i][v*2 - j] = "#"
        n = len(new_map)
        m = len(new_map[0])
        map = new_map[:]

        if not b:
            break

        total = 0
        for row in new_map:
            for element in row:
                total += element == "#"
        if not b:
            return total

    pprint = ""
    for row in new_map:
        pprint += "".join(row)

    print(pprint)
    m = ["".join(x) for x in new_map]

    return new_map


if __name__ == '__main__':
    dots_raw, instructions = open("13.txt").read().split('\n\n')
    dots = [["_"] * 1500 for x in range(1500)]
    for val in dots_raw.split('\n'):
        x, y = list(map(int, val.split(",")))
        dots[y][x] = "#"

    # print(solve_a(dots, instructions.split("\n")))
    print(solve_a(dots, instructions.split("\n")), True)
