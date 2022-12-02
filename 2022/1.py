import heapq


def task_1(rows):
    max_val = 0
    for row in rows:
        max_val = max(max_val, sum(list(map(int, row.split('\n')))))

    return max_val


def task_2(rows):
    heap = []
    for row in rows:
        heapq.heappush(heap, sum(list(map(int, row.split('\n')))))

    return sum(heapq.nlargest(3, heap))


if __name__ == '__main__':
    with open("1.txt") as f:
        rows = f.read().split("\n\n")
    print(rows)
    print(task_1(rows))
    print(task_2(rows))
