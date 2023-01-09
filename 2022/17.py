from itertools import cycle


def part_b():
    rocks, i = ((0,1,2,3),(1,0+1j,2+1j,1+2j),(0,1,2,2+1j,2+2j),(0,0+1j,0+2j,0+3j),(0,1,0+1j,1+1j)), 0
    jets,  j = [ord(x)-61 for x in open('17.txt').read()], 0
    tower, cache, top = set(), dict(), 0

    empty = lambda pos: pos.real in range(7) and pos.imag>0 and pos not in tower
    check = lambda pos, dir, rock: all(empty(pos+dir+r) for r in rock)

    for step in range(int(1e12)):
        pos = complex(2, top+4)                     # set start pos
        if step == 2022:
            print(top)

        key = i,j
        if key in cache:                            # check for cycle
            S, T = cache[key]
            d, m = divmod(1e12-step, step-S)
            if m == 0: print(top + (top-T)*d); break
        else: cache[key] = step, top

        rock = rocks[i]                             # get next rock
        i = (i+1) % len(rocks)                      # and inc index

        while True:
            jet = jets[j]                           # get next jet
            j = (j+1) % len(jets)                   # and inc index

            if check(pos, jet, rock): pos += jet    # maybe move side
            if check(pos, -1j, rock): pos += -1j    # maybe move down
            else: break                             # can't move down

        tower |= {pos+r for r in rock}              # add rock to tower
        top = max(top, pos.imag+[1,0,2,2,3][i])     # compute new top

if __name__ == '__main__':
    input = ">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"
    input = open("17.txt").read().strip()
    blocks_val = 10000
    n = len(input)
    part_b()
    exit()
    # input = reversed(input)
    # shapes stores the bounds of the shape, indexed from top left
    # [l, r, t, b]
    shapes = [
        [(0, 0), (0, 1), (0, 2), (0, 3)],  # -
        [(-2, 1), (-1, 0), (-1, 1), (-1, 2), (0, 1)],  # +
        [(-2, 0), (-2, 1), (-2, 2), (-1, 2), (0, 2)],  # L
        [(-3, 0), (-2, 0), (-1, 0), (0, 0)],  # l
        [(-1, 0), (-1, 1), (0, 1), (0, 0)]   # #
    ]
    offset = [1, 3, 3, 4, 2]

    grid = [['#'] * 9]
    # grid.extend([['#'] + ['_'] * 7 + ['#'] for _ in range(3)])
    floor_height = 0
    blocks = 0
    index = 0

    test_cache = {}
    cache = {}

    for shape, offset in zip(cycle(shapes), cycle(offset)):
        # if blocks == blocks_val:
        #     break
        grid.extend([['#'] + ['_'] * 7 + ['#'] for _ in range((offset + 3 + floor_height) - len(grid) + 1)])
        x, y = 3, floor_height + offset + 3
        prev_height = floor_height
        # start dropping
        while blocks < blocks_val:
            exit = False
            if input[index % n] == '>':
                # print('right')
                # Try move right
                valid = True
                for i, j in shape:
                    if grid[y + i][x + 1 + j] == '#':
                        valid = False
                        break
                if valid:
                    x += 1
            else:
                # Try move left
                # print('left')
                valid = True
                for i, j in shape:
                    if grid[y + i][x + j - 1] == '#':
                        valid = False
                        break
                if valid:
                    x -= 1
            index += 1

            # Try drop down
            for i, j in shape:
                if grid[y - 1 + i][x + j] == '#':
                    # print(i, j)
                    # update the grid with new blocks
                    for a, b in shape:
                        grid[y + a][x + b] = '#'
                        floor_height = max(floor_height, y + a)

                    blocks += 1

                    if blocks > 5000:
                        floor = get_floor(grid)
                        if f'{index % 5}:{input[index % n]}:{floor}' in cache:
                            print(blocks - cache[f'{index % 5}:{input[index % n]}:{floor}'][0])
                            print(floor_height - cache[f'{index % 5}:{input[index % n]}:{floor}'][1])
                            print(f'{index % 5}:{input[index % n]}:{floor}')
                            pass
                        cache[f'{index % 5}:{input[index % n]}:{floor}'] = (blocks, floor_height)

                    if blocks == blocks_val:
                        print(floor_height)
                        exit = True
                        break

                    exit = True
                    break

            y -= 1

            if exit:
                break
