from collections import deque

def solve_a(rows):
    q = deque()
    x = 1
    i = 2
    total = 0
    while i <= 220:
        for row in rows:
            if len(q) >= 2:
                x += q.pop()
            if row[0] == 'a':
                q.appendleft(int(row.split()[1]))
                q.appendleft(0)
            else:
                q.appendleft(0)
            if (i - 20) % 40 == 0:
                total += i * x
            i += 1
            if i > 220:
                break

    return total


def solve_b(rows):
    output = ""
    q = deque()
    x = 1
    i = 1
    pixel = 0
    while i < 220:
        for row in rows:
            if row[0] == 'a':
                q.appendleft(int(row.split()[1]))
                q.appendleft(0)
            else:
                q.appendleft(0)

            if pixel in {x - 1, x, x + 1}:
                output += '#'
            else:
                output += '.'
            if i % 40 == 0:
                pixel = -1
                # return output
                output += '\n'
            if len(q) > 2:
                x += q.pop()
            i += 1
            pixel += 1

            if i > 240:
                break

    return output




if __name__ == '__main__':
    rows = open("10.txt").read().split('\n')
    print(solve_a(rows))
    print(solve_b(rows))
