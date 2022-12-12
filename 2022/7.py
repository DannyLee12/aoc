from collections import defaultdict
from functools import lru_cache

def solve_a(rows):
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
            d[q[-1]].append(row)
        elif row[0] == 'd':
            d[q[-1]].append(row.split()[-1])

    @lru_cache(maxsize=-1)
    def sum(path):
        total = 0
        vals = sorted(d[path])
        for item in vals:
            if item[0].isnumeric():
                total += int(item.split()[0])
            else:
                total += sum(item)
            if total > 100000:
                return 100001
        return total

    new_total = 0

    for key in d.keys():
        total = sum(key)
        # print(key, total)
        if total <= 100000:
            new_total += total

    return new_total


if __name__ == '__main__':
    rows = open("7.txt").read().split('\n')
    print(solve_a(rows))
