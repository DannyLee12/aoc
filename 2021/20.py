from collections import defaultdict


def solve(tiles: list):
    d = {}
    for i, tile in enumerate(tiles):
        horizontal = tile.split("\n")
        no = horizontal[0]
        top, bottom = horizontal[1], horizontal[-1]
        left, right = "", ""
        for j, element in enumerate(horizontal):
            if j == 0:
                continue
            left += element[0]
            right += element[-1]
        d[no] = (top, bottom, left, right)

    total = 1
    corners = [""] * 4  # top-left, top-right, bottom-left, bottom-right
    for i, (k, v) in enumerate(d.items()):
        l = v
        counter = 0
        seen = [False, False, False, False]
        for j, v1 in enumerate(d.values()):
            if j == i:
                continue
            for a, val in enumerate(v1):
                if val in l or val[::-1] in l:
                    counter += 1
                    seen[a] = True

        if counter == 2:
            print(k)
            print(seen)
            # total *= int(k.split()[-1][:-1])
            if seen[0] and seen[3]:
                corners[1] = k
            elif seen[1] and seen[2]:
                corners[2] = k
            elif seen[1] and seen[3]:
                corners[3] = k
            else:
                corners[0] = k
            print(corners)



if __name__ == '__main__':
    tiles = open("20.txt").read().split("\n\n")
    print(len(tiles))
    solve(tiles)
