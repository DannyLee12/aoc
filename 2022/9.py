dirs = {'R': [1, 0], 'L': [-1, 0], 'U': [0, 1], 'D': [0, -1]}


def solve_a(steps):
    visited = set()
    H, T = [0, 0], [0, 0]
    for step in steps:
        dir, count = step.split()
        count = int(count)
        for _ in range(count):
            move(H, T)

            visited.add(f'{T[0]},{T[1]}')

            # print(H, T)

    return len(visited)


def move(H, T):
    # Move T
    # In the same row or column, not touching
    if H[0] == T[0] and abs(H[1] - T[1]) > 1:
        if T[1] > H[1]:
            T[1] = H[1] + 1
        else:
            T[1] = H[1] - 1
    elif H[1] == T[1] and abs(H[0] - T[0]) > 1:
        if T[0] > H[0]:
            T[0] = H[0] + 1
        else:
            T[0] = H[0] - 1
    # diagonals, not touching
    if H[0] != T[0] and H[1] != T[1]:
        if abs(H[0] - T[0]) > 1:
            if T[0] > H[0]:
                T[0] = H[0] + 1
            else:
                T[0] = H[0] - 1
            T[1] = H[1]
        elif abs(H[1] - T[1]) > 1:
            if T[1] > H[1]:
                T[1] = H[1] + 1
            else:
                T[1] = H[1] - 1
            T[0] = H[0]


def solve_b(steps):
    visited = set()
    links = [[11, 5] for _ in range(10)]
    for step in steps:
        i = 0
        dir, count = step.split()
        count = int(count)
        for _ in range(count):
            i = 0
            links[i][0] += dirs[dir][0]
            links[i][1] += dirs[dir][1]
            while i < 9:
                move(links[i], links[i+1])
                i += 1

        visited.add(f'{links[9][0]},{links[9][1]}')

    return len(visited)


if __name__ == '__main__':
    steps = open("9.txt").read().split('\n')
    # print(solve_a(steps))
    print(solve_b(steps))
