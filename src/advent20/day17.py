import itertools


def pad_cube(data, n=6, hc=False):
    data = ['.' * n + d + '.' * n for d in data]
    l_x = ['.' * len(data[0])] * n
    data = l_x + data + l_x
    l_y = [[data[0]] * len(data)] * int((len(data) - 1) / 2)
    data = l_y + [data] + l_y
    if hc:
        l_z = [[data[0]] * len(data)] * int((len(data) - 1) / 2)
        return l_z + [data] + l_z
    return data


def count_cubes(data, hc=False):
    if hc:
        return sum(line.count('#') for cb in data for slce in cb for line in slce)
    return sum(line.count('#') for slce in data for line in slce)


def cycle_cube(data):
    new_data = []
    for z, slce in enumerate(data):
        new_slice = []
        for y, line in enumerate(slce):
            new_line = ''
            for x, cube in enumerate(line):
                n = get_neighbours(data, z, y, x)
                new_line += new_character(n, cube)
            new_slice.append(new_line)
        new_data.append(new_slice)
    return new_data


def cycle_hyper_cube(data):
    new_data = []
    for w, in_cube in enumerate(data):
        new_in_cube = []
        for z, slce in enumerate(in_cube):
            new_slice = []
            for y, line in enumerate(slce):
                new_line = ''
                for x, cube in enumerate(line):
                    n = get_neighbours_hc(data, w, z, y, x)
                    new_line += new_character(n, cube)
                new_slice.append(new_line)
            new_in_cube.append(new_slice)
        new_data.append(new_in_cube)
    return new_data


def new_character(n, cube):
    if ((cube == '#') and (4 > n > 1)) or ((cube == '.') and (n == 3)):
        return '#'
    return '.'


def get_neighbours(data, z, y, x):
    nbrs = 0
    for ix, iy, iz in itertools.product([0, -1, 1], [0, -1, 1], [0, -1, 1]):
        if not ((ix == 0) and (iy == 0) and (iz == 0)):
            nx, ny, nz = x + ix, y + iy, z + iz
            if (len(data) > nx >= 0) and (len(data) > ny >= 0) and (len(data) > nz >= 0):
                if data[nz][ny][nx] == '#':
                    nbrs += 1
    return nbrs


def get_neighbours_hc(data, w, z, y, x):
    nbrs = 0
    for ix, iy, iz, iw in itertools.product([0, -1, 1], [0, -1, 1], [0, -1, 1], [0, -1, 1]):
        if not ((ix == 0) and (iy == 0) and (iz == 0) and (iw == 0)):
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
    answer2 = part(input_data, 6, True)
    print(answer1)  # 112
    print(answer2)  # 848
