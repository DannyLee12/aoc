from collections import deque


class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

    def __repr__(self):
        return str(self.val)

    def find(self, val):
        node = self
        while node.val != val:
            node = node.next
        return node

    def move(self, length):
        i = self.val % (length - 1)
        node = self
        prev = self.prev

        while i:
            # prev
            next_node = node.next
            prev.next = next_node
            next_node.prev = prev
            # curr
            node = next_node
            next_node = node.next
            node.next = self
            self.prev = node
            # next
            self.next = next_node
            next_node.prev = self

            prev = node
            node = node.next
            i -= 1


if __name__ == '__main__':
    input = list(map(int,open("20.txt").read().split('\n')))
    n = len(input)
    head = Node(input[0] * 811589153)
    node = head
    nodes = []
    for i, val in enumerate(input):
        if i == 0:
            continue
        new_node = Node(val * 811589153)
        new_node.prev = node
        node.next = new_node
        nodes.append(node)
        node = node.next

    nodes.append(node)

    node.next = head
    head.prev = node

    for i in range(10):
        print("Mix", i)
        for node in nodes:
            node.move(n)

    node = node.find(0)
    total = 0
    for _ in range(3):
        for _ in range(1000 % n):
            node = node.next
        total += node.val

    print(total)
