from src.utils import get_input_data
import re

slope = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#"""


def count_trees(slp, right=3, down=1) -> int:
    x_max = len(slp[0])
    x = 0
    trees = []
    for a, i in enumerate(slp[::down]):
        trees.append(i[x])
        x = (x + right) % x_max
    return trees.count('#')


if __name__ == '__main__':
    slope_data = [i[0] for i in get_input_data("advent20/input3.txt")]
    r1d1 = count_trees(slope_data, 1)
    r3d1 = count_trees(slope_data)
    r5d1 = count_trees(slope_data, 5)
    r7d1 = count_trees(slope_data, 7)
    r1d2 = count_trees(slope_data, 1, 2)
    print(r3d1)
    print(r1d1 * r3d1 * r5d1 * r7d1 * r1d2)
