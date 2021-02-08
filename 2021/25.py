
if __name__ == '__main__':
    val = 1
    loop = 0
    while val != 8335663:
        loop += 1
        val *= 7
        val %= 20201227

    val2 = 1
    loop2 = 0
    while val2 != 8614349:
        loop2 += 1
        val2 *= 7
        val2 %= 20201227

    loops = loop
    val3 = 1
    while loops:
        # print(val3)
        val3 *= 8614349
        val3 %= 20201227
        loops -= 1

    print(loop)
    print(loop2)
    print(val3)
