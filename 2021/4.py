def solve_a(boards: list, numbers: list) -> int:
    """Mark numbers when called, return sum of non-called numbers"""
    n = len(boards)
    m = len(boards[0])
    o = len(boards[0][0])

    def check_board(boards, solved) -> tuple:
        """return true if a row or column is all 0"""
        n = len(boards[0])
        m = len(boards[0][0])
        for a, board in enumerate(boards):
            if solved[a]:
                continue
            for i in range(n):
                row, column = 0, 0
                for j in range(m):
                    row += int(board[i][j])
                    column += int(board[j][i])
                if row == 0 or column == 0:
                    solved[a] = True
                    return board

    def sum_board(board):
        """Add all values in the board together"""
        total = 0
        for row in board:
            for value in row:
                total += int(value)
        return total

    solved = [False] * len(boards)
    bingos = set()
    for number in numbers.split(","):
        print(number)
        for i in range(n):
            for j in range(m):
                for k in range(o):
                    if boards[i][j][k] == number:
                        boards[i][j][k] = 0
                    bingo = check_board(boards, solved)
                    if bingo:
                        sb = sum_board(bingo)
                        if sb not in bingos:
                            print(sb * int(number))
                            print(bingo)
                            print(bingos)
                            print(solved)
                            bingos.add(sb)


if __name__ == '__main__':
    numbers, *board = open("4.txt").read().split('\n\n')

    boards = [[x.split() for x in y.split("\n")] for y in board]
    # print(boards)
    print(solve_a(boards, numbers))
