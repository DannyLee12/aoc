import math


def expression(id: int, l: list) -> int:
    """Return the operation on the list"""
    if id == 0:
        return sum(l)
    elif id == 1:
        return math.prod(l)
    elif id == 2:
        return min(l)
    elif id == 3:
        return max(l)
    elif id == 5:
        return l[0] > l[1]
    elif id == 6:
        return l[0] < l[1]
    elif id == 7:
        return l[0] == l[1]


def solve_a(input: str, pos: int = 0, versions: list = []) -> tuple:
    """Add up the version numbers of all packets"""

    version = int(input[pos: pos + 3], 2)

    versions.append(version)
    # print(sum(versions))

    id = int(input[pos + 3: pos + 6], 2)

    pos += 6
    num = input[pos + 1: pos + 5]
    start_bit = input[pos]
    pos_lit = pos + 5
    if id == 4:
        # Literal
        while start_bit != '0':
            num += input[pos + 1: pos + 5]
            start_bit = input[pos_lit]
            pos_lit += 5

        return pos_lit, int(num, 2)

    else:
        values = []
        length_id = input[pos]
        if length_id == '0':
            len_sub_packet = int(input[pos + 1: pos + 1 + 15], 2)
            pos += 16
            end_val = pos + len_sub_packet
            while pos < end_val:
                pos, value = solve_a(input, pos, versions)
                values.append(value)
            return pos, expression(id, values)

        elif length_id == '1':
            no_of_packets = int(input[pos + 1: pos + 1 + 11], 2)
            pos += 12
            for _ in range(no_of_packets):
                pos, value = solve_a(input, pos, versions)
                values.append(value)
            return pos, expression(id, values)

    # return sum(versions)


if __name__ == '__main__':
    input = open("16.txt").read()
    # input = ""
    # input = "D2FE28"
    # input = "A0016C880162017C3686B18A3D4780"
    # input = "38006F45291200"
    # input = "EE00D40C823060"
    bin_input = ""
    for char in input:
        b = bin(int(char, 16))
        bin_input += "0" * (6 - len(b)) + b[2:]
    # input = "0101001000100100"
    print(solve_a(bin_input))
