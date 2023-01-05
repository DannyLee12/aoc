from collections import defaultdict, deque
import re
from functools import cache


def solve_a(F, g, flows):
    @cache
    def dfs(valve, time, visited):
        if time <= 1:
            return 0
        res = 0
        for link in g[valve]:
            res = max(res, dfs(link, time - 1, visited))
        if valve not in visited and flows[valve] > 0:
            visited = tuple(sorted([*visited, valve]))
            res = max(res, dfs(valve, time - 1, visited) + flows[valve] * (time - 1))

        return res

    return dfs('AA', 30, tuple())





if __name__ == '__main__':

    import sys, re
    lines = [re.split('[\\s=;,]+', x) for x in open("16.txt").read().splitlines()]
    G = {x[1]: set(x[10:]) for x in lines}
    F = {x[1]: int(x[5]) for x in lines if int(x[5]) != 0}
    I = {x: 1<<i for i, x in enumerate(F)}
    T = {x: {y: 1 if y in G[x] else float('+inf') for y in G} for x in G}
    for k in T:
        for i in T:
            for j in T:
                T[i][j] = min(T[i][j], T[i][k]+T[k][j])
    input = open("16.txt").read().split('\n')
    flows = {}
    g = defaultdict(list)
    for row in input:
        valve = row.split()[1]
        flow = int(re.findall(r'rate=(\d+);', row)[0])
        flows[valve] = flow
        valves = [x.strip() for x in row.split("valve")[-1].lstrip('s').split(",")]
        g[valve].extend(valves)

    # Floyd Warshall
    # distances to valves

    # F = {x: {y: 1 if y in g[x] else float('inf')} for x,y in g.items()}
    F = {}
    for x, y in g.items():
        F[x] = {}
        for valve in g.keys():
            if valve in y:
                F[x][valve] = 1
            else:
                F[x][valve] = float('inf')

        for k in F:
            for i in F:
                for j in F:
                    F[i][j] = min(F[i][j], F[i][k]+F[k][j])


    print(solve_a(F, g, flows))
