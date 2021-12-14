from collections import defaultdict


def solve_a(routes: list) -> int:
    """Return the max number of paths that visit small caves once"""
    paths = []
    d = defaultdict(list)
    for route in routes:
        d[route[0]].append(route[1])
        d[route[1]].append(route[0])

    def dfs(graph, node, path, twice: bool=False):
        path.append(node)
        if 'end' in path:
            paths.append(path)
            return path

        for n in graph[node]:
            if n in path and n.islower():
                if not twice and not n == 'start' and not n == 'end':
                    twice = True
                else:
                    continue

            dfs(graph, n, list(path), twice)

        return path

    dfs(d, 'start', [], False)

    return paths


if __name__ == '__main__':
    routes = [x.split('-') for x in open("12.txt").read().split("\n")]
    paths = solve_a(routes)
    count = 0
    with open("a.txt") as f:
        i = f.read().split("\n")
        for row in i:
            if row.split(',') not in paths:
                print(row)
                count += 1
                print(count)
    print(len(paths))
