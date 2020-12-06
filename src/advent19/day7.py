import itertools
from typing import List

from src.advent19.day5 import Intcode
from src.utils import get_input_data


def amplifier_array(program: List[int], ps: List[int]):
    amps = [Intcode(program.copy(), p) for p in ps]
    for amp in amps:
        amp.run_until_input()
        amp._run_step()
    amp_index = 0
    amp_input = 0
    amps[0].input_val.append(amp_input)
    while not all([amp.terminated() for amp in amps]):
        amp = amps[amp_index]
        amp.run_until_input()
        amp.input_val.append(amp_input)
        amp.run_until_output()
        if not amp.terminated():
            amp._run_step()
            amp_input = amp.output[-1]
        if amp_index == len(amps) - 1:
            amp_index = 0
        else:
            amp_index += 1
    return amp_input


def phase_setting(program: List[int], phase_settings: List[int]) -> int:
    input_val = 0
    for setting in phase_settings:
        print(setting)
        ic = Intcode(program.copy(), [setting, input_val])
        ic.run_program()
        input_val = ic.output[0]
    return input_val


def get_max_setting(data: List[int]) -> int:
    return max(phase_setting(data, i) for i in itertools.permutations(range(5)))


if __name__ == "__main__":
    input_data = get_input_data("input7.txt")
    data = [int(i) for i in input_data[0]]
    # answer1 = get_max_setting(data)
    # print(answer1)
    # answer2 = amplifier_array([3, 26, 1001, 26, -4, 26, 3, 27, 1002, 27, 2, 27, 1, 27, 26,
    #                            27, 4, 27, 1001, 28, -1, 28, 1005, 28, 6, 99, 0, 0, 5], [9, 8, 7, 6, 5])

    answer3 = amplifier_array([3, 52, 1001, 52, -5, 52, 3, 53, 1, 52, 56, 54, 1007, 54, 5, 55, 1005, 55, 26, 1001, 54,
                               -5, 54, 1105, 1, 12, 1, 53, 54, 53, 1008, 54, 0, 55, 1001, 55, 1, 55, 2, 53, 55, 53, 4,
                               53, 1001, 56, -1, 56, 1005, 56, 6, 99, 0, 0, 0, 0, 10], [9, 7, 8, 5, 6])
    print(answer3)

18216
139629729
