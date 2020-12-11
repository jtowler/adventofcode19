from typing import List
from functools import partial


def get_seat(old_layout: List[str], y: int, x: int, yi: int, xi: int) -> str:
    new_y = y + yi
    new_x = x + xi
    if (0 <= new_y < y_len) and (0 <= new_x < x_len):
        return old_layout[new_y][new_x]
    else:
        return '.'


def get_seat_in_dir(old_layout: List[str], y: int, x: int, y_dir: int, x_dir: int) -> str:
    new_y = y + y_dir
    new_x = x + x_dir
    while (0 <= new_y < y_len) & (0 <= new_x < x_len):
        seat = old_layout[new_y][new_x]
        if seat != '.':
            return seat
        new_y = new_y + y_dir
        new_x = new_x + x_dir
    return '.'


def should_change(old_layout: List[str], y: int, x: int, empty: bool, n: int, func) -> bool:
    occupied = 0
    for yi, xi in [[0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1], [1, 0], [-1, 0]]:
        seat = func(old_layout, y, x, yi, xi)
        if seat == '#':
            occupied += 1
            if empty and (occupied > 0):
                return False
            if (not empty) and (occupied >= n):
                return True
    return empty


should_change1 = partial(should_change, func=get_seat, n=4)
should_change2 = partial(should_change, func=get_seat_in_dir, n=5)


def get_new_layout(old_layout, func) -> List[str]:
    new_layout = []
    for y, row in enumerate(old_layout):
        new_row = ''
        for x, seat in enumerate(row):
            if seat == '.':
                new_row += seat
            else:
                changes = func(old_layout, y, x, seat == 'L')
                if seat == '#':
                    new_row += 'L' if changes else seat
                elif seat == 'L':
                    new_row += '#' if changes else seat

        new_layout.append(new_row)
    return new_layout


def part(old_layout: List[str], func) -> int:
    while True:
        new_layout = get_new_layout(old_layout, func)
        if new_layout == old_layout:
            return sum(map(lambda x: x.count('#'), old_layout))
        else:
            old_layout = new_layout


if __name__ == '__main__':
    layout = open("../../resources/advent20/input11.txt", "r").read().split("\n")
    y_len = len(layout)
    x_len = len(layout[0])
    answer1 = part(layout, should_change1)
    answer2 = part(layout, should_change2)
    print(answer1)  # 2303
    print(answer2)  # 2057
