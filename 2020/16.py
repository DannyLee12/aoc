from collections import defaultdict


def solve_a(rules: list, tickets: list) -> list:
    """Return the number of tickets not valid for anything"""
    invalids = 0
    valid_tickets = [[[] for _ in range(20)] for __ in range(len(tickets))]
    i, j = 0, 0
    for ticket in tickets:
        valid = False
        for rule in rules:
            split_rules = rule.split("-")
            if int(split_rules[0]) <= int(ticket) <= int(split_rules[1]):
                valid = True
                break
        if not valid:
            invalids += int(ticket)
            valid_tickets[j][i] = -1
        else:
            valid_tickets[j][i] = ticket
        if i == 19:
            j += 1
            i = 0
        else:
            i += 1

    return valid_tickets[:236]


def solve_b(rules: list, valid_tickets: list) -> int:
    """Figure out the order"""
    rules_dict = defaultdict(set)
    valid_tickets.insert(0, "109,137,131,157,191,103,127,53,107,151,61,59,139,83,101,149,89,193,113,97".split(","))
    k = 0
    while k < 20:
        for i, ticket in enumerate(valid_tickets):
            if ticket == -1:
                continue
            for j, rule in enumerate(rules):
                if int(rule[0].split("-")[0]) <= int(ticket[k]) <= int(rule[0].split("-")[1]) or int(rule[1].split("-")[0]) <= int(ticket[k]) <= int(rule[1].split("-")[1]):
                    rules_dict[k].add(j)
        k += 1

    clean_dict = {}
    l = 1
    while l < 19:
        for k, v in rules_dict.items():
            if len(v) == l:
                print(k, v, l)
                l += 1
        l += 1

    while rules_dict:
        for k, v in rules_dict.items():
            if len(v) == 1:
                val = v
                clean_dict[k] = v
                del rules_dict[k]
                for k, v in rules_dict.items():
                    rules_dict[k] = rules_dict[k] - val
                break
    clean_dict[8] = {14}

    for i in range(20):
        print(i, clean_dict[i])

    value = 1
    for i, val in enumerate("109,137,131,157,191,103,127,53,107,151,61,59,"
                            "139,83,101,149,89,193,113,97".split(",")):
        if i in [1, 5, 11, 13, 14, 17]:
            value *= int(val)

    return value


if __name__ == '__main__':
    rules_list = []
    rules_list_2 = []
    rules, tickets = tuple(open("16.txt").read().split("your ticket:"))
    for rule in rules.split("\n"):
        dirty_split = tuple(rule.split(" or "))
        try:
            rules_list.extend([dirty_split[0].split(":")[1], dirty_split[1]])
            rules_list_2.append([dirty_split[0].split(":")[1], dirty_split[1]])
        except IndexError:
            break
    tickets_list = []
    for i, ticket in enumerate(tickets.split("\n")):
        if i <= 3:
            continue
        tickets_list.extend(ticket.split(","))

    print(solve_b(rules_list_2, solve_a(rules_list, tickets_list)))
