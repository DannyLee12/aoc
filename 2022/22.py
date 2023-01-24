import math


def turn(x, y, dir):
    if dir == 'R':
        return [y, -x]
    elif dir == 'L':
        return [-y, x]
    else:
        return [x, y]


def dir_val(dir):
    if dir == [0, 1]:
        return 0
    elif dir == [0, -1]:
        return 2
    elif dir == [1, 0]:
        return 1
    elif dir == [-1, 0]:
        return 3


def solve_a(grid, dirs):
    grid = [list(x) for x in grid.split('\n')]
    pos = [0, grid[0].index('.')]
    direction = [0, 1]
    row_bounds = []
    col_bounds = [[math.inf, -math.inf]]
    for i, row in enumerate(grid):
        bounds = [-1, -1]
        for j, char in enumerate(row):
            if j >= len(col_bounds):
                col_bounds.append([math.inf, -math.inf])
            if char != ' ':
                if bounds[0] == -1:
                    bounds[0] = j
                else:
                    bounds[1] = j
                # Column bounds
                col_bounds[j][0] = min(col_bounds[j][0], i)
                col_bounds[j][1] = max(col_bounds[j][1], i)
        row_bounds.append(bounds)

    val = ""
    i = 0
    for char in dirs:
        if char.isdigit():
            val += char
        else:
            i += 1
            val = int(val)
            # move
            while val:
                pot_pos = [pos[0] + direction[0], pos[1] + direction[1]]
                try:
                    if pot_pos[0] < 0 or pot_pos[1] < 0:
                        raise IndexError
                    if grid[pot_pos[0]][pot_pos[1]] == '#':
                        val = ""
                        break
                except IndexError:
                    pass

                try:
                    if grid[pot_pos[0]][pot_pos[1]] == ' ' or pot_pos[0] < 0 or pot_pos[1] < 0:
                        raise IndexError
                except IndexError:
                    if direction == [0, 1]:  # Right
                        pot_pos[1] = row_bounds[pos[0]][0]
                    elif direction == [0, -1]:  # Left
                        pot_pos[1] = row_bounds[pos[0]][1]
                    elif direction == [1, 0]:
                        pot_pos[0] = col_bounds[pos[1]][0]
                    elif direction == [-1, 0]:
                        pot_pos[0] = col_bounds[pos[1]][1]

                    if grid[pot_pos[0]][pot_pos[1]] == '#':
                        val = ""
                        break
                    else:
                        pos = pot_pos
                        val -= 1
                else:
                    pos = pot_pos
                    val -= 1

            val = ""

            direction = turn(*direction, char)

    print(i)
    return 1000 * (pos[0] + 1) + 4 * (pos[1] + 1) + dir_val(direction)


if __name__ == '__main__':
    grid, dirs = open("22.txt").read().split('\n\n')
    print(solve_a(grid, dirs))

