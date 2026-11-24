import numpy as np
import matplotlib.pyplot as plt
import math


def dual_basis(A) :
    R = np.array(A, dtype = float)
    
    Rinv = np.linalg.inv(R)

    basis = []

    n, m = R.shape

    for row in range(n) :
        basis.append(Rinv[row])

    return basis

rng = np.random.default_rng(67)

if 0 :
    A = rng.uniform(-10, 10, size = (5, 5)) # most probably invertible
    R = np.array(A, dtype = float)
    dualbasis = dual_basis(A)
    n = len(dualbasis)

    RB = np.zeros((5, 5) ,dtype = float)
    for i in range(n) : 
        for j in range(n) :
            RB[i][j] = (dualbasis[i] @ R[:, j])

    print(RB)

    x = rng.uniform(-10, 10, size = (5))
    print(x)

    y = np.zeros(5, dtype = float)
    for i in range(n) :
        coord = dualbasis[i] @ x
        y += coord * R[:, i]
    print(y)

if 0 : 
    t = [-1, 0, 1]
    V = np.zeros((len(t), len(t)), dtype = float)
    for i in range(len(t)) :
        for j in range(len(t)) :
            V[i][j] = (t[i] ** j)

    Vinv = np.linalg.inv(V)
    lagrange = []
    for i in range(Vinv.shape[0]) :
        poly = []
        for j in range(Vinv.shape[0]) :
            poly.append(V[j, i])
        lagrange.append(poly)
    print(lagrange)

if 0: 
    t = np.linspace(-1, 1, 9)

    V = np.zeros((len(t), len(t)), dtype = float)
    for i in range(len(t)) :
        for j in range(len(t)) :
            V[i][j] = (t[i] ** j)

    Vinv = np.linalg.inv(V)
    lagrange = []
    for i in range(Vinv.shape[0]) :
        poly = []
        for j in range(Vinv.shape[0]) :
            poly.append(Vinv[j, i])
        lagrange.append(poly)

    x = np.linspace(-1, 1, 10000)
    p = np.zeros(len(x))
    for i, poly in enumerate(lagrange) :
        p += np.sin(3 * t[i]) * np.polynomial.polynomial.polyval(x, poly)

    plt.figure()
    plt.plot(x, np.sin(3 * x), label="f")
    plt.plot(x, p, label = "p")
    plt.legend()
    plt.show(block=True)

if 0: 
    t = np.linspace(-5, 5, 21)

    V = np.zeros((len(t), len(t)), dtype = float)
    for i in range(len(t)) :
        for j in range(len(t)) :
            V[i][j] = (t[i] ** j)

    Vinv = np.linalg.inv(V)
    lagrange = []
    for i in range(Vinv.shape[0]) :
        poly = []
        for j in range(Vinv.shape[0]) :
            poly.append(Vinv[j, i])
        lagrange.append(poly)

    x = np.linspace(-5, 5, 10000)
    p = np.zeros(len(x))
    for i, poly in enumerate(lagrange) :
        p += (1 / (1 + (t[i]) ** 2)) * np.polynomial.polynomial.polyval(x, poly)

    plt.figure()
    plt.plot(x, (1 / (1 + (x) ** 2)), label="f")
    plt.plot(x, p, label = "p")
    plt.legend()
    plt.show(block=True)