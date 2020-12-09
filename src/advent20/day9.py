from itertools import combinations


def does_sum(n, prmbl):
    for i, j in combinations(prmbl, 2):
        if (i + j) == n:
            return True
    return False


def part1(data, prmbl_len):
    preamble = data[:prmbl_len]
    data = data[prmbl_len:]
    for d in data:
        if does_sum(d, preamble):
            preamble = preamble[1:] + [d]
        else:
            break
    return d


def part2(data, target):
    candidates = []
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            this_val = sum(data[i:j])
            if this_val == target:
                candidates.append(input_data[i:j])
                break
            elif this_val > target:
                break

    longest = max(candidates, key=len)
    return max(longest) + min(longest)


if __name__ == '__main__':
    input_data = open("../../resources/advent20/input9.txt")
    input_data = [int(i.strip('\n')) for i in input_data.readlines()]
    preamble_len = 25

    target_val = part1(input_data, preamble_len)
    print(target_val)
    print(part2(input_data, target_val))
