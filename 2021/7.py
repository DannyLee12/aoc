from collections import defaultdict
import re


def solve_a(map: dict) -> int:
    """Return the number of bags that can contain a gold bag"""
    def bfs(node, visited=None):
        if not visited:
            visited = []

        queue = [node]

        while queue:
            node = queue.pop()
            if node not in visited:
                visited.append(node)

                neighbours = map[node]
                for n in neighbours:
                    if n == "shiny gold":
                        return True
                    queue.append(n)
        return False

    total = 0
    bags = list(map.keys())
    for bag in bags:
        if bfs(bag):
            total += 1

    return total


def solve_b(map: dict, node: tuple, total_bags: int=0) -> int:
    """Count total number of bags in a gold bag"""

    def dfs(node, visited=None):
        if not visited:
            visited = defaultdict(int)
            visited["shiny gold"] = 1

        q = [node]

        while q:
            ne = q.pop()
            if not ne:
                continue
            elif not map[ne[1]]:
                continue
            for n in map[ne[1]]:
                if not n:
                    continue
                else:
                    visited[n[1]] += int(n[0]) * int(visited[ne[1]])
                dfs(n, visited)
        print(visited)
        return sum(visited.values()) - 1

    return dfs(node)


if __name__ == '__main__':
    map = defaultdict(list)
    with open("7.txt") as f:
        for row in f:
            key, value = row.split(" bags contain")
            for x in value.split(","):
                r = re.match(r'.*\d (.+) bag.*', x)
                if r:
                    map[key].append(r.group(1).strip())
                else:
                    map[key].append(None)

    mapb = defaultdict(list)
    with open("7.txt") as f:
        for row in f:
            key, value = row.split(" bags contain")
            for x in value.split(","):
                r = re.match(r'.*(\d) (.+) bag.*', x)
                if r:
                    mapb[key].append((r.group(1).strip(), r.group(2).strip()))
                else:
                    mapb[key].append(None)

    # print(solve_a(map))
    print(solve_b(mapb, (1, "shiny gold")))
    print(9339)
