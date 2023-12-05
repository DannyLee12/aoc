from math import inf


def solve_a(input):
    total = 0
    for row in input:
        min_red, min_blue, min_green = 0, 0, 0
        game_no, game = row.split(':')
        game_no = int(game_no[5:])
        for g in game.split(';'):
            for colour in g.strip().split(','):
                no, col = colour.strip().split(' ')
                if col == 'red':
                    min_red = max(min_red, int(no))
                elif col == 'green':
                    min_green= max(min_green, int(no))
                elif col == 'blue':
                    min_blue = max(min_blue, int(no))

        total += min_red * min_blue * min_green


    return total



if __name__ == '__main__':
    input = open("2.txt").read().split('\n')
    print(solve_a(input))
