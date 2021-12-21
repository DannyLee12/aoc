import json


def solve_a(input: str) -> int:
    """Return the magtitude of the snail sum"""
    items = []

    def reduce(s_items: str) -> str:
        """Reduce the string based on rules"""
        s_items = s_items.replace(' ', '')
        new_str = ''
        open = 0
        n = len(s_items)
        i = 0
        while i < n:
            # print(new_str)
            char = s_items[i]
            if char == '[':
                open += 1
            elif char == ']':
                open -= 1
            if open >= 5 and char == '[':
                # Explode items nested within 4 pairs
                if s_items[i+1] == '[':
                    i += 1
                    continue
                open -= 1
                left = int(s_items[i + 1])
                right = int(s_items[i + 3])
                for l_pos in range(len(new_str) - 1, 0, -1):
                    if new_str[l_pos].isnumeric():
                        val = int(new_str[l_pos]) + left
                        if val > 9:
                            if val % 2 == 0:
                                val = f"[{val//2},{val//2}]"
                            else:
                                val = f"[{val//2},{(val+1)//2}]"
                        new_str = new_str[:l_pos] + str(val) + new_str[l_pos + 1:]
                        break
                for r_pos in range(i + 4, n):
                    if s_items[r_pos].isnumeric():
                        val = int(s_items[r_pos]) + right
                        if val > 9:
                            if val % 2 == 0:
                                val = f"[{val//2},{val//2}]"
                            else:
                                val = f"[{val//2},{(val+1)//2}]"
                        s_items = s_items[:r_pos] + str(val) + s_items[r_pos + 1:]
                        break
                # Replace nested items with a 0
                new_str += "0"
                i += 4
            else:
                new_str += char
            i += 1
            n = len(s_items)

        return new_str

    items = ''
    for i, row in enumerate(input):
        if i > 0:
            items = '[' + items + ',' + row + ']'
            items = reduce(items)
        else:
            items = row


    return items


if __name__ == '__main__':
    input = open('18.txt').read().split("\n")
    print(solve_a(input))
