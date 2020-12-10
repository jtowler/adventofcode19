from functools import reduce
from typing import List


def part1(data):
    diffs = [i - j for i, j in zip(data + [data[-1] + 3], [0] + data)]
    return diffs.count(1) * diffs.count(3)


def part2(sorted_adapters: List[int]) -> int:
    diffs = [i - j for i, j in zip(sorted_adapters, [0] + sorted_adapters)] + [3]
    runs1 = []
    run = 0
    for i in diffs:
        if i == 3:
            runs1.append(run)
            run = 0
        else:
            run += 1
    configuration_map = {0: 1, 1: 1, 2: 2, 3: 4, 4: 7}
    configurations = map(configuration_map.get, runs1)
    return reduce(lambda x, y: x * y, configurations)


if __name__ == '__main__':
    input_data = open("../../resources/advent20/input10.txt")
    input_data = [int(i.strip('\n')) for i in input_data.readlines()]
    sorted_test = sorted(input_data)
    print(part1(sorted_test))
    print(part2(sorted_test))
