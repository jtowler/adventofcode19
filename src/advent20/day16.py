import re
from functools import reduce


def check_valid(rs: dict, n):
    for r, ((a, b), (c, d)) in rs.items():
        if (n in range(a, b + 1)) or (n in range(c, d + 1)):
            return True
    return False


def check_valid_ticket(rs, ticket):
    for n in ticket:
        if not check_valid(rs, n):
            return False
    return True


def check_valid_rule(vals, a, b, c, d):
    for v in vals:
        if (v not in range(a, b + 1)) and (v not in range(c, d + 1)):
            return False
    return True


def get_valid_tickets(rs, tickets):
    return [ticket for ticket in tickets if check_valid_ticket(rs, ticket)]


def get_valid_rules(tickets, i, rs):
    vals = [ticket[i] for ticket in tickets]
    return [r for r, ((a, b), (c, d)) in rs.items() if check_valid_rule(vals, a, b, c, d)]


def get_actual_columns(options: dict):
    actual_columns = {}
    while len(options) > 0:
        new_actuals = {k: v[0] for k, v in options.items() if len(v) == 1}
        actual_columns.update(new_actuals)
        remove_vals = []
        for k, v in new_actuals.items():
            options.pop(k)
            remove_vals.append(v)
        options = {k: [v for v in vs if v not in remove_vals] for k, vs in options.items()}
    return actual_columns


def part1(rs, tickets):
    invalid = 0
    for ticket in tickets:
        for n in ticket:
            if not check_valid(rs, n):
                invalid += n
    return invalid


def part2(rs, tickets, target):
    valid_tickets = get_valid_tickets(rs, tickets)
    column_options = {i: get_valid_rules(valid_tickets, i, rs)
                      for i in range(len(valid_tickets[0]))}
    actual_columns = get_actual_columns(column_options)
    dep_inds = [k for k, v in actual_columns.items() if v.startswith('departure')]
    target_deps = [a for i, a in enumerate(target) if i in dep_inds]
    return reduce(lambda x, y: x * y, target_deps)


if __name__ == '__main__':
    input_data = open("../../resources/advent20/input16.txt", "r").read().split("\n")
    blanks = [i for i, a in enumerate(input_data) if a == '']
    rules = {}
    pattern = r"([a-z\s]+): (\d+)-(\d+) or (\d+)-(\d+)"
    for i in input_data[:blanks[0]]:
        match = re.match(pattern, i)
        rules[match.group(1)] = ((int(match.group(2)), int(match.group(3))),
                                 (int(match.group(4)), int(match.group(5))))

    my_ticket = [int(i) for i in input_data[blanks[0] + 2].split(',')]
    nearby_tickets = [[int(j) for j in i.split(',')] for i in input_data[blanks[1] + 2:]]

    answer1 = part1(rules, nearby_tickets)
    answer2 = part2(rules, nearby_tickets, my_ticket)

    print(answer1)  # 21980
    print(answer2)  # 1439429522627
