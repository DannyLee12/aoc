dirs = [[0, 0, -1], [0, 0, 1], [0, -1, 0], [0, 1, 0], [1, 0, 0], [-1, 0, 0]]
print(dirs)

def solve_a(blocks):
    total = 0
    for i, j, k in blocks:
        for x, y, z in dirs:
            if (i + x, y + j, k + z) not in blocks:
                total += 1

    return total


if __name__ == '__main__':
    blocks = set([tuple(map(int, x.split(','))) for x in open("18.txt").read().split("\n")])
    print(solve_a(blocks))
