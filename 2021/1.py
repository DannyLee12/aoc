
rows = open("1.txt").readlines()


def part_a():
    """Calculate which values in a list are increasing"""
    total = 0
    for i, srow in enumerate(rows):

        row = int(srow.strip())
        if i == 0:
            val = row
            continue

        total += row > val
        val = row

    print(total)


def part_b():
    """calculate which values of 3 values are increasing"""
    total = 0
    n = len(rows)
    for i in range(n - 2):

        if i == 0:
            val = int(rows[0]) + int(rows[1]) + int(rows[2])
            continue

        total += (int(rows[i]) + int(rows[i + 1]) + int(rows[i + 2])) > val
        val = int(rows[i]) + int(rows[i + 1]) + int(rows[i + 2])

        # print(val)

    print(total)


if __name__ == '__main__':
    part_a()
    part_b()
