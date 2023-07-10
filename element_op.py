@jit(nopython=True, nogil=True)
def element_op(z, div_len, c, radius):
    for x in range(z.shape[0]):
        for y in range(z.shape[1]):
            if np.abs(z[x][y]) < radius:
                z[x][y] = np.square(z[x][y]) + c
                div_len[x][y] +=1
    return z, div_len
            

@jit(nopython=True,nogil=True)
def julia_fast(mesh, c=-1, num_iter=10, radius=2):

    z = mesh.copy()
    diverge_len = np.zeros(z.shape)

    for i in range(num_iter):
        z, diverge_len = element_op(z, diverge_len, c,radius)

    return diverge_len