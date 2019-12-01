import math

from src.utils import get_input_data


def calc_fuel(mass: int):
    return max(math.floor(mass / 3) - 2, 0)


def calc_fuel_for_fuel(mass):
    sum_fuel = 0
    while mass > 0:
        sum_fuel += mass
        mass = calc_fuel(mass)
    return sum_fuel


if __name__ == "__main__":
    input_data = get_input_data("input1.txt")
    data = [int(i[0]) for i in input_data]
    fuel = list(map(calc_fuel, data))

    answer1 = sum(fuel)
    answer2 = sum(map(calc_fuel_for_fuel, fuel))

    print(answer1)
    print(answer2)
