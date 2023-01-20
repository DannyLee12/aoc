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
    graph['root'] = graph['root'].replace("+", '==')

    def reduce(node):

        value = graph[node]

        # Int
        if isinstance(value, int):
            return value
        if value == 'humn':
            return 'humn'
        # split into two
        for op in ["+", "-", "/", "*", '==']:
            if op in value:
                t1, t2 = value.split(op)
                t1, t2 = reduce(t1.strip()), reduce(t2.strip())
                calc = str(t1) + op + str(t2)
                try:
                    graph[node] = eval(calc)
                except:
                    graph[node] = "(" + calc + ")"
                return graph[node]
    calc = reduce("root")

    low, high = 1, 100_000_000_000_000_000_000_000_000_000_000_000

    target = float(calc.split("==")[1][:-1])
    equation = calc.split("==")[0][1:]
    while low < high:

        value = (high + low) // 2

        result = eval(equation.replace("humn", str(value)))
        if result == target:
            return value
        if result < target:
            high = value
        else:
            low = value + 1

    return low, high


if __name__ == '__main__':
    monkeys = open("21.txt").read().split('\n')
    graph = defaultdict(str)
    for monkey in monkeys:
        x, y = monkey.split(':')
        try:
            graph[x] = int(y)
        except:
            graph[x] = y.strip()
    print(solve_a(graph))
    print(solve_b(graph))
