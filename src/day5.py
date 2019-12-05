from typing import List

from src.utils import get_input_data


class Intcode(object):

    def __init__(self, program: List[int], input_val: int = None) -> None:
        self.pointer = 0
        self.program = program
        self.input_val = input_val
        self.output = []

    def _get_value(self, i: int, immediate: int = 0) -> int:
        p = self.program[i]
        if immediate:
            return p
        else:
            return self.program[p]

    def _add_to_output(self, i: int) -> None:
        self.output.append(self._get_value(i))

    def _set_value(self, i: int, value: int) -> None:
        self.program[i] = value

    def _increment_pointer(self, i: int) -> None:
        self.pointer += i

    def _get_type(self) -> int:
        return self._get_value(self.pointer, 1)

    def run_program(self) -> None:
        while self._get_type() != 99:
            self._run_step()

    def _run_step(self) -> None:
        t = self._get_type()
        if t == 1:
            self._set_value(self._get_value(self.pointer + 3, 1),
                            self._get_value(self.pointer + 1) + self._get_value(self.pointer + 2))
            self._increment_pointer(4)
        elif t == 2:
            self._set_value(self._get_value(self.pointer + 3, 1),
                            self._get_value(self.pointer + 1) * self._get_value(self.pointer + 2))
            self._increment_pointer(4)
        elif t == 3:
            self._set_value(self._get_value(self.pointer + 1, 1), self.input_val)
            self._increment_pointer(2)
        elif t == 4:
            self._add_to_output(self.pointer + 1)
            self._increment_pointer(2)
        elif t > 4:
            self._advanced_step()
        else:
            raise ValueError(f"Unknown instruction type {t}.")

    def _advanced_step(self):

        s = str(self._get_type())
        t = int(s[-2:])
        s = s[:-2][::-1]

        def get_mode_value(i):
            try:
                return self._get_value(self.pointer + i + 1, int(s[i]))
            except IndexError:
                return self._get_value(self.pointer + i + 1)

        i1 = get_mode_value(0)
        if t == 4:
            self.output.append(i1)
            self._increment_pointer(2)
            return
        i2 = get_mode_value(1)
        o = self._get_value(self.pointer + 3, 1)
        if t == 1:
            self._set_value(o, i1 + i2)
            self._increment_pointer(4)
        elif t == 2:
            self._set_value(o, i1 * i2)
            self._increment_pointer(4)
        elif t == 3:
            self._set_value(o, self.input_val)
            self._increment_pointer(2)

        else:
            raise ValueError(f"Unknown instruction type: {t}")


if __name__ == "__main__":
    input_data = get_input_data("input5.txt")
    data = [int(i) for i in input_data[0]]
    # answer1 = run_noun_verb(12, 2, data.copy())[0]
    # answer2 = check_noun_verb(data, 19690720)
    #
    # print(answer1)
    # print(answer2)
    # data = [1101,100,-1,4,0]
    # run_program(data, 1)
    ic = Intcode(data, input_val=1)
    ic.run_program()
    answer1 = ic.output[-1]
    print(answer1)
