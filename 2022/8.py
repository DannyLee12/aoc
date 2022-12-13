def solve_a(rows):
    n = len(rows)
    m = len(rows[0])

    visible = set()

    # left to right
    for i, row in enumerate(rows):
        largest = ''
        for j, item in enumerate(row):
            if item > largest:
                visible.add(f'{i},{j}')
            largest = max(largest, item)

    # right to left
    for i, row in enumerate(rows):
        largest = ''
        for j, item in enumerate(reversed(row)):
            if item > largest:
                visible.add(f'{i},{m - j - 1}')
            largest = max(largest, item)

    # top to bottom
    for i in range(n):
        largest = ''
        for j in range(m):
            # print(rows[j][i])
            if rows[j][i] > largest:
                visible.add(f'{j},{i}')
            largest = max(largest, rows[j][i])

    # bottom to top
    for i in range(n):
        largest = ''
        for j in range(m - 1, -1, -1):
            # print(rows[j][i])
            if rows[j][i] > largest:
                # print(rows[j][i])
                visible.add(f'{j},{i}')
            largest = max(largest, rows[j][i])

    return len(visible)


def solve_b(rows):
    n = len(rows)
    m = len(rows[0])

    def count_trees(i, j):
        # print(i, j)
        ii, jj = i, j
        tree = rows[i][j]
        up, down, left, right = 0, 0, 0, 0
        # up
        ii -= 1
        while 0 <= ii < n:
            if rows[ii][j] < tree:
                up += 1
                ii -= 1
            else:
                up += 1
                break
        # down
        ii = i + 1
        while 0 <= ii < n:
            if rows[ii][j] < tree:

                down += 1
                ii += 1
            else:
                down += 1
                break

        # right
        jj = j + 1
        while 0 <= jj < m:
            if rows[i][jj] < tree:
                right += 1
                jj += 1
            else:
                right += 1
                break
        # left
        jj = j - 1
        while 0 <= jj < m:
            if rows[i][jj] < tree:
                left += 1
                jj -= 1
            else:
                left += 1
                break

        return left * right * up * down

    most_trees = 0

    # print(count_trees(3, 2))

    for i in range(n):
        for j in range(m):
            most_trees = max(most_trees, count_trees(i, j))

    return most_trees


if __name__ == '__main__':
    rows = [list(x) for x in open("8.txt").read().split('\n')]
    print(solve_a(rows))
    print(solve_b(rows))
