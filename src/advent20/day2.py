from src.utils import get_input_data
import re


def parse_rule(s):
    pattern = "(\d+)-(\d+) (\w): (\w+)"
    match = re.match(pattern, s)
    return int(match.group(1)), int(match.group(2)), match.group(3), match.group(4)


def rule_1(s):
    min_val, max_val, character, password = parse_rule(s)
    char_count = password.count(character)
    return min_val <= char_count <= max_val


def rule_2(s):
    index1, index2, character, password = parse_rule(s)
    index1 -= 1
    index2 -= 1
    char1 = password[index1] == character
    char2 = password[index2] == character
    return sum([char1, char2]) == 1


if __name__ == '__main__':
    input_data = get_input_data("advent20/input2.txt")
    print(sum([rule_1(i[0]) for i in input_data]))
    print(sum([rule_2(i[0]) for i in input_data]))
