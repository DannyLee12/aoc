from itertools import product

SNAFU_TO_DECIMAL = {"1": 1, "2": 2, "0": 0, "-": -1, "=": -2}
SNAFU_POWER = 5


def convert(value: str):
    total = 0
    multiplier = 1
    for val in reversed(value):
        if val == '-':
            total -= multiplier
        elif val == '=':
            total -= 2 * multiplier
        else:
            total += int(val) * multiplier

        multiplier *= 5

    return total


def reconvert(decimal: int) -> str:
    # determine how many snafu places this number requires
    number_of_characters = 0
    while True:
        number_of_characters += 1
        if sum([max(SNAFU_TO_DECIMAL.values()) * (SNAFU_POWER**i) for i in range(number_of_characters)]) >= decimal:
            break

    # initialise our result string with 0's, then for each snafu place, find the char that gets us closest to `decimal`
    snafu = "0" * number_of_characters
    for i in range(number_of_characters):
        snafu = min(
            [snafu[0:i] + x + snafu[i + 1 :] for x in SNAFU_TO_DECIMAL.keys()],
            key=lambda my_snafu: abs(decimal - convert(my_snafu)),
        )

    return snafu


def solve_a(rows):
    total = 0
    for row in rows:
        total += convert(row)
    return reconvert(total)


if __name__ == '__main__':
    rows = open("25.txt").read().split('\n')
    print(solve_a(rows))
