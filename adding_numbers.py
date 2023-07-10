from numba import njit

@njit #remember that njit is the short hand for @jit(nopython=True)
def adding_numbers(x, y):
    return int(x) + int(y)