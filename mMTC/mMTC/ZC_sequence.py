import math
import numpy as np


def prime_factor(n):
    return next(n // i for i in range(1, n) if n % i == 0 and is_prime(n // i))


def is_prime(m):
    return all(m % i for i in range(2, m - 1))


def zc_sequence(length: int, root: int, shift: int = 0) -> np.ndarray[complex]:
    """
    Returns Zadoff-Chu sequence
    :param root: root index
    :param length: length of sequence {0, ..., length - 1}
    :param shift: cyclic shift
    :return: np.array(complex): Array of complex numbers
    """

    if not isinstance(length, int):
        raise TypeError(f"Argument 'length' must be of type 'int', not {type(length)}.")
    if not length > 1:
        raise ValueError(f"Argument 'length' must be greater than 1, not {length}.")

    if not isinstance(root, int):
        raise TypeError(f"Argument 'root' must be of type 'int', not {type(root)}.")
    if not 0 < root < length:
        raise ValueError(f"Argument 'root' must be greater than 0 and less than 'length', not {root}.")

    if not isinstance(shift, int):
        raise TypeError(f"Argument 'shift' must be of type 'int', not {type(shift)}.")
    
    n_values = np.arange(length)
    z_values = np.exp(-1j * np.pi * root * n_values * (n_values + 1) / length)
    
    if not math.gcd(length, root) == 1:
        n_sf = prime_factor(length)
        return z_values[np.arange(n_sf) % length]
    else:
        return z_values
