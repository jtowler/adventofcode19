from typing import List
import numpy


def get_earliest(time: int, bus: int) -> int:
    return filter(lambda x: x >= time, range(0, bus + time, bus)).__next__()


def part1(info: List[str]) -> int:
    departure = int(info[0])
    buses = [int(i) for i in info[1].split(',') if i != 'x']
    bus_times = {bus: get_earliest(departure, bus) for bus in buses}
    min_bus, min_departure = min(bus_times.items(), key=lambda x: x[1])
    wait_time = min_departure - departure
    return min_bus * wait_time


def get_t(t: int, step: int, offset: int, mod: int):
    while (t + offset) % mod != 0:
        t += step
    return t


def part2(info: List[str]) -> int:
    bus_times = [(int(a), i) for i, a in enumerate(info[1].split(',')) if a != 'x']
    t = 0
    m = bus_times[0][0]
    for bus, offset in bus_times[1:]:
        t = get_t(t, m, offset, bus)
        m = numpy.lcm(m, bus)
    return t


if __name__ == '__main__':
    input_data = open("../../resources/advent20/input13.txt", "r").read().split("\n")
    answer1 = part1(input_data)
    print(answer1)
    answer2 = part2(input_data)
    print(answer2)
