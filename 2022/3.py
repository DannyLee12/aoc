from itertools import chain

from string import ascii_lowercase, ascii_uppercase

score = {char: i + 1 for i, char in enumerate(chain(ascii_lowercase, ascii_uppercase))}
score['#'] = 0
def solve_a(rows):
    total = 0

    for row in rows:
        n = len(row) // 2
        left, right = row[:n], set(row[n:])
        for char in left:
            if char in right:
                total += score[char]
                break

    return total


def solve_b(rows):
    total = 0

    s = {'#'}
    for i, row in enumerate(rows):
        if i % 3 == 0:
            total += score["".join(s)]
            s = set(list(row))
        else:
            s &= set(list(row))

    total += score["".join(s)]

    return total


if __name__ == '__main__':
    rows = open('3.txt').read().split('\n')
    print(solve_a(rows))
    print(solve_b(rows))
