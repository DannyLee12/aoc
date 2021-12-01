def solve_a(l: list) -> int:
    """Count the total number of people that answered yes"""
    total = 0
    for group in l:
        questions = set()
        for person in group.split("\n"):
            questions = questions.union(set(person))
        total += len(questions)

    return total


def solve_b(l: list) -> int:
    """Count the groups that answered yes"""
    total = 0
    for group in l:
        q = set()
        for i, person in enumerate(group.split('\n')):
            if i == 0:
                q = set(person)
            else:
                q = q.intersection(set(person))
        total += len(q)

    return total


if __name__ == '__main__':
    with open("6.txt") as f:
        input = f.read().split("\n\n")

    print(solve_a(input))
    print(solve_b(input))
