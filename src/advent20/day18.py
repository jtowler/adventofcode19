def reduce_non_brackets(data: str):
    line = data.split(' ')
    while len(line) >= 3:
        n1, op, n2 = line[:3]
        n1, n2 = int(n1), int(n2)
        if op == '*':
            n = n1 * n2
        elif op == '+':
            n = n1 + n2
        line = [str(n)] + line[3:]
    return line[0]


def reduce_non_brackets_pres(data: str):
    def update_line(ln, symbol, op):
        i = ln.index(symbol)
        return ln[:i - 1] + [str(op(int(ln[i - 1]), int(ln[i + 1])))] + ln[i + 2:]

    line = data.split(' ')
    while len(line) >= 3:
        if '+' in line:
            line = update_line(line, '+', lambda x, y: x + y)
        elif '*' in line:
            line = update_line(line, '*', lambda x, y: x * y)
    return line[0]


def eliminate_brackets(data: str, func):
    opening_ind = data.index('(')
    extra_opens = 0
    for i, a in enumerate(data[opening_ind + 1:]):
        if a == ')':
            if extra_opens == 0:
                closing_ind = i + opening_ind + 1
                break
            else:
                extra_opens -= 1
        elif a == '(':
            extra_opens += 1
    new_section = data[opening_ind + 1:closing_ind]
    if '(' in new_section:
        new_section = eliminate_brackets(new_section, func)
    data = data[:opening_ind] + func(new_section) + data[closing_ind + 1:]
    if '(' in data:
        data = eliminate_brackets(data, func)
    return func(data)


def part(data, func):
    return sum(int(eliminate_brackets(d, func)) if '(' in d else (int(func(d))) for d in data)


if __name__ == '__main__':
    input_data = open("../../resources/advent20/input18.txt", "r").read().split("\n")
    answer1 = part(input_data, reduce_non_brackets)
    answer2 = part(input_data, reduce_non_brackets_pres)
    print(answer1)  # 69490582260
    print(answer2)  # 362464596624526
