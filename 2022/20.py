from collections import deque


class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

    def __repr__(self):
        return str(self.val)

    def move(self, length):
        i = self.val % (length - 1)
        node = self
        while i:
            node = node.next
            i -= 1

        prev = self.prev
        prev.next = self.next
        self.prev = node
        self.next = node.next

if __name__ == '__main__':
    input = list(map(int,open("20.txt").read().split('\n')))
    n = len(input)
    head = Node(input[0])
    node = head
    nodes = []
    for i, val in enumerate(input):
        if i == 0:
            continue
        new_node = Node(val)
        new_node.prev = node
        node.next = new_node
        nodes.append(node)
        node = node.next

    node.next = head
    head.prev = node

    for node in nodes:
        head = node

        val = ""
        for _ in range(n):
            val += str(head.val) + ", "
            head = head.next

        print(val)

        node.move(n)
