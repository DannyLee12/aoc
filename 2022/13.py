from itertools import zip_longest
import json


def compare(x, y):
    """Return True if in correct order"""
    for l, r in zip_longest(x, y):
        if l is None:
            return True
        elif r is None:
            return False
        elif isinstance(l, list) and isinstance(r, list):
            val = compare(l, r)
            if val is not None:
                return val
        elif isinstance(l, list):
            val = compare(l, [r])
            if val is not None:
                return val
        elif isinstance(r, list):
            val = compare([l], r)
            if val is not None:
                return val
        elif l < r:
            return True
        elif l > r:
            return False


def solve_a(items):
    total = 0
    for i, item in enumerate(items):
        i1, i2 = item.split('\n')
        total += (i + 1) * compare(json.loads(i1), json.loads(i2))

    return total


def merge_sort(l: list) -> list:
    """Merge sort a list"""
    def merge(l1, l2, l=None):
        if not l:
            l = []
        if not l1:
            return l2
        if not l2:
            return l1
        if compare(l1[0], l2[0]):
            l.append(l1[0])
            l.extend(merge(l2, l1[1:]))
        else:
            l.append(l2[0])
            l.extend(merge(l2[1:], l1))

        return l

    def _mergesort(l):
        if len(l) <= 1:
            return l

        middle = len(l) // 2
        left = _mergesort(l[:middle])
        right = _mergesort(l[middle:])

        return merge(left, right)

    return _mergesort(l)


def solve_b(items):
    print(items)
    items = merge_sort(items)

    return (items.index([[2]]) + 1) * (items.index([[6]]) + 1)


if __name__ == '__main__':
    items = open("13.txt").read().split('\n\n')
    new_items = [json.loads(x) for x in open("13.txt").read().split('\n') if x != '']
    print(solve_a(items))
    print(solve_b(new_items))