from typing import List

from src.utils import get_input_data


class SIF:

    def __init__(self, data: List[int], width: int, height: int) -> None:
        self.layer_size = width * height
        n_layers = len(data) / self.layer_size
        assert n_layers % 1 == 0, "Corrupted data"
        self.n_layers = int(n_layers)
        self.data = data
        self.length = len(data)
        self.width = width
        self.height = height
        self.layers = self._build_layers()
        self.image = self._get_image()

    def display(self) -> None:
        for line in self.image:
            print(''.join(['#' if i else ' ' for i in line]))

    def _build_layers(self):
        layers = []
        for l in range(0, self.length, self.layer_size):
            layer = [self.data[l + i: l + i + self.width] for i in range(0, self.layer_size, self.width)]
            layers.append(layer)
        return layers

    def count_n_in_layers(self, n: int):
        return [self.count_n_in_layer(l, n) for l in self.layers]

    @staticmethod
    def count_n_in_layer(layer: List[List[int]], n: int):
        return sum(map(lambda x: x.count(n), layer))

    def _get_image(self) -> List[List[int]]:
        image = []
        for w in range(self.width):
            line = []
            for h in range(self.height):
                pixel = [l[h][w] for l in self.layers]
                pixel = list(filter(lambda x: x < 2, pixel))
                line.append(pixel[0] if pixel else 2)
            image.append(line)
        return image


if __name__ == "__main__":
    input_data = [int(i) for i in get_input_data("advent19/input8.txt")[0][0]]

    assert SIF([1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2], 3, 2).layers[1] == [[7, 8, 9], [0, 1, 2]]
    assert SIF([0, 2, 2, 2, 1, 1, 2, 2, 2, 2, 1, 2, 0, 0, 0, 0], 2, 2).image == [[0, 1], [1, 0]]

    sif = SIF(input_data, 25, 6)
    z_count_layers = sif.count_n_in_layers(0)
    min_z_index = z_count_layers.index(min(z_count_layers))
    min_z_layer = sif.layers[min_z_index]
    min_z_1 = sif.count_n_in_layer(min_z_layer, 1)
    min_z_2 = sif.count_n_in_layer(min_z_layer, 2)
    answer1 = min_z_1 * min_z_2
    print(answer1)
    sif.display()
