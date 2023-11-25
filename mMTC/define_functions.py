<<<<<<< HEAD
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
=======
import cmath
import math


def Zr(n):
    """
    Function Zr(n): doc/Functions.md:3
    :param n: float:
    :return :
    """
    a = -(math.pi)
    return cmath.exp(math.pi)
>>>>>>> ab779599bf45fae6ca3ee4c40dcefb63b22315ca
