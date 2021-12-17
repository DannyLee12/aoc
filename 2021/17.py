def solve_a(t_x: tuple, t_y: tuple, b: bool=True) -> int:
    """Return the max y pos that goes through the Target area"""
    maxs = []
    vals = 0
    points = []
    for x in range(1, 1000):
        for y in range(-100, 1000):
            point = [0, 0]
            init_val = (x, y)
            vx, vy = x, y
            max_y = 0
            while point[0] <= max(t_x) and point[1] >= min(t_y):
                point[0] += vx
                point[1] += vy
                max_y = max(max_y, point[1])
                if min(t_x) <= point[0] <= max(t_x) and min(t_y) <= point[1] <= max(t_y):
                    # print(init_val)
                    vals += 1
                    points.append(init_val)
                    maxs.append(max_y)
                    break
                if vx < 0:
                    vx += 1
                elif vx > 0:
                    vx -= 1
                else:
                    if not min(t_x) <= point[0] <= max(t_x):
                        break
                vy -= 1

    if b:
        return vals

    return max(maxs)


if __name__ == '__main__':
    x = 288, 330
    y = -96, -50

    print(solve_a(x, y))

