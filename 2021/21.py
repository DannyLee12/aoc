from collections import defaultdict


def solve_a(d: dict) -> list:
    """Return the number of ingredients without allergies"""
    loop = 9
    while loop:
        for i, (k, v) in enumerate(d.items()):
            for j, (k1, v1) in enumerate(d.items()):
                if i == j:
                    continue
                if len(v1) == 1:
                    for element in v1:
                        try:
                            v.remove(element)
                        except KeyError:
                            pass
        loop -=1


    def solve_b(d):
        nd = {}
        for k, v in d.items():
            nd[k] = list(v)[0]

        nd = ",".join(x[1] for x in sorted(nd.items(), key=lambda x : x[0]))

        print(nd)

    all_values = []
    for v in d.values():
        all_values.extend(list(v))

    solve_b(d)

    return all_values


if __name__ == '__main__':
    d = defaultdict(set)
    all_foods = []
    for row in open('21.txt').read().split('\n'):
        split_row = row.split('contains')
        foods = {x.strip() for x in split_row[0].split() if x != "("}
        all_foods.extend(foods)
        allergies = {y.strip().rstrip(')') for y in split_row[1].split(',') if y != ','}
        for allergy in allergies:
            if not d[allergy]:
                d[allergy] = foods
            else:
                d[allergy] = d[allergy].intersection(foods)

    all_allergies = solve_a(d)
    total = 0
    for item in all_foods:
        if item in all_allergies:
            total += 1

    print(len(all_foods) - total)

