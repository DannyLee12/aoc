def solve_a(input: str, iterations: int=0) -> str:
    """Solve for part a"""
    l = list(input)
    pos = 0
    val = l[pos]
    while iterations:
        pickup = [l[(pos + 1) % 9]] + [l[(pos + 2) % 9]] + [l[(pos + 3) % 9]]
        value = str(int(l[pos]) - 1)
        if value == '0':
            value = '9'
        while value in pickup:
            value = str(int(value) - 1)
            if value == '0':
                value = '9'
        nl = []
        for item in l:
            if item in pickup:
                continue
            if item != value:
                nl.append(item)
            elif item == value:
                nl.append(value)
                nl.extend(pickup)

        l = nl[:]
        iterations -= 1
        pos = (l.index(val) + 1) % 9
        val = l[pos]

    i1 = l.index('1')

    return "".join(l[i1:] + l[:i1])


class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def __repr__(self):
        return self.data

    def pickup_list(self):
        l = []
        n = self
        for i in range(3):
            l.append(n.data)
            n = n.next_node
        return l


class CircularLinkedList(object):
    hash = {}
    def __init__(self, head=None):
        self.head = head

    def pprint(self):
        temp = self.head
        while temp.next_node:
            print(temp, ' -> ', end='')
            temp = temp.next_node
            if temp == self.head:
                break
        print("")

    def find_node(self, s: str) -> Node:
        """Find and return a particular node"""
        temp = self.head
        while temp.data != s:
            temp = temp.next_node
        return temp


def solve_b(input: str, iterations=1_000_000) -> int:
    """Return the product of the two cups to the right of 1"""
    cache = {}
    temp = Node(input[-1])
    for i, x in enumerate(list(input) + [str(x) for x in range(10, 1_000_001)]):
        n = Node(x)
        cache[x] = n
        temp.next_node = n
        if i == 0:
            ll = CircularLinkedList(n)
        temp = n
    temp.next_node = ll.head
    n = ll.head

    while iterations:
        dest = str(int(n.data) - 1)
        if dest == '0':
            dest = '1000000'

        pickup1 = n.next_node
        pickup3 = pickup1.next_node.next_node
        pickup3_next = pickup3.next_node
        pickup = pickup1.pickup_list()

        while dest in pickup:
            dest = str(int(dest) - 1)
            if dest == '0':
                dest = '1000000'

        dest_node = cache[dest]
        if dest_node.data != dest:
            ll.head = dest_node
            dest_node = ll.find_node(dest)

        temp = dest_node.next_node
        dest_node.next_node = pickup1
        pickup3.next_node = temp
        n.next_node = pickup3_next
        n = n.next_node

        iterations -= 1

    node1 = ll.find_node('1')

    return int(node1.next_node.data) * int(node1.next_node.next_node.data)


if __name__ == '__main__':
    print(solve_a("156794823", 100))
    print(solve_b("156794823", 10_000_000))
