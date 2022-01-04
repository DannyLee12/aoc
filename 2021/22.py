from collections import defaultdict


def solve(input: list) -> int:
    """Return the number of items on after the steps of switches"""
    on = set()
    for i, row in enumerate(input):
        io, blocks = row.split(" ")
        d = {}
        for coord in blocks.split(","):
            c, vals = coord.split("=")
            d[c] = list(map(int, vals.split("..")))

        for x in range(d["x"][0], d["x"][1] + 1):
            if not -50 < int(x) < 50:
                continue
            for y in range(d["y"][0], d["y"][1] + 1):
                for z in range(d["z"][0], d["z"][1] + 1):
                    if io == 'on':
                        on.add(f'{x},{y},{z}')
                    elif io == 'off':
                        try:
                            on.remove(f'{x},{y},{z}')
                        except KeyError:
                            pass
        print(f"{i/len(input) * 100} %")

    return len(on)


def solve_b(input: list) -> int:
    """Return the number of items on, but smarter ;)"""
    offs = set()
    mins = defaultdict(lambda: float("inf"))
    maxs = defaultdict(int)

    for i, row in enumerate(input):
        io, blocks = row.split(" ")
        d = {}
        if io == "on":
            for coord in blocks.split(","):
                c, vals = coord.split("=")
                m, ma = list(map(int, vals.split("..")))

                maxs[c] = max(ma, maxs[c])
                mins[c] = min(m, mins[c])

                for item in offs:
                    # See if any lights are switched on
                    pass

        elif io == "off":
            for coord in blocks.split(","):
                c, vals = coord.split("=")
                offs.add(vals)

        # return the size of the block less the off items
        ons = (maxs['x'] + 1 - mins['x']) * (maxs['y'] + 1 - mins['y']) * (maxs['z'] + 1 - mins['z'])
        # for item in offs:
        #     ons -= 1

    return ons


if __name__ == '__main__':
    input = open('22.txt').read().split('\n')
    print(solve_b(input))
