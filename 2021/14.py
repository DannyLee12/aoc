from collections import defaultdict


def solve_a(element: str, rules_list: list, steps: int) -> int:
    """Return the difference between the most & least common elements"""

    rules = {}
    for rule in rules_list:
        find, replace = rule.split(" -> ")
        rules[find] = replace

    for _ in range(steps):
        print(_)
        shift = 0
        element_old = element[:]
        n = len(element_old)
        for i in range(n - 1):
            if element_old[i:i+2] in rules:
                element = element[:i + 1 + shift] + rules[element_old[i:i+2]] + element[i+1 + shift:]
                shift += 1

    d = defaultdict(int)
    for c in element:
        d[c] += 1

    return(max(d.values()) - min(d.values()))


def solve_b(element: str, rules_list: list, steps: int) -> int:
    """More efficient part A"""
    rules = {}
    for rule in rules_list:
        find, replace = rule.split(" -> ")
        rules[find] = [find[0] + replace, replace + find[-1]]

    n = len(element)
    d = defaultdict(int)
    for i in range(n-1):
        d[element[i:i+2]] += 1

    for _ in range(steps):
        d_new = defaultdict(int)
        for k, v in d.items():
            if k in rules:
                for val in rules[k]:
                    d_new[val] += d[k]

        d = d_new

    d1 = defaultdict(int)
    for k, v in d.items():
        for char in k:
            d1[char] += v
            break

    return(max(d1.values()) - min(d1.values())) - 1


if __name__ == '__main__':
    element, rules = open("14.txt").read().split("\n\n")

    print(solve_b(element, rules.split("\n"), 40))
