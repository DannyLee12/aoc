from itertools import cycle


def get_floor(grid):
    floor = ''
    for i in range(1, 8):
        j = -1
        while grid[j][i] != '#':
            j -= 1
        floor += str(j)
        floor += '|'

    return floor


if __name__ == '__main__':
    input = ">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"
    input = open("17.txt").read().strip()
    blocks_val = 10000
    n = len(input)
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
