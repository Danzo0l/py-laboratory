import numpy as np


def Z_r(r: int, n_zc: int) -> np.ndarray[complex]:
    """

    `Expression (1)`
    :param r: root index
    :param n_zc: max index {0, ..., N_ZC - 1}
    :return: np.array(complex): Array of complex numbers
    """

    n_values = np.arange(0, n_zc)
    return np.exp(-1j * np.pi * r * n_values * (n_values + 1) / n_zc)


def Z_p_r(p: int, zr: np.ndarray) -> np.ndarray[complex]:
    """
    Zadoff-Chu sequence cyclic shift
    `Expression (2)`
    :param zr:
    :param p: p is the preamble index randomly selected in the set{1,...,NPT}
    NPT = [n_zc /n_cs]
    :return: np.array(complex): Array of complex numbers
    """
    return np.roll(zr, p)
