from collections import OrderedDict
from typing import List, Dict

from src.utils import get_input_data
import math


class Asteroid(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def angle(self, other):
        return math.atan2(other.y - self.y, other.x - self.x)

    def count_visible(self, others):
        angles = [self.angle(other) for other in others if other != self]
        unique_angles = set(angles)
        return len(unique_angles)

    def __eq__(self, other):
        return (self.x == other.x) & (self.y == other.y)

    def __repr__(self):
        return f"({self.x}, {self.y})"


def get_asteroids_in_angle(d: Dict[float, List[Asteroid]], a: float) -> List[Asteroid]:
    al = sorted(d)
    ls = [i for i in al if i > a]
    if len(ls) > 0:
        return d[ls[0]]
    else:
        return d[al[0]]


def vaporise(field: List[Asteroid], asteroid: Asteroid, n: int = 200):
    angles = {}
    for f in field:
        angle = asteroid.angle(f)
        if angle not in angles:
            angles[angle] = [f]
        else:
            angles[angle] = angles[angle] + [f]

    for k, v in angles.items():
        angles[k] = sorted(v, key=lambda a: math.sqrt(((a.x - asteroid.x) ** 2) + (a.y - asteroid.y) ** 2))

    vaporised = 0
    laser_angle = math.atan2(-1, 0) - 0.0000000001
    while vaporised < n:
        asteroids_in_angle = get_asteroids_in_angle(angles, laser_angle)
        vaporised += 1
        nearest_asteroid = asteroids_in_angle.pop(0)
        laser_angle = asteroid.angle(nearest_asteroid)
        if len(asteroids_in_angle) == 0:
            angles.pop(laser_angle)
    return 100 * nearest_asteroid.x + nearest_asteroid.y


if __name__ == "__main__":
    input_data = [list(i[0]) for i in get_input_data("advent19/input10.txt")]
    asteroids = [Asteroid(x, y) for y in range(len(input_data)) for x in range(len(input_data[0]))
                 if input_data[y][x] == '#']
    asteroids[1].count_visible(asteroids)
    visible = [asteroid.count_visible(asteroids) for asteroid in asteroids]
    answer1 = max(visible)
    asteroid = asteroids[visible.index(answer1)]
    print(answer1)
    answer2 = vaporise(asteroids, asteroid, 200)
    print(answer2)
