DIRS = {"forward": (1, 0),
        "down": (0, 1),
        "up": (0, -1)}

DIRS_AIM = {"forward": (1, 1, 0),
            "down": (0, 0, 1),
            "up": (0, 0, -1)}


def solve_a(directions: list) -> int:
    """Find position based on directions"""
    horizontal, depth = 0, 0
    for direction in directions:
        horizontal, depth = (horizontal + (int(direction[1]) * DIRS[direction[0]][0]),
                              depth + (int(direction[1]) * DIRS[direction[0]][1]))

    return horizontal * depth


def solve_b(directions: list) -> int:
    """Find new position based on aim"""
    horizontal, depth, aim = 0, 0, 0
    for direction in directions:
        horizontal, depth, aim = (horizontal + int(direction[1]) * DIRS_AIM[direction[0]][0],
                                 depth + (int(direction[1]) * DIRS_AIM[direction[0]][1] * aim),
                                  aim + int(direction[1]) * DIRS_AIM[direction[0]][2])

    return horizontal * depth


if __name__ == '__main__':
    d = [direction.strip().split(" ") for direction in open("2.txt").readlines()]
    print(solve_a(d))
    print(solve_b(d))

