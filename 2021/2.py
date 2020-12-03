# Part 1
def _is_valid_1(s: str, c: str, i: (int, int)) -> bool:
    """
    Return if the password is valid

    Return True if there are between i[0] and i[1] instances
    of c in s
    """
    return int(i[0]) <= s.count(c) <= int(i[1])


# Part 2
def _is_valid_2(s: str, c: str, i: (int, int)) -> bool:
    """
    Return if the password is valid
    Return true if the password has c at either position i[0] OR i[1]
    """
    return (s[int(i[0]) - 1] == c and s[int(i[1]) - 1] != c) or (s[int(i[0]) - 1] != c and s[int(i[1]) - 1] == c)


total_valid = 0

with open("2.txt") as f:
    for row in f:
        # Split on whitespace
        split_row = row.split()
        if _is_valid_2(split_row[-1], split_row[1][:-1], split_row[0].split("-")):
            total_valid += 1

print(total_valid)

if __name__ == '__main__':
    pass
