def move_(position, direction, steps):
    """Move steps in direction direction"""
    if direction == "N":
        position[0] += steps
    elif direction == "E":
        position[1] += steps
    elif direction == "S":
        position[0] -= steps
    elif direction == "W":
        position[1] -= steps
    return position


def solve_a(l: list) -> int:
    """Return the manhattan distance"""
    dir = "E"
    dirs = ["E", "S", "W", "N"]
    l_dirs = ["E", "N", "W", "S"]
    position = [0, 0]

    for move in l:
        if move[0] == "F":
            position = move_(position, dir, int(move[1:]))
        elif move[0] == "R":
            dir = dirs[(int((int(move[1:]) % 360) / 90) + dirs.index(dir)) % 4]
        elif move[0] == "L":
            dir = l_dirs[(int((int(move[1:]) % 360) / 90) + l_dirs.index(dir)) % 4]
        else:
            move_(position, move[0], int(move[1:]))
    print(dir)

    return abs(position[0]) + abs(position[1])


def solve_b(l: list) -> int:
    """Moving waypoints"""
    wp = [1, 10]
    ship = [0, 0]
    for move in l:
        if move[0] == "F":
            moves = list(map(lambda x: x * int(move[1:]), wp))
            ship[0] += moves[0]
            ship[1] += moves[1]
        elif move[0] == "R":
            for _ in range(int(move[1:]) % 360 // 90):
                wp[0], wp[1] = -wp[1], wp[0]
        elif move[0] == "L":
            for _ in range(int(move[1:]) % 360 // 90):
                wp[0], wp[1] = wp[1], -wp[0]
        else:
            wp = move_(wp, move[0], int(move[1:]))

    return abs(ship[0]) + abs(ship[1])


if __name__ == '__main__':
    moves = open("12.txt").read().split("\n")
    print(solve_a(moves))
    print(solve_b(moves))
