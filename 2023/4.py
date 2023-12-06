def solve_a(input):
    total = 0
    for row in input:
        _, numbers = row.split(':')
        winning, mine = numbers.split('|')
        winning = {int(x) for x in winning.split()}
        score = 0
        for number in mine.split():
            if int(number) in winning:
                if not score:
                    score = 1
                else:
                    score *= 2
        total += score

    return total

def solve_b(input):
    output =  [1] * len(input)
    for i, row in enumerate(input):
        _, numbers = row.split(':')
        winning, mine = numbers.split('|')
        winning = {int(x) for x in winning.split()}
        i_ = i + 1
        copy = output[i]
        for number in mine.split():
            if int(number) in winning:
                output[i_] += copy
                i_ += 1


    return sum(output)



if __name__ == '__main__':
    input = open("4.txt").read().split('\n')
    print(solve_a(input))
    print(solve_b(input))