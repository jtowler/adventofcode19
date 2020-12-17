import itertools


def pad_cube(data, n=6, hc=False):
    def expand(dt):
        l_y = [[dt[0]] * len(dt)] * int((len(dt) - 1) / 2)
        return l_y + [dt] + l_y

    data = ['.' * n + d + '.' * n for d in data]
    l_x = ['.' * len(data[0])] * n
    data = expand(l_x + data + l_x)
    return expand(data) if hc else data


def count_cubes(data, hc=False):
    if hc:
        return sum(line.count('#') for cb in data for slce in cb for line in slce)
    return sum(line.count('#') for slce in data for line in slce)


def cycle_cube(data):
    return [[''.join([new_character(get_neighbours(data, z, y, x), cube)
                      for x, cube in enumerate(line)])
             for y, line in enumerate(slce)]
            for z, slce in enumerate(data)]


def cycle_hyper_cube(data):
    return [[[''.join([new_character(get_neighbours_hc(data, w, z, y, x), cube)
                       for x, cube in enumerate(line)])
              for y, line in enumerate(slce)]
             for z, slce in enumerate(in_cube)]
            for w, in_cube in enumerate(data)]


def new_character(n, cube):
    if ((cube == '#') and (4 > n > 1)) or ((cube == '.') and (n == 3)):
        return '#'
    return '.'


def get_neighbours(data, z, y, x):
    nbrs = 0
    for ix, iy, iz in itertools.product([0, -1, 1], [0, -1, 1], [0, -1, 1]):
        if not (ix, iy, iz).count(0) == 3:
            nx, ny, nz = x + ix, y + iy, z + iz
            if (len(data) > nx >= 0) and (len(data) > ny >= 0) and (len(data) > nz >= 0):
                if data[nz][ny][nx] == '#':
                    nbrs += 1
    return nbrs


def get_neighbours_hc(data, w, z, y, x):
    nbrs = 0
    for ix, iy, iz, iw in itertools.product([0, -1, 1], [0, -1, 1], [0, -1, 1], [0, -1, 1]):
        if not (ix, iy, iz, iw).count(0) == 4:
            nx, ny, nz, nw = x + ix, y + iy, z + iz, w + iw
            if (len(data) > nx >= 0) and (len(data) > ny >= 0) and \
                    (len(data) > nz >= 0) and (len(data) > nw >= 0):
                if data[nw][nz][ny][nx] == '#':
                    nbrs += 1
    return nbrs


def part(data, n, hc):
    cycle = cycle_hyper_cube if hc else cycle_cube
    padded_data = pad_cube(data, hc=hc)
    for _ in range(n):
        padded_data = cycle(padded_data)
    return count_cubes(padded_data, hc)


if __name__ == '__main__':
    input_data = open("../../resources/advent20/input17.txt", "r").read().split("\n")
    answer1 = part(input_data, 6, False)
    print(answer1)  # 112
    answer2 = part(input_data, 6, True)
    print(answer2)  # 848
