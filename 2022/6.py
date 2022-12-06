from collections import deque


def solve_a(buffer, chars):
    q = deque()
    for i, char in enumerate(buffer):
        q.appendleft(char)
        if len(q) >= chars + 1:
            q.pop()
            if len(q) == len(set(q)):
                return i + 1


if __name__ == '__main__':
    buffer = open("6.txt").read()

    print(solve_a(buffer, 4))
    print(solve_a(buffer, 14))

