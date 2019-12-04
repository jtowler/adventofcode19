def is_adj(l):
    for i in range(len(l) - 1):
        if l[i] == l[i + 1]:
            return True
    return False


def is_adj2(l):
    for i in l:
        if l.count(i) == 2:
            return True
    return False


def is_password(x, condition=is_adj):
    ints = [int(i) for i in str(x)]
    return sorted(ints) == ints and condition(ints)


def count_passwords(r, condition=is_adj):
    return sum([is_password(pwd, condition) for pwd in r])


if __name__ == "__main__":
    input_data = range(231832, 767347)
    answer1 = count_passwords(input_data)
    answer2 = count_passwords(input_data, is_adj2)
    print(answer1)
    print(answer2)
