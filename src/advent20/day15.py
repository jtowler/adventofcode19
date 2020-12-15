from typing import List


def get_nth(turns: List[int], n: int) -> int:
    it = len(turns[:-1])
    last = turns[-1]
    d = {a: i for i, a in enumerate(turns[:-1])}
    while it < n - 1:
        if last not in d:
            d[last] = it
            last = 0
        else:
            tmp_last = it - d[last]
            d[last] = it
            last = tmp_last
        it += 1
    return last


if __name__ == '__main__':
    init_turns = [19, 20, 14, 0, 9, 1]

    answer1 = get_nth(init_turns, 2020)
    print(answer1)

    answer2 = get_nth(init_turns, 30000000)
    print(answer2)
