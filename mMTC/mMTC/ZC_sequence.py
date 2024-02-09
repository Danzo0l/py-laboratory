import numpy as np


def zc_sequence(r: int, n_zc: int) -> np.ndarray[complex]:
    """
    `Expression (1)`
    :param r: root index
    :param n_zc: max index {0, ..., N_ZC - 1}
    :return: np.array(complex): Array of complex numbers
    """

    n_values = np.arange(0, n_zc)
    return np.exp(-1j * np.pi * r * n_values * (n_values + 1) / n_zc)


def zc_shift(p: int, zr: np.ndarray) -> np.ndarray[complex]:
    """
    Zadoff-Chu sequence cyclic shift
    `Expression (2)`
    :param zr:
    :param p: p is the preamble index randomly selected in the set{1,...,NPT}
    NPT = [n_zc /n_cs]
    :return: np.array(complex): Array of complex numbers
    """
    return np.roll(zr, p)


def auto_correlation(z_pr: np.ndarray, z_r: np.ndarray, tao: int) -> float:
    """
    Cyclic cross-correlation
    :param z_pr: Shifted Zadoff-Chu sequence
    :param z_r: Zadoff-Chu sequence
    :param tao: Shift of ZC sequence
    :return:
    """
    return sum(z_pr * np.conj(np.roll(z_r, tao)))
