from typing import List


def parse_rule(s: str) -> (str, List[str]):
    colour, rules = s.rstrip('.\n').split(' contain ')
    return colour, rules.split(', ')


def parse_rules(data: List[str]) -> dict:
    d = {}
    for i in data:
        colour, rules = parse_rule(i)
        d[' '.join(colour.split(' ')[:2])] = {' '.join(rule.split(' ')[1:-1]) for rule in rules}
    return d


def parse_rules_2(data: List[str]) -> dict:
    def split_num_rule(x):
        x = x.split(' ')
        return int(x[0]), ' '.join(x[1:-1])
    d = {}
    for i in data:
        colour, rules = parse_rule(i)
        k = ' '.join(colour.split(' ')[:2])
        try:
            d[k] = [split_num_rule(rule) for rule in rules]
        except ValueError:
            d[k] = None

    return d


def part1(data):
    valid_bags = {'shiny gold'}
    old_num = 0
    new_num = len(valid_bags)
    while old_num != new_num:
        old_num = new_num
        for k, v in data.items():
            if len(valid_bags.intersection(v)) > 0:
                valid_bags.add(k)
        new_num = len(valid_bags)
    return len(valid_bags) - 1


def part2(data):
    def loop(col):
        if col is None:
            return 1
        else:
            return 1 + sum([n * loop(data[c]) for n, c in col])

    return loop(data['shiny gold']) - 1


if __name__ == '__main__':
    input_data = open("../../resources/advent20/input7.txt")
    input_data = input_data.readlines()

    d = parse_rules(input_data)
    print(part1(d))

    d = parse_rules_2(input_data)
    print(part2(d))
