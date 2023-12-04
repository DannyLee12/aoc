def first_digit(s: str) -> str:
    """Return the first digit in a string."""
    for c in s:
        if c.isdigit():
            return c


def solve_a(rows):
    total = 0
    for row in rows:
        total += int(first_digit(row) + first_digit(row[::-1]))

    return total


numbers = {"zero": '0', "one": '1', "two": '2', "three": '3', "four": '4',
           "five": '5', "six": '6', "seven": '7', "eight": '8', "nine": '9'}

def solve_b(rows):
    total = 0

    for row in rows:
        pos = {}
        for i, c in enumerate(row):
            if c.isdigit():
                pos[i] = c
        for number in numbers:
            if row.find(number) > -1:
                pos[row.find(number)] = numbers[number]
            if row.rfind(number) > -1:
                pos[row.rfind(number)] = numbers[number]

        keys = sorted(pos.keys())
        total += int(pos[keys[0]] + pos[keys[-1]])

    return total


if __name__ == '__main__':
    with open("1.txt") as f:
        rows = f.read().split('\n')

    # print(solve_a(rows))
    print(solve_b(rows))
