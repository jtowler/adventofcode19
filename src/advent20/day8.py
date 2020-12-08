from copy import deepcopy
from typing import List


def get_insts(lns: List[str]):
    def get_inst(ln):
        ins, n = ln.rstrip('\n').split(' ')
        return ins, int(n)
    return [get_inst(ln) for ln in lns]


def process_inst(inst, acc):
    inst, n = inst
    if inst == 'nop':
        return 1, acc
    elif inst == 'acc':
        return 1, acc + n
    elif inst == 'jmp':
        return n, acc


def get_prog_val(data):
    insts = get_insts(data)
    total = 0
    index = 0
    visited = [index]
    while (index < len(insts)) and (len(visited) == len(set(visited))):
        inst = insts[index]
        index_inc, total = process_inst(inst, total)
        index += index_inc
        visited.append(index)
    return total, index >= len(insts)


def part2(data):
    for i in range(len(data)):
        adj_data = change_inst(deepcopy(data), i)
        if adj_data is not None:
            total, terminated = get_prog_val(adj_data)
            if terminated:
                return total


def change_inst(data, i):
    if data[i].startswith('jmp'):
        data[i] = data[i].replace('jmp', 'nop')
        return data
    elif data[i].startswith('nop'):
        data[i] = data[i].replace('nop', 'jmp')
        return data
    else:
        return None


if __name__ == '__main__':
    input_data = open("../../resources/advent20/input8.txt")
    input_data = input_data.readlines()
    print(get_prog_val(input_data))
    print(part2(input_data))
