import math
import numpy as np
from typing import TypeVar

T = TypeVar('T')


def Zr(r: int, n: int, n_zc: int) -> np.ndarray[complex]:
    """
    Function Zr(n): doc/Functions.md:3
    :param r: int: Radius
    :param n: np.array: Array of n values
    :param n_zc: Number n_zc
    :return: np.array(complex): Array of complex numbers
    """

    return np.exp(0 - 1j * ((math.pi * r * n * (n + 1)) / n_zc))


def Zpr(p: int, r: int, n: np.ndarray) -> np.ndarray[complex]:
    """
    Function Zr(n): doc/Functions.md:3
    :param r: int: Radius
    :param n: np.array: Array of n values
    :param n_zc: Number n_zc
    :return: np.array(complex): Array of complex numbers
    """

    return np.exp(0 - 1j * ((math.pi * r * n * (n + 1)) / n_zc))
