from src.utils import get_input_data


def get_val(s: str, n):
    l = list(range(n))
    for c in s:
        half_len = int(len(l) / 2)
        if c in ['F', 'L']:
            l = l[:half_len]
        else:
            l = l[half_len:]
    return l[0]


def get_seat(s):
    r = get_val(s[:7], 128)
    c = get_val(s[7:], 8)
    return (r * 8) + c


def get_seat_full(s):
    r = get_val(s[:7], 128)
    c = get_val(s[7:], 8)
    return r, c


if __name__ == '__main__':
    input_data = [i[0] for i in get_input_data('advent20/input5.txt')]
    print(max([get_seat(i) for i in input_data]))
    seats = [get_seat_full(i) for i in input_data]
    for r in range(9, 108):
        for c in range(8):
            if (r, c) not in seats:
                print((r * 8) + c)
