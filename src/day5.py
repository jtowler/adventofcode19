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

    def _add_to_output(self, i: int, immediate: int = None) -> None:
        self.output.append(self._get_value(i, immediate))

    def _set_value(self, i: int, value: int) -> None:
        self.program[i] = value

    def _increment_pointer(self, i: int) -> None:
        self.pointer += i

    def _get_type(self) -> int:
        return self._get_value(self.pointer, 1)

    def run_program(self) -> None:
        while self._get_type() != 99:
            self._run_step()

    def _parse_type(self):
        t = self._get_value(self.pointer, 1)
        if t < 100:
            return t, 0, 0
        else:
            s = str(t)
            nt = int(s[-2:])
            s = s[:-2][::-1]
            p1 = int(s[0]) if len(s) > 0 else 0
            p2 = int(s[1]) if len(s) > 1 else 0
            return nt, p1, p2

    def _run_step(self) -> None:
        t, p1, p2 = self._parse_type()
        if t == 1:
            self._set_value(self._get_value(self.pointer + 3, 1),
                            self._get_value(self.pointer + 1, p1) + self._get_value(self.pointer + 2, p2))
            self._increment_pointer(4)
        elif t == 2:
            self._set_value(self._get_value(self.pointer + 3, 1),
                            self._get_value(self.pointer + 1, p1) * self._get_value(self.pointer + 2, p2))
            self._increment_pointer(4)
        elif t == 3:
            self._set_value(self._get_value(self.pointer + 1, 1), self.input_val)
            self._increment_pointer(2)
        elif t == 4:
            self._add_to_output(self.pointer + 1, p1)
            self._increment_pointer(2)
        elif t == 5:
            if self._get_value(self.pointer + 1, p1):
                self.pointer = self._get_value(self.pointer + 2, p2)
            else:
                self._increment_pointer(3)
        elif t == 6:
            if not self._get_value(self.pointer + 1, p1):
                self.pointer = self._get_value(self.pointer + 2, p2)
            else:
                self._increment_pointer(3)
        elif t == 7:
            v = self._get_value(self.pointer + 1, p1) < self._get_value(self.pointer + 2, p2)
            third = self._get_value(self.pointer + 3, 1)
            self._set_value(third, int(v))
            self._increment_pointer(4)
        elif t == 8:
            v = self._get_value(self.pointer + 1, p1) == self._get_value(self.pointer + 2, p2)
            third = self._get_value(self.pointer + 3, 1)
            self._set_value(third, int(v))
            self._increment_pointer(4)
        else:
            raise ValueError(f"Unknown instruction type {t}.")


if __name__ == "__main__":
    input_data = get_input_data("input5.txt")
    data = [int(i) for i in input_data[0]]

    ic = Intcode(data.copy(), input_val=1)
    ic.run_program()
    answer1 = ic.output[-1]
    print(answer1)

    ic = Intcode(data.copy(), input_val=5)
    ic.run_program()
    answer2 = ic.output[0]
    print(answer2)
