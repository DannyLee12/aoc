
s = set()
with open("1.txt") as f:
    for row in f:
        s.add(int(row))

# Part 1
for i in s:
    if 2020 - int(i) in s:
        print((2020 - int(i)) * int(i))


# Part 2
for j in s:
    for k in s:
        if 2020 - int(j) - int(k) in s:
            print((2020 - int(j) - int(k)) * int(k) * int(j))

if __name__ == '__main__':
    pass
