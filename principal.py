import numpy as np
from loguru import logger


def raiz(numero: float) -> float:
    return np.sqrt(numero)


def read_as_list(file: str) -> list:
    data = open(file, 'r')
    data = data.read().split(', ')
    return [int(i) for i in data]


def add_from_file(file: str) -> int:
    data = read_as_list(file)
    add = 0
    for i in data:
        add += int(i)
    return add
