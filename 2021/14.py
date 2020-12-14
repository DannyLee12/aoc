from collections import defaultdict


def solve_a(l: list) -> int:
    """Return sum of all values in list"""
    vals = defaultdict(int)
    for row in l:
        if row.startswith("mask"):
            mask = row.split("=")[1][::-1]
        else:
            position, value = row.split("=")
            position = position[4:-2]
            new_val = ""
            i = 0
            num = bin(int(value))[2:][::-1]
            while i < 36:
                if i < len(num):
                    if mask[i] == "X":
                        new_val += num[i]
                    else:
                        new_val += mask[i]
                else:
                    if mask[i] == '1':
                        new_val += "1"
                    else:
                        new_val += "0"
                i += 1
            vals[position] = int(new_val[::-1], 2)

    return sum(vals.values())


def solve_b(l: list) -> int:
    """Use a bitmask for memory this time"""
    vals = defaultdict(int)
    for row in l:
        if row.startswith("mask"):
            mask = row.split("=")[1][::-1]
        else:
            position, value = row.split("=")
            position = position[4:-2]
            new_pos = ""
            i = 0
            position = bin(int(position))[2:][::-1]
            while i < 36:
                if i < len(position) and mask[i] == "0":
                    new_pos += position[i]
                else:
                    new_pos += mask[i]
                i += 1
            positions = [new_pos]
            while positions:
                xs = False
                x = positions.pop()
                if "X" in x:
                    positions.append(x.replace("X", "0", 1))
                    positions.append(x.replace("X", "1", 1))
                else:
                    vals[int(x[::-1], 2)] = int(value)

    return sum(vals.values())


if __name__ == '__main__':
    input = open("14.txt").read().split("\n")
    print(solve_a(input))
    print(solve_b(input))
