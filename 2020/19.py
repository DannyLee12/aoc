from collections import defaultdict


def gen_regex(r):
    """Create a regex"""

    if r == 8:
        return '(' + gen_regex(42) + ')+'
    if r == 11:
        r42 = gen_regex(42)
        r31 = gen_regex(31)
        parts = []
        # We don't generally make it work, we just make it work for up to
        # 10 recursions of rule 11 which is good enough for our input.
        for i in range(1, 10):
            parts.append('(%s){%d}(%s){%d}' % (r42, i, r31, i))
        return '(' + '|'.join(parts) + ')'

    if isinstance(r, str):
        return r
    parts = rules[r]
    if len(parts) == 1:
        return ''.join(gen_regex(child) for child in parts[0])
    return '(' + '|'.join(
        ''.join(gen_regex(child) for child in p) for p in parts) + ')'






if __name__ == '__main__':
    rules_raw, vals = open("19.txt").read().split("\n\n")
    # rules = rules.split("\n")
    # rules_d = {x.strip(): y.strip() for x, y in (z.split(":") for z in rules)}

    # print(solve_a(rules_d, vals))

    rules = {}
    for line in rules_raw.strip().splitlines():
        k, rest = line.split(':')
        parts = rest.split('|')
        rules[int(k)] = [tuple(map(eval, p.split())) for p in parts]

    import re

    m = re.compile('^' + gen_regex(0) + '$')
    count = 0
    for line in vals.strip().splitlines():
        if m.match(line.strip()):
            count += 1
    print(count)
