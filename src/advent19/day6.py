from typing import List

from src.utils import get_input_data


class Orbiter(object):

    def __init__(self, s: str) -> None:
        self.n, self.orbited = s.split(')')

    def count_orbiting(self, l: List['Orbiter']) -> int:

        orbits = [o for o in l if o.orbited == self.n]
        if not orbits:
            return 1
        else:
            return 1 + orbits[0].count_orbiting(l)

    def get_all_orbits_from(self, l: List['Orbiter']) -> List['Orbiter']:
        orbits = [o for o in l if o.orbited == self.n]
        if not orbits:
            return [self]
        else:
            return [self] + orbits[0].get_all_orbits_from(l)


def get_shortest_between_orbits(l: List[Orbiter]) -> int:
    a_orbits = list(filter(lambda x: x.orbited == 'YOU', data))[0].get_all_orbits_from(l)
    b_orbits = list(filter(lambda x: x.orbited == 'SAN', data))[0].get_all_orbits_from(l)
    jumps = [i + j for i in range(len(a_orbits)) for j in range(len(b_orbits)) if a_orbits[i] == b_orbits[j]]
    return min(jumps) - 2


if __name__ == "__main__":
    input_data = get_input_data("advent19/input6.txt")
    data = [Orbiter(i[0]) for i in input_data]
    answer1 = sum([i.count_orbiting(data) for i in data])
    answer2 = get_shortest_between_orbits(data)
    print(answer1)
    print(answer2)
