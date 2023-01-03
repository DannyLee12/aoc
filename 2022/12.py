from collections import deque


def solve_a(grid):

    n = len(grid)
    m = len(grid[0])

    def get_next(x, y):
        for i, j in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            xx = x + i
            yy = y + j
            if 0 <= xx < n and 0 <= yy < m:
                if grid[x][y] == 'S' or ord(grid[xx][yy]) - ord(grid[x][y]) <= 1 or grid[xx][yy] == 'E':
                    yield xx, yy

    def bfs(i, j, visited):
        q = deque([[i, j, 0]])
        while q:
            x, y, distance = q.popleft()
            for i, j in get_next(x, y):
                if grid[i][j] == 'E' and grid[x][y] == 'z':
                    return distance + 1
                if f'{i}_{j}' not in visited:
                    visited.add(f'{i}_{j}')
                    q.append([i, j, distance + 1])

    min_length = 10_000
    for i, row in enumerate(grid):
        for j, char in enumerate(row):
            if char == 'a':
                length = bfs(i, j, {f'{i}_{j}'})
                if length:
                    min_length = min(min_length, length)

    return min_length


if __name__ == '__main__':
    grid = [list(x) for x in open('12.txt').read().split('\n')]
    # print(grid)x
    print(solve_a(grid))


