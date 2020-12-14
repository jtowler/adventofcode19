import itertools
import re


def get_instructions(data):
    instructs = []
    new_instruction = [data[0].split(' = ')[1]]
    for instruction in data[1:]:
        if instruction.startswith('mask'):
            instructs.append(new_instruction)
            new_instruction = [instruction.split(' = ')[1]]
        else:
            match = re.match(r"mem\[(\d+)] = (\d+)", instruction)
            new_instruction.append((int(match.group(1)), int(match.group(2))))
    return instructs + [new_instruction]


def apply_mask(mask, value):
    binary_val = "{0:b}".format(value).zfill(36)
    return int(''.join([m if m != 'X' else b for b, m in zip(binary_val, mask)]), 2)


def apply_mask2(mask, value):
    binary_val = "{0:b}".format(value).zfill(36)
    new_mask = [b if m == '0' else m for b, m in zip(binary_val, mask)]
    x_inds = [i for i, a in enumerate(new_mask) if a == 'X']
    combs = itertools.product(*[['0', '1'] for _ in range(len(x_inds))])
    adds = []
    for comb in combs:
        for i, c in enumerate(comb):
            new_mask[x_inds[i]] = c
        adds.append(int(''.join(new_mask), 2))
    return adds


def part2(instructs):
    addresses = {}
    for instruction in instructs:
        mask = instruction[0]
        for address, value in instruction[1:]:
            adds = apply_mask2(mask, address)
            for add in adds:
                addresses[add] = value
    return sum(addresses.values())


def part1(instructs):
    addresses = {}
    for instruction in instructs:
        mask = instruction[0]
        for address, value in instruction[1:]:
            value = apply_mask(mask, value)
            addresses[address] = value
    return sum(addresses.values())


if __name__ == '__main__':
    input_data = open("../../resources/advent20/input14.txt", "r").read().split("\n")
    instructions = get_instructions(input_data)
    answer1 = part1(instructions)
    print(answer1)
    answer2 = part2(instructions)
    print(answer2)
