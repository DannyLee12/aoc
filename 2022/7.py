from collections import defaultdict
from functools import lru_cache


def solve_a(rows):
    totals = {}
    d = defaultdict(list)
    q = []
    for row in rows:
        if row == '$ cd ..':
            q.pop()
        elif row[:4] == '$ cd':
            q.append(row.split()[-1])
        elif row[0] == '$':  # Ignore ls
            pass
        elif row[0].isnumeric():
            d["/".join(q)].append("/".join(q) + '/' + row)
        elif row[0] == 'd':
            d["/".join(q)].append("/".join(q) + '/' + row.split()[-1])

    @lru_cache(maxsize=-1)
    def sum(path):
        total = 0
        for value in d[path]:
            item = value.split('/')[-1].split()[0]
            if item[0].isnumeric():
                total += int(item)
            else:
                total += sum(value)
        return total

    new_total = 0

    for key in d.keys():
        total = sum(key)
        # print(key, total)
        # if total <= 100000:
        totals[key] = total
        new_total += total

    print(totals)
    total_space = totals['/']
    availible_space = 70000000 - total_space
    required_space = 30000000 - availible_space

    smallest = float("inf")
    for v in totals.values():
        if int(v) >= required_space:
            smallest = min(smallest, int(v))

    return smallest


if __name__ == '__main__':
    rows = open("7.txt").read().split('\n')
    print(solve_a(rows))
