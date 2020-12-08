from src.utils import get_input_data


def generate_full_wire(l):
    ps = [(0, 0)]
    for i in l:
        x1, y1 = ps[-1]
        x2, y2 = get_next_pos(x1, y1, i)
        ps += generate_line(x1, x2, y1, y2)
    return ps


def get_next_pos(x, y, mv):
    d = mv[0]
    n = int(mv[1:])
    if d == 'L':
        x -= n
    if d == 'R':
        x += n
    if d == 'U':
        y -= n
    if d == 'D':
        y += n
    return x, y


def generate_line(x1, x2, y1, y2):
    if x1 == x2:
        return [(x1, i) for i in get_range(y1, y2)]
    else:
        return [(i, y1) for i in get_range(x1, x2)]


def get_range(a, b):
    if a > b:
        return [i for i in range(a - 1, b - 1, -1)]
    else:
        return [i for i in range(a + 1, b + 1)]


def determine_cross(l1, l2):
    f1 = generate_full_wire(l1)
    f2 = generate_full_wire(l2)

    s = set(f2) & set(f1)
    s.remove((0, 0))
    return min(map(lambda x: abs(x[0]) + abs(x[1]), s))


def determine_timing(l1, l2):
    f1 = generate_full_wire(l1)
    f2 = generate_full_wire(l2)

    s = set(f2) & set(f1)
    s.remove((0, 0))
    return min(f1.index(i) + f2.index(i) for i in s)


if __name__ == "__main__":
    input_data = get_input_data("advent19/input3.txt")
    w1 = [i for i in input_data[0]]
    w2 = [i for i in input_data[1]]

    answer1 = determine_cross(w1, w2)
    answer2 = determine_timing(w1, w2)

    print(answer1)
    print(answer2)
