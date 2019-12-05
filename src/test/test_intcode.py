from unittest import TestCase

from src.day5 import Intcode


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
