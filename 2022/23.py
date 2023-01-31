def solve_a(elves, steps=1000):
    dirs = ["N", "S", "W", "E"]
    total = 0
    moved = True
    while moved:
        moved = False
        proposed = {}
        moving = set()
        refused = set()
        for elf in elves:
            r, c = elf.split('_')
            r = int(r)
            c = int(c)
            # N
            for dir in dirs:
                propose(c, elf, elves, proposed, r, refused, dir, moving)
            # S

        dirs = dirs[1:] + [dirs[0]]

        for proposed_elf, current_elf in proposed.items():
            if proposed_elf not in refused:
                elves.remove(current_elf)
                elves.add(proposed_elf)
                moved = True

        total += 1
        steps -= 1
        if total % 10 == 0:
            print(total)

    return total
    # min_x, min_y, max_x, max_y = 100, 100, 0, 0
    # for elf in elves:
    #     x, y = elf.split('_')
    #     x, y = int(x), int(y)
    #     min_x, min_y = min(min_x, x), min(min_y, y)
    #     max_x, max_y = max(max_x, x), max(max_y, y)
    #
    # return (max_y - min_y + 1) * (max_x - min_x + 1) - len(elves)


def propose(c, elf, elves, proposed, r, refused, dir, moving):
    go = False
    if elf in moving:
        return
    # check any elves in the 8 positions
    for i, j in ([-1, -1], [-1, 0], [-1, 1],
                [0, -1],           [0, 1],
                [1, -1], [1, 0], [1, 1]):
        if f'{r + i}_{c + j}' in elves:
            go = True
            break
    if not go:
        return

    if dir == 'N':
        if not {f'{r - 1}_{c - 1}', f'{r - 1}_{c}',
                f'{r - 1}_{c + 1}'}.intersection(elves):
            if f'{r - 1}_{c}' in proposed:
                refused.add(f'{r - 1}_{c}')
            elif elf not in proposed:
                proposed[f'{r - 1}_{c}'] = elf
            moving.add(elf)

    elif dir == 'S':
        if not {f'{r + 1}_{c - 1}', f'{r + 1}_{c}', f'{r + 1}_{c + 1}'}.intersection(elves):
            if f'{r + 1}_{c}' in proposed:
                refused.add(f'{r + 1}_{c}')
            elif elf not in proposed:
                proposed[f'{r + 1}_{c}'] = elf
            moving.add(elf)

    elif dir == 'W':
        if not {f'{r - 1}_{c - 1}', f'{r}_{c - 1}', f'{r + 1}_{c - 1}'}.intersection(elves):
            if f'{r}_{c - 1}' in proposed:
                refused.add(f'{r}_{c - 1}')
            elif elf not in proposed:
                proposed[f'{r}_{c - 1}'] = elf
            moving.add(elf)

    elif dir == 'E':
        if not {f'{r - 1}_{c + 1}', f'{r}_{c + 1}', f'{r + 1}_{c + 1}'}.intersection(elves):
            if f'{r}_{c + 1}' in proposed:
                refused.add(f'{r}_{c + 1}')
            elif elf not in proposed:
                proposed[f'{r}_{c + 1}'] = elf
            moving.add(elf)


if __name__ == '__main__':
    map = open("23.txt").read().split('\n')
    elves = set()  # {row}_{column}
    for i, row in enumerate(map):
        for j, cell in enumerate(row):
            if cell == '#':
                elves.add(f'{i}_{j}')

    # print(solve_a(elves, 1))
    # print(solve_a(elves, 2))
    print(solve_a(elves, 10))
