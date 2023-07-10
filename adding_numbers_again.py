from numba import jit
@jit
def adding_numbers_again(x, y):
    return int(x) + int(y)