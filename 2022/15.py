def solve_a(rows, chosen_row):
    cant_be = set()
    beacons = set()
    for row in rows:
        sensor, beacon = row.split(":")
        s_x, s_y = get_coords(sensor)
        b_x, b_y = get_coords(beacon, False)
        if b_y == chosen_row:
            beacons.add(b_x)
        manhat_distance = abs(s_x - b_x) + abs(s_y - b_y)
        if abs(chosen_row - s_y) <= manhat_distance:
            manhat_distance -= abs(chosen_row - s_y)
            cant_be.add(s_x)
            i = 1
            while manhat_distance > 0 and (s_x - i >= 0 or s_x + i <= 4_000_000):
                cant_be.add(s_x - i)
                cant_be.add(s_x + i)
                manhat_distance -= 1
                i += 1

    # s = set(range(20))

    for i in range(4_000_001):
        if i not in cant_be:
            return i


def solve_b(rows, max=20):
    # Get max ranges and start points
    # check all points in these ranges
    sensors = []
    beacons = set()
    for row in rows:
        sensor, beacon = row.split(":")
        s_x, s_y = get_coords(sensor)
        b_x, b_y = get_coords(beacon, False)
        manhat_distance = abs(s_x - b_x) + abs(s_y - b_y)
        sensors.append([s_x, s_y, manhat_distance])
        beacons.add(f'{b_x}.{b_y}')

    # y2 - y1 = m(x2 - x1)

    def possible(x, y):
        valid = 0 <= x < 4_000_000 and 0 <= y < 4_000_000
        if not valid:
            return False
        if f'{x}.{y}' in beacons:
            return False
        for i, j, d in sensors:
            if abs(x - i) + abs(y - j) <= d:
                return False
        return True

    for sx, sy, d in sensors:
        # Start point left of sensor
        dx, dy = sx - (d + 1), sy
        for mx, my in [(1, -1), (1, 1)]:
            for i in range(d + 2):
                x, y = dx + (mx * i), dy + (my * i)
                if possible(x, y):
                    return 4_000_000 * x + y
        # start point right of sensor
        dx, dy = sx + d + 1, sy
        for mx, my in [(-1, 1), (-1, -1)]:
            for j in range(d + 2):
                x, y = dx + (mx * j), dy + (my * j)
                if possible(x, y):
                    return 4_000_000 * x + y


def get_coords(sensor, s=True):
    x, y = sensor.split(",")
    if s:
        return map(int, [x.lstrip("Sensor at x="), y.lstrip(" y=")])
    else:
        return map(int, [x.lstrip("closest beacon is at x="), y.lstrip(" y=")])


if __name__ == '__main__':
    rows = open("15.txt").read().split('\n')
    # print(solve_a(rows, 2000000))
    print(solve_b(rows))
