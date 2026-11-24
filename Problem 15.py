import numpy as np

def rank_one(u, v, w) :
    return np.einsum("i,j,k->ijk", u, v, w)

if 0:
    T = np.arange(24).reshape(2, 3, 4)

    print(T)

    for i in range(2) :
        for j in range(3) :
            for k in range(4) :
                print(T[i, j, k])
                print(T.reshape(-1)[12 * i + 4 * j + k])

    print(T.reshape(2, 12))
    print(T.transpose(1, 0, 2).reshape(3, 8))

if 0:
    rng = np.random.default_rng(67)
    A = rng.integers(0, 10, size=(2, 2))
    B = rng.integers(0, 10, size=(2, 2))
    x = rng.integers(0, 10, size=2)
    y = rng.integers(0, 10, size=2)

    #matrix product
    print(np.einsum("ij,jk->ik", A, B))
    print(A@B)
    #trace
    print(np.einsum("ii->", A))
    print(np.trace(A))
    #dot product
    print(np.einsum("i,i->", x, y))
    print(x@y)
    #outer product
    print(np.einsum("i,j->ij", x, y))
    print(np.outer(x, y))
    #transpose
    print(np.einsum("ij->ji", A))
    print(A.T)
    #bilinear form
    print(np.einsum("i,ij,j->", x, A, y))
    print(x@A@y)
    #batch matrix product
    A_batch = rng.integers(0, 10, size=(2, 2, 2))
    B_batch = rng.integers(0, 10, size=(2, 2, 2))
    print(np.einsum("bij,bjk->bik", A_batch, B_batch))
    print(A_batch@B_batch)

if 0:
    rng = np.random.default_rng(67)
    A_batch = rng.integers(0, 10, size=(100, 4, 4))
    B_batch = rng.integers(0, 10, size=(100, 4, 4))
    traces = np.einsum("bii->b", A_batch)
    products = np.einsum("bij, bjk->bik", A_batch, B_batch)

    loop_traces = []
    loop_products = []
    for A, B in zip(A_batch, B_batch) :
        loop_traces.append(np.trace(A))
        loop_products.append(A@B)

    for i in range(len(traces)) :
        if traces[i] != loop_traces[i] :
            print("Bad")

    for i in range(len(products)) :
        if not np.array_equal(products[i], loop_products[i]) :
            print("Bad")
    # all good

if 0:
    rng = np.random.default_rng(67)
    A = rng.integers(0, 10, size = (3, 4))
    B = rng.integers(0, 10, size = (2, 5))
    X = rng.integers(0, 10, size = (4, 5))

    if np.array_equal((A @ X @ B.T).reshape(-1), np.kron(A, B) @ X.reshape(-1)) :
        print("Equal")
    #good

if 0:
    rng = np.random.default_rng(67)
    u = rng.integers(0, 10, size = 3)
    v = rng.integers(0, 10, size = 3)
    w = rng.integers(0, 10, size = 3)
    T = rank_one(u, v, w)

    for k in range(3) :
        print(T[:, :, k])
        uvT = u[:, None] @ v[None, :]
        print(uvT)
    #indeed multiples