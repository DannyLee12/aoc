from collections import defaultdict


def solve_a(graph):
    def dfs(node):
        if isinstance(graph[node], int):
            return graph[node]
        else:
            for op in ["+", "-", "/", "*", "=="]:
                if op in graph[node]:
                    split = graph[node].split(op)
                    return eval(str(dfs(split[0].strip())) + op + str(dfs(split[1].strip())))

    return dfs('root')


def solve_b(graph):
    graph["humn"] = "humn"

    def reduce(node):
        for op in ["+", "-", "/", "*", "=="]:
            if op in graph[node]:
                split = graph[node].split(op)
                # print(split)
                graph[node] = reduce(str(graph[split[0].strip()])) + op + str(reduce(graph[split[1].strip()]))
        return node

    return reduce("root")


if __name__ == '__main__':
    monkeys = open("21.txt").read().split('\n')
    graph = defaultdict(str)
    for monkey in monkeys:
        x, y = monkey.split(':')
        try:
            graph[x] = int(y)
        except:
            graph[x] = y.strip()
    # graph = [[x + y for x, y in monkey.split(":")] for monkey in monkeys]
    # print(graph)
    # print(solve_a(graph))
    print(solve_b(graph))
    print(graph['root'])
