from dataclasses import dataclass


@dataclass
class Range:
    north: int
    east: int
    south: int
    west: int


def solve_a(dirs: list) -> tuple:
    """Return the number of flipped tiles"""
    flipped = set()

    range = Range(0, 0, 0, 0)  # N, E, S, W
    for dir in dirs:
        pos = [0, 0]  # (N, E)
        i = 0
        # We move up N,S in 1s and E,W in 1 or 2
        while i < len(dir):
            if dir[i] in {'n', 's'}:
                if dir[i] == 'n':
                    pos[0] += 1
                else:
                    pos[0] -= 1
                if dir[i + 1] == 'e':
                    pos[1] += 1
                else:
                    pos[1] -= 1
                i += 2
            else:
                if dir[i] == 'e':
                    pos[1] += 2
                else:
                    pos[1] -= 2
                i += 1
        range.north = max(pos[0], range.north)
        range.south = min(pos[0], range.south)
        range.east = max(pos[1], range.east)
        range.west = min(pos[1], range.west)

        pos_string = "|".join(str(x) for x in pos)

        if pos_string in flipped:
            flipped.remove(pos_string)
        else:
            flipped.add(pos_string)

    # return len(flipped)
    return flipped, range


def calculate_range(pos, range) -> Range:
    range.north = max(pos[0], range.north)
    range.south = min(pos[0], range.south)
    range.east = max(pos[1], range.east)
    range.west = min(pos[1], range.west)

    return range


def solve_b(black_tiles: set, range: "Range",  iterations: int=100) -> int:
    """
    Return the number of black tiles after 100 days

    Rules: any black tile with 0 or > 2 black -> white
           any white tile with == 2 black -> black
    """
    def get_neighbours(pos, black_tiles):
        black_neighbours = 0
        for dir in [[1, 1], [0, 2], [-1, 1], [-1,-1], [0, -2], [1, -1]]:
            if "|".join(str(x) for x in [pos[0] + dir[0], pos[1] + dir[1]]) in black_tiles:
                black_neighbours += 1
        return black_neighbours

    # We need an odd east west if the north south value is odd.
    def get_pos(range) -> list:
        if (range.south - 1) % 2 == 1:
            if range.west % 2 == 0:
                pos = [range.south - 1, range.west - 1]
            else:
                pos = [range.south - 1, range.west - 2]
        else:
            if range.west % 2 == 0:
                pos = [range.south - 1, range.west - 2]
            else:
                pos = [range.south - 1, range.west - 1]

        return pos

    def add_black_tile(black_tiles, pos, range):
        new_black_tiles.add("|".join(str(x) for x in pos))

        return black_tiles, calculate_range(pos, range)

    while iterations:
        new_black_tiles = black_tiles.copy()
        pos = get_pos(range)
        base_pos = pos[:]
        while pos[0] < range.north + 1 or pos[1] < range.east + 2:
            neighbours = get_neighbours(pos, black_tiles)
            if "|".join(str(x) for x in pos) in black_tiles:
                # Tile is black
                if neighbours == 0 or neighbours > 2:
                    new_black_tiles.remove("|".join(str(x) for x in pos))
            else:  # Tile is white
                if neighbours == 2:
                    new_black_tiles, range = add_black_tile(new_black_tiles,
                                                            pos, range)
            if pos[1] >= range.east + 2:
                pos[1] = base_pos[1]  # Reset to far west position
                pos[0] += 1
                if pos[0] % 2 != pos[1] % 2:
                    pos[1] -= 1
            else:
                pos[1] += 2
        black_tiles = new_black_tiles
        iterations -= 1

    return len(new_black_tiles)


if __name__ == '__main__':
    dirs = open("24.txt").read().split()
    black_tiles, range = solve_a(dirs)
    print(solve_b(black_tiles, range, 100))
