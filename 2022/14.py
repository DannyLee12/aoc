from collections import deque


def solve_a(grid, min_y):
    # fall down
    # then left (if on sand)
    # then right (if on sand)
    total_sand = 0
    x, y = 0, 500 - min_y
    while grid[0][500] != 'O':
        if grid[x + 1][y] == '.':
            # print(x,y, total_sand)
            # Drop down
            x += 1
        else:  # Either blocked by sand or rock
            # Try Diagonal left
            if grid[x + 1][y - 1] == '.':
                x += 1
                y -= 1
            elif grid[x + 1][y + 1] == '.':
                x += 1
                y += 1
            else:
                grid[x][y] = 'O'
                total_sand += 1
                x, y = 0, 500 - min_y
                print(total_sand, x, y)
    return total_sand


if __name__ == '__main__':
    rows = open("14.txt").read().split('\n')
    grid = [['.'] * 20000 for x in range(200)]
    seen = set()
    # min_y = 494
    min_y, max_y = 0, 10
    # min_y, max_y = 494, 505
    for row in rows:
        if ".".join(row) not in seen:
            seen.add(".".join(row))
            dirs = deque([x.strip() for x in row.split('->')])
            while len(dirs) >= 2:
                dir = dirs.popleft()
                x, y = list(map(int, dir.split(",")))
                i, j = list(map(int, dirs[0].split(",")))
                min_y_1, max_y = min(min_y, j), max(max_y, j)
                x, i = x - min_y, i - min_y
                if x == i:
                    if y < j:
                        for yy in range(y, j + 1):
                            grid[yy][x] = '#'
                    else:
                        for yy in range(j, y + 1):
                            grid[yy][x] = '#'
                elif y == j:
                    if x < i:
                        for xx in range(x, i + 1):
                            grid[y][xx] = '#'
                    else:
                        for xx in range(i, x + 1):
                            grid[y][xx] = '#'

    for i in range(999):
        grid[175][i] = '#'

    print(max_y)
    print(solve_a(grid, min_y))