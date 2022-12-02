def solve_a(rows):
    scores = {'A': {'X': 3, 'Y': 6, 'Z': 0},
              'B': {'X': 0, 'Y': 3, 'Z': 6},
              'C': {'X': 6, 'Y': 0, 'Z': 3}}
    pick = {'X': 1, 'Y': 2, 'Z': 3}
    total = 0
    for row in rows:
        total += scores[row[0]][row[2]] + pick[row[2]]

    return total


def solve_b(rows):
    scores = {'A': {'X': 0 + 3, 'Y': 3 + 1, 'Z': 6 + 2},
              'B': {'X': 0 + 1, 'Y': 3 + 2, 'Z': 6 + 3},
              'C': {'X': 0 + 2, 'Y': 3 + 3, 'Z': 6 + 1}}

    return sum(scores[row[0]][row[2]] for row in rows)

if __name__ == '__main__':
    rows = open('2.txt').read().split('\n')
    print(solve_a(rows))
    print(solve_b(rows))
