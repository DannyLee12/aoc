def solve_a(l: list) -> int:
    """Return the max seat id (row x 8) + column"""
    max_seat_id = 0
    def row_search(start, stop, rows, i):
        midpoint = (start + stop) // 2
        if i == 7:
            if rows == "F":
                return start
            else:
                return stop
        if rows[i] == "F":
            return row_search(start, midpoint, rows, i + 1)
        elif rows[i] == "B":
            return row_search(midpoint, stop, rows, i + 1)

    def col_search(start, stop, rows, j):
        midpoint = (start + stop) // 2
        if j == 3:
            if rows == "L":
                return start
            else:
                return stop
        if rows[j] == "L":
            return col_search(start, midpoint, rows, j + 1)
        else:
            return col_search(midpoint, stop, rows, j + 1)

    seat_ids = set()
    for item in l:
        row = row_search(0, 127, item[:7], 0)
        col = col_search(0, 7, item[7:], 0)
        max_seat_id = max(max_seat_id, (row * 8) + col)
        seat_ids.add((row * 8) + col)

    for k in range(max_seat_id, 0, -1):
        if k not in seat_ids:
            break

    return k


if __name__ == '__main__':
    with open("5.txt") as f:
        rows = f.readlines()

    print(solve_a(rows))
