from collections import defaultdict, deque


def solve_a(blizzards, max_row, max_column, goal):
    def get_next(row, col, goal=goal):
        for i, j in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            xx = row + i
            yy = col + j
            if xx == goal[0] and yy == goal[1]:
                yield xx, yy
            if 1 <= xx < max_row and 1 <= yy < max_column:
                yield xx, yy

    def move_blizzards(blizzards):
        new_blizzards = defaultdict(list)
        for k, v in blizzards.items():
            row_, col_ = k.split('_')
            for shape in v:
                row, col = int(row_), int(col_)
                if shape == 'v':
                    if row + 1 == max_row:
                        row = 1
                    else:
                        row += 1
                elif shape == '^':
                    if row - 1 == 0:
                        row = max_row - 1
                    else:
                        row -= 1
                elif shape == '>':
                    if col + 1 == max_column:
                        col = 1
                    else:
                        col += 1
                elif shape == '<':
                    if col - 1 == 0:
                        col = max_column - 1
                    else:
                        col -= 1
                new_blizzards[f'{row}_{col}'].append(shape)

        return new_blizzards

    def bfs(blizzards, goal=goal):
        q = deque([[0, 1, 0]])
        visited = set()
        while q:
            row, col, time = q.popleft()
            if len(blizzards) <= time + 1:
                blizzards.append(move_blizzards(blizzards[time]))
            if f'{row}_{col}_{time}' in visited:
                continue
            visited.add(f'{row}_{col}_{time}')
            if row == goal[0] and col == goal[1]:
                return time
            q.append([row, col, time + 1])  # wait
            for x, y in get_next(row, col):
                if f'{x}_{y}' not in blizzards[time + 1]:
                    q.append([x, y, time + 1])

    return bfs(blizzards)


if __name__ == '__main__':
    map = open("24.txt").read().split('\n')
    blizzards = [defaultdict(list)]
    for r, row in enumerate(map):
        for c, cell in enumerate(row):
            if cell in ['<', '>', '^', 'v']:
                blizzards[0][f'{r}_{c}'] += [cell]

    goal = [36, 100]
    print(solve_a(blizzards, len(map) - 1, len(map[0]) - 1, goal))

    # print(blizzards)
