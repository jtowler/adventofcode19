from unittest import TestCase

from src.advent19.day5 import Intcode


class TestIntcode(TestCase):

    def test_run_program(self):
        ic = Intcode([1, 0, 0, 0, 99])
        ic.run_program()
        assert ic.program == [2, 0, 0, 0, 99]

        ic = Intcode([2, 3, 0, 3, 99])
        ic.run_program()
        assert ic.program == [2, 3, 0, 6, 99]

        ic = Intcode([2, 4, 4, 5, 99, 0])
        ic.run_program()
        assert ic.program == [2, 4, 4, 5, 99, 9801]

        ic = Intcode([1, 1, 1, 4, 99, 5, 6, 0, 99])
        ic.run_program()
        assert ic.program == [30, 1, 1, 4, 2, 5, 6, 0, 99]

    def test_advanced_run_program(self):
        ic = Intcode([1101, 100, -1, 4, 0])
        ic.run_program()
        assert ic.program == [1101, 100, -1, 4, 99]

        ic = Intcode([1002, 4, 3, 4, 33])
        ic.run_program()
        assert ic.program == [1002, 4, 3, 4, 99]

    def test_run_program_output(self):
        ic = Intcode([3, 0, 4, 0, 99], 100)
        ic.run_program()
        assert ic.output == [100]

    def test_equality_program(self):
        ic = Intcode([3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8], 8)
        ic.run_program()
        assert ic.output == [1]

        ic = Intcode([3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8], 7)
        ic.run_program()
        assert ic.output == [0]

    def test_less_than_program(self):
        ic = Intcode([3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8], 8)
        ic.run_program()
        assert ic.output == [0]

        ic = Intcode([3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8], 7)
        ic.run_program()
        assert ic.output == [1]

    def test_equality_program_immediate(self):
        ic = Intcode([3, 3, 1108, -1, 8, 3, 4, 3, 99], 8)
        ic.run_program()
        assert ic.output == [1]

        ic = Intcode([3, 3, 1108, -1, 8, 3, 4, 3, 99], 7)
        ic.run_program()
        assert ic.output == [0]

    def test_less_than_program_immediate(self):
        ic = Intcode([3, 3, 1107, -1, 8, 3, 4, 3, 99], 8)
        ic.run_program()
        assert ic.output == [0]

        ic = Intcode([3, 3, 1107, -1, 8, 3, 4, 3, 99], 7)
        ic.run_program()
        assert ic.output == [1]

    def test_zero_program(self):
        ic = Intcode([3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9], 0)
        ic.run_program()
        assert ic.output == [0]

        ic = Intcode([3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9], 8)
        ic.run_program()
        assert ic.output == [1]

    def test_zero_program_immediate(self):
        ic = Intcode([3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1], 0)
        ic.run_program()
        assert ic.output == [0]

        ic = Intcode([3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1], 8)
        ic.run_program()
        assert ic.output == [1]

    def test_large_program(self):
        program = [3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31,
                   1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104,
                   999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99]

        ic = Intcode(program, 0)
        ic.run_program()
        assert ic.output == [999]

        ic = Intcode(program, 8)
        ic.run_program()
        assert ic.output == [1000]

        ic = Intcode(program, 9)
        ic.run_program()
        assert ic.output == [1001]
