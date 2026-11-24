import numpy as np

def rref(A, tol = 1e-10) :
    R = np.array(A, dtype = float)

    n, m = R.shape
    r = 0
    pivotcol = []
    for c in range(0, m) :
        if r >= n : # all rows have pivot
            break

        mx = R[r][c]
        mxrow = r
        for row in range(r, n) :
            if mx < abs(R[row][c]) :
                mx = abs(R[row][c])
                mxrow = row
        if mx > tol : # has a pivot
            R[[r, mxrow]] = R[[mxrow, r]]
            pivotval = R[r][c]
            R[r] /= pivotval
            for row in range(0, n) :
                if row == r :
                    continue
                R[row] -= R[row][c] * R[r]
            pivotcol.append(c)
            r += 1 # move to next

    return R, pivotcol

def rank(A, tol = 1e-10) :
    R, pivotcol = rref(A)

    return len(pivotcol)

def null_space_basis(A, tol = 1e-10) :
    R, pivotcol = rref(A)
    r = rank(A)
    basis = []

    n, m = R.shape

    freecol = []
    for col in range(0, m) :
        if not (col in pivotcol) :
            freecol.append(col)

    for f in freecol :
        x = np.zeros(m)
        x[f] = 1
        for i, p in enumerate(pivotcol) :
            x[p] = -R[i][f]
        basis.append(x)
    
    return basis

def col_space_basis(A, tol = 1e-10) :
    R, pivotcol = rref(A)
    basis = []
    for col in pivotcol :
        basis.append(R[:, col])
    return basis
        

rng = np.random.default_rng(67)

if 0:
    for guess in range(20) : 
        A = rng.uniform(-10, 10, size = (5, 7))
        # print(R)

        nullbasis = null_space_basis(A)

        for el in nullbasis :
            print(A @ el)

if 0:
    A = rng.uniform(-10, 10, size = (6, 4))
    B = rng.uniform(-10, 10, size = (4, 8))
    C = A @ B
    print(rank(C))
    print(null_space_basis(C))
    print(C)
