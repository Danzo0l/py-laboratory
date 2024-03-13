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


def zc_shift(zr: np.ndarray, p: int) -> np.ndarray[complex]:
    """
    Zadoff-Chu sequence cyclic shift
    `Expression (2)`
    :param zr:
    :param p: p is the preamble index randomly selected in the set{1,...,NPT}
    NPT = [n_zc /n_cs]
    :return: np.array(complex): Array of complex numbers
    """
    return np.roll(zr, p)


def discrete_fourier_transform(sequence: np.ndarray, length: int) -> np.ndarray[complex]:
    """
    Discrete Fourier Transform
    :param sequence: ZC-sequence
    :param length: sequence length
    :return: np.array(complex): Array of complex numbers
    """
    result = np.zeros(length, dtype=complex)

    for k in range(length):
        for n in range(length):
            result[k] += sequence[n] * np.exp(-2j * np.pi * k * n / length)

    return result


def cyclic_auto_correlation(zc: np.ndarray, zc_shifted: np.ndarray) -> float:
    """
    Correlation
    :param zc_shifted: Shifted Zadoff-Chu sequence
    :param zc: Zadoff-Chu sequence
    :return:
    """
    return sum(np.conj(zc) * zc_shifted)


def cyclic_correlation(zc: np.ndarray, zc_shifted: np.ndarray) -> float:
    """
    Correlation
    :param zc_shifted: Shifted Zadoff-Chu sequence
    :param zc: Zadoff-Chu sequence
    :return:
    """
    return sum(np.conj(zc) * zc_shifted)
