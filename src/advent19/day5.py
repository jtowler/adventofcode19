from typing import List, Union

from src.utils import get_input_data


class Intcode:

    def __init__(self, program: List[int], input_val: Union[int, List[int]] = None) -> None:
        self.pointer = 0
        self.program = program
        if type(input_val) == int:
            self.input_val = [input_val]
        else:
            self.input_val = input_val
        self.input_val_pointer = 0
        self.output = []

    def _get_value(self, i: int, immediate: int = 0) -> int:
        p = self.program[i]
        if immediate:
            return p
        return self.program[p]

    def _add_to_output(self, i: int, immediate: int = None) -> None:
        self.output.append(self._get_value(i, immediate))

    def _set_value(self, i: int, value: int) -> None:
        self.program[i] = value

    def _increment_pointer(self, i: int) -> None:
        self.pointer += i

    def terminated(self) -> bool:
        return self._get_value(self.pointer, 1) == 99

    def run_program(self) -> None:
        while not self.terminated():
            self._run_step()

    def _run_until_instruction(self, n) -> None:
        t, p1, p2 = self._parse_type()
        while (t != 99) & (t != n):
            self._run_step()
            t, p1, p2 = self._parse_type()

    def run_until_input(self) -> None:
        self._run_until_instruction(3)

    def run_until_output(self) -> None:
        self._run_until_instruction(4)

    def _parse_type(self):
        t = self._get_value(self.pointer, 1)
        if t < 100:
            return t, 0, 0
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
            self._set_value(self._get_value(self.pointer + 1, 1), self.input_val[self.input_val_pointer])
            self.input_val_pointer += 1
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
    input_data = get_input_data("advent19/input5.txt")
    data = [int(i) for i in input_data[0]]

    ic = Intcode(data.copy(), input_val=1)
    ic.run_program()
    answer1 = ic.output[-1]
    print(answer1)

    ic = Intcode(data.copy(), input_val=5)
    ic.run_program()
    answer2 = ic.output[0]
    print(answer2)
