from itertools import combinations
from functools import reduce

from src.utils import get_input_data


def get_sum_to(ls, val, order):
    for i in combinations(ls, order):
        if sum(i) == val:
            return reduce(lambda x, y: x * y, i)


if __name__ == '__main__':
    input_data = get_input_data("advent20/input1.txt")
    data = [int(i[0]) for i in input_data]
    print(get_sum_to(data, 2020, 2))
    print(get_sum_to(data, 2020, 3))
