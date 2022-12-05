from collections import deque

stacks = [deque() for _ in range(9)]
from string import ascii_uppercase


def solve_a(instructions):
    for instruction in instructions.split('\n'):
        # move x from y to z
        _, m, __, f, ___, t = instruction.split(" ")
        for _ in range(int(m)):
            stacks[int(t) - 1].appendleft(stacks[int(f) - 1].popleft())

    return "".join([stacks[x][0] for x in range(9)])


def solve_b(instructions):
    for instruction in instructions.split('\n'):
        # move x from y to z
        _, m, __, f, ___, t = instruction.split(" ")
        temp_stack = []
        for _ in range(int(m)):
            temp_stack.append(stacks[int(f) - 1].popleft())
        while temp_stack:
            stacks[int(t) - 1].appendleft(temp_stack.pop())

    return "".join([stacks[x][0] for x in range(9)])


if __name__ == '__main__':
    setup, instructions = open("5.txt").read().split('\n\n')
    for row in setup.split('\n'):
        for i, char in enumerate(row):
            if char in ascii_uppercase:
                stacks[(i - 1)//4].append(char)

    print(solve_a(instructions))
    print(solve_b(instructions))
