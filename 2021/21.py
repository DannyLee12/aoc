from functools import lru_cache
from functools import cache
from itertools import product

DICE = [(3, 1), (4, 3), (5, 6), (6, 7), (7, 6), (8, 3), (9, 1)]


def solve_a() -> int:
    """Return the score of the loser by the number of times the die rolled"""
    p1 = 7
    p2 = 10
    t1 = 0
    t2 = 0

    player1 = True

    i = 1
    while t1 < 1000 and t2 < 1000:
        total = 0
        for x in range(i, i + 3):
            total += x
        if player1:
            p1 = 10 if (p1 + total) % 10 == 0 else (p1 + total) % 10
            t1 += p1
            player1 = False
        else:
            p2 = 10 if (p2 + total) % 10 == 0 else (p2 + total) % 10
            t2 += p2
            player1 = True
        i += 3

    return (i - 1) * min(t1, t2)


@cache
def solve_b(p1, p2, s1=0, s2=0) -> tuple:
    """Recursively solve for all universes"""
    if s2 >= 21:
        return 0, 1
    wins1, wins2 = 0, 0
    # With 3 dice, it's possible to roll 3 1 way, 4 3 ways etc etc
    for value, possibilities in DICE:
        p = (p1 + value) % 10 or 10  # 10 % 10 is falsy so or is called
        # Swap to change turns
        r2, r1 = solve_b(p2, p, s2, s1 + p)
        wins1, wins2 = wins1 + r1 * possibilities, wins2 + r2 * possibilities
    return wins1, wins2


if __name__ == '__main__':
    print(solve_a())
    print(max(solve_b(7, 10)))
