bearings = 'ESWN'


class Ship:
    east = 0
    north = 0
    bearing = 'E'

    def read_instruction(self, instruction: str) -> None:
        d, n = instruction[0], int(instruction[1:])
        if d in 'LR':
            self.change_bearing(d, n)
        else:
            self.move(d, n)

    def move(self, direction: str, amount: int):
        if direction == 'F':
            direction = self.bearing
        if direction == 'E':
            self.east += amount
        if direction == 'W':
            self.east -= amount
        if direction == 'N':
            self.north += amount
        if direction == 'S':
            self.north -= amount

    def change_bearing(self, direction: str, amount: int) -> None:
        bearing_index = bearings.index(self.bearing)
        bearing_inc = int(amount / 90)
        if direction == 'L':
            bearing_inc *= -1
        new_bearing_index = (bearing_index + bearing_inc) % 4
        self.bearing = bearings[new_bearing_index]


class WaypointShip:
    wp_east = 10
    wp_north = 1
    east = 0
    north = 0

    def read_instruction(self, instruction: str) -> None:
        d, n = instruction[0], int(instruction[1:])
        if d in 'LR':
            self.rotate_waypoint(d, n)
        if d == 'F':
            self.move(n)
        else:
            self.move_waypoint(d, n)

    def rotate_waypoint(self, direction: str, amount: int) -> None:
        bearing_inc = int(amount / 90)
        if direction == 'L':
            bearing_inc *= -1
        bearing_index = bearing_inc % 4
        if bearing_index == 0:
            self.wp_east, self.wp_north = self.wp_east, self.wp_north
        if bearing_index == 1:
            self.wp_east, self.wp_north = self.wp_north, -self.wp_east
        if bearing_index == 2:
            self.wp_east, self.wp_north = -self.wp_east, -self.wp_north
        if bearing_index == 3:
            self.wp_east, self.wp_north = -self.wp_north, self.wp_east

    def move(self, amount: int) -> None:
        self.east += amount * self.wp_east
        self.north += amount * self.wp_north

    def move_waypoint(self, direction: str, amount: int):
        if direction == 'E':
            self.wp_east += amount
        if direction == 'W':
            self.wp_east -= amount
        if direction == 'N':
            self.wp_north += amount
        if direction == 'S':
            self.wp_north -= amount


def manhattan(ship):
    return abs(ship.east) + abs(ship.north)


if __name__ == '__main__':
    instructions = open("../../resources/advent20/input12.txt", "r").read().split("\n")
    ship1 = Ship()
    ship2 = WaypointShip()
    for ins in instructions:
        ship1.read_instruction(ins)
        ship2.read_instruction(ins)
    print(manhattan(ship1))  # 962
    print(manhattan(ship2))  # 56135
