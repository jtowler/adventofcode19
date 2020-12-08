from functools import reduce
from math import gcd
from typing import List, Dict

from src.utils import _RESOURCE_LOC
import re


def lcm(a, b):
    return int(a * b / gcd(a, b))


def lcms(*numbers):
    return reduce(lcm, numbers)


def planet_from_str(s: str) -> 'Planet':
    xs, ys, zs = re.match("<x=(-?\d+), y=(-?\d+), z=(-?\d+)>", s).groups()
    return Planet(int(xs), int(ys), int(zs))


class Planet(object):

    def __init__(self, x: int, y: int, z: int, v_x: int = 0, v_y: int = 0, v_z: int = 0):
        self.x = x
        self.y = y
        self.z = z
        self.v_x = v_x
        self.v_y = v_y
        self.v_z = v_z

    def __repr__(self) -> str:
        return f"pos=<x= {self.x}, y= {self.y}, z= {self.z}>, vel=<x= {self.v_x}, y= {self.v_y}, z= {self.v_z}>"

    def __eq__(self, other: 'Planet') -> bool:
        return ((self.x == other.x) & (self.y == other.y) & (self.z == other.z) &
                (self.v_x == other.v_x) & (self.v_y == other.v_y) & (self.v_z == other.v_z))

    def copy(self) -> 'Planet':
        return Planet(self.x, self.y, self.z, self.v_x, self.v_y, self.v_z)

    @staticmethod
    def _get_velocity(this: int, that: int) -> int:
        if this == that:
            return 0
        elif this > that:
            return -1
        else:
            return 1

    def update(self, others: List['Planet']) -> None:
        others = [planet for planet in others if planet != self]
        self.v_x += sum([self._get_velocity(self.x, planet.x) for planet in others])
        self.v_y += sum([self._get_velocity(self.y, planet.y) for planet in others])
        self.v_z += sum([self._get_velocity(self.z, planet.z) for planet in others])

        self.x += self.v_x
        self.y += self.v_y
        self.z += self.v_z

    def get_energy(self):
        pot = abs(self.x) + abs(self.y) + abs(self.z)
        kin = abs(self.v_x) + abs(self.v_y) + abs(self.v_z)
        return pot * kin


def run_sim(moons: List['Planet'], steps: int):

    count = 0
    xs = []
    ys = []
    zs = []
    while count < steps:
        n_moons = [moon.copy() for moon in moons]
        xs.append(n_moons[2].x)
        ys.append(n_moons[2].y)
        zs.append(n_moons[2].z)
        for i in moons:
            i.update(n_moons)
        count += 1

    return moons, lcms(find_cycle(xs), find_cycle(ys), find_cycle(zs))


def find_cycle(l):
    inds = [i for i in range(len(l)) if l[i] == l[0]][1:]
    for ind in inds:
        if l[:ind] == l[ind: ind * 2]:
            return ind
    else:
        raise ValueError


if __name__ == "__main__":
    with open(f"{_RESOURCE_LOC}advent19/input12.txt") as f:
        planets = [planet_from_str(i) for i in f.readlines()]

    new_planets, answer2 = run_sim(planets, 1000000)
    answer1 = sum([m.get_energy() for m in new_planets])
    print(answer1)
    print(answer2)
