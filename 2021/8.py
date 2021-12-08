def solve_a(input: list) -> int:
    """Return the number of 1, 4, 7 & 8s"""
    total = 0
    for row in input:
        for output in row[1].strip().split(" "):
            if len(output) in {2, 3, 4, 7}:
                total += 1

    return total

def solve_b(raw_input: list) -> int:
    """return the sum of the digits returned"""
    sum_total = 0
    for row in raw_input:
        total = ""
        map = {}
        input = row[0].strip().split()
        while input:
            broken = False
            for i, x in enumerate(input):
                try:
                    for c in map[1]:
                        if c in map[2]:
                            map["c"] = c
                except KeyError:
                    pass
                if len(x) == 2:
                    map[1] = input.pop(i)
                    break
                elif len(x) == 3:
                    map[7] = input.pop(i)
                    break
                elif len(x) == 4:
                    map[4] = input.pop(i)
                    break
                elif len(x) == 7:
                    map[8] = input.pop(i)
                    try:
                        map["e"] = "".join(set(map[8]) - set(map[9]))
                    except KeyError:
                        pass
                    break
                elif len(x) == 6:
                    if broken:
                        break

                    try:
                        b = True
                        for c in map[4]:
                            if c not in x:
                                b = False
                                break
                        if b:
                            map[9] = input.pop(i)
                            map["e"] = "".join(set(map[8]) - set(map[9]))
                            broken = True
                            break
                    except KeyError:
                        pass
                    # map[9] exists
                    try:
                        _ = map[9]
                        if map["c"] in x:
                            map[0] = input.pop(i)
                            break
                        else:
                            map[6] = input.pop(i)
                            break
                    except KeyError:
                        pass
                elif len(x) == 5:
                    if broken:
                        break
                    # 3 contains 7

                    try:
                        b = True
                        for c in map[7]:
                            if c not in x:
                                b = False
                                break
                        if b:
                            map[3] = input.pop(i)
                            broken = True
                            break
                    except KeyError:
                        pass
                    # if map[3] exists
                    if broken:
                        break
                    try:
                        _ = map[3]
                        if map["e"] in x:
                            map[2] = input.pop(i)
                            break
                        else:
                            map[5] = input.pop(i)
                            broken = True
                            break
                    except KeyError:
                        pass
        new_map = dict([("".join(sorted(value)), key) for key, value in map.items()])
        for item in row[1].strip().split():
            total += str(new_map["".join(sorted(item))])
        print(total)
        sum_total += int(total)

    return sum_total







if __name__ == '__main__':
    input = [x.split("|") for x in open("8.txt").read().split("\n")]
    # print(solve_a(input))
    print(solve_b(input))
