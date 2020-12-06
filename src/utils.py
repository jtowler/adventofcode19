from csv import reader

_RESOURCE_LOC = "../../resources/"


def get_input_data(filename: str, **kwargs):
    with open(f"{_RESOURCE_LOC}{filename}") as f:
        csv_reader = reader(f, kwargs)
        data = [i for i in csv_reader]
    return data
