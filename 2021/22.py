from functools import lru_cache

def solve_a(p1: list, p2: list) -> int:
    """Get the score of the winner"""
    total = 0
    while p1 and p2:
        total += 1
        if p1[0] > p2[0]:
            p1.extend([p1.pop(0), p2.pop(0)])
        else:
            p2.extend([p2.pop(0), p1.pop(0)])

    n = max(len(p1), len(p2))
    score = 0
    if p1:
        p = p1[:]
    else:
        p = p2[:]
    for card in p:
        score += card * n
        n -= 1

    return score


def solve_b(p1: list, p2: list) -> int:
    """Recursively solve for p1 and p2"""

    def solve(p1, p2):
        seen1, seen2 = set(), set()

        while p1 and p2:
            h = hash(str(p1))
            h2 = hash(str(p2))

            # Check if we can recurse
            if h in seen1 or h2 in seen2:
                return 'p1'
            a, b = p1.pop(0), p2.pop(0)
            if a <= len(p1) and b <= len(p2):
                if solve(p1[:a], p2[:b]) == 'p1':
                    p1.extend([a, b])
                else:
                    p2.extend([b, a])
            else:
                if a > b:
                    p1.extend([a, b])
                else:
                    p2.extend([b, a])
            seen1.add(h)
            seen2.add(h2)

        if p1:
            return 'p1'
        return 'p2'

    seen1, seen2 = set(), set()

    while p1 and p2:
        h = hash(str(p1))
        h2 = hash(str(p2))

        # Check if we can recurse
        if h in seen1 or h2 in seen2:
            p1.extend([p1.pop(0), p2.pop(0)])
        a, b = p1.pop(0), p2.pop(0)
        if a <= len(p1) and b <= len(p2):
            if solve(p1[:a], p2[:b]) == 'p1':
                p1.extend([a, b])
            else:
                p2.extend([b, a])
        else:
            if a > b:
                p1.extend([a, b])
            else:
                p2.extend([b, a])
        seen1.add(h)
        seen2.add(h2)

    n = max(len(p1), len(p2))
    score = 0
    if p1:
        p = p1[:]
    else:
        p = p2[:]
    for card in p:
        score += card * n
        n -= 1

    return score


if __name__ == '__main__':
    p1, p2 = open("22.txt").read().split('\n\n')
    p1 = [int(x) for x in p1.split() if 'Player' not in x and ':' not in x]
    p2 = [int(y) for y in p2.split() if 'Player' not in y and ':' not in y]
    print(solve_b(p1, p2))