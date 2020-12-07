from collections import Counter
from typing import List


def get_qs(data: List[str]):
    qs = []
    q = []
    ls = []
    l = 0
    for ln in data:
        if ln == '\n':
            qs.append(Counter(q))
            ls.append(l)
            q = []
            l = 0
        else:
            q += ln.rstrip('\n')
            l += 1
    qs.append(Counter(q))
    ls.append(l)
    return qs, ls


if __name__ == '__main__':
    input_data = open("../../resources/advent20/input6.txt")
    qs, ls = get_qs(input_data.readlines())
    print(sum(len(i) for i in qs))

    print(len([k for q, l in zip(qs, ls) for k, v in q.items() if v == l]))