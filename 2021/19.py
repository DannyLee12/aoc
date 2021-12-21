from collections import defaultdict


def solve_a(input: list) -> int:
    """Find beacons"""
    scanner = []
    for i, scan in enumerate(input):
        for j, row in enumerate(scan.split("\n")):
            if j == 0:
                continue
            x, y, z = list(map(int, row.split(",")))
            if i == 0:
                scanner.append((x, y, z))
            else:
                continue


    print(scanner)
    # print(distances)
    # return len(set(beacons) - remove)


if __name__ == '__main__':
    input = open("19.txt").read().split("\n\n")
    print(input)
    print(solve_a(input))
