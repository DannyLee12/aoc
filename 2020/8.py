
def solve_a(l: list) -> int:
    """Determine the value once all instructions have been run once"""
    s = set()
    acc = 0
    i = 0
    while 1:
        if i in s:
            return None
        s.add(i)
        if l[i][:3] == "acc":
            acc += int(l[i][4:])
        elif l[i][:3] == "jmp":
            i += int(l[i][4:]) - 1
        elif l[i][:3] == "nop":
            pass
        i += 1
        if i == len(l):
            return acc


if __name__ == '__main__':
    input = open("8.txt").read().split('\n')
    # print(solve_a(input))
    ret = None
    jmp_index = -1
    while not ret:
        solve = False
        in2 = input[:]
        for i in range(jmp_index + 1, len(input)):
            if in2[i][:3] == "nop":
                in2[i] = "jmp " + in2[i][4:]
                jmp_index = i
                solve = True
                break
            elif in2[i][:3] == "jmp":
                in2[i] = "nop " + in2[i][4:]
                jmp_index = i
                solve = True
                break
        if solve:
            ret = solve_a(in2)
    print(ret)
