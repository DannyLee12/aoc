from collections import deque


def solve_a(items, operations, tests):
    """Solve a"""
    total = 10000
    i = 0
    n = len(operations)
    inspections = [0] * n
    divtotal = 1
    for x in tests:
        divtotal *= x[0]
    while total:
        while items[i]:
            item, operation, test = items[i].popleft(), operations[i], tests[i]
            if operation == ' * ':
                newval = item * item
            else:
                newval = eval(str(item) + operation)
            newval %= divtotal
            if newval % test[0] == 0:
                items[test[1]].append(newval)
            else:
                items[test[2]].append(newval)
            inspections[i] += 1

        i += 1
        if i >= n:
            total -= 1
            i = 0

    inspections.sort()

    return inspections[-1] * inspections[-2]


if __name__ == '__main__':
    monkeys = open("11.txt").read().split('\n\n')
    items = [deque() for _ in range(len(monkeys))]
    operations = [deque() for _ in range(len(monkeys))]
    tests = [deque() for _ in range(len(monkeys))]
    for i, monkey in enumerate(monkeys):
        rows = monkey.split('\n')
        items[i] = deque(map(int, rows[1].split(':')[1].split(',')))
        operations[i] = str(rows[2].split('old')[1])
        tests[i] = list(map(int, (rows[3].split(' ')[-1], rows[4].split(' ')[-1], rows[5].split(' ')[-1])))

    print(solve_a(items, operations, tests))
