Programming exercises

For     
A = np.array([[1e-17, 1], [1, 1]], dtype = float)
b = np.array([1, 2], dtype = float).T

lu_solve gives [0, 1] while linalg.solve() gives [1, 1]

Since first lu uses pivot 1e-17 it has first row multiplier 1e17, so after elimination equation
x1 + x2 = 2 becomes (1 - 1e17)x2 = 2 - 1e17

Since both 1 - 1e17 and 2 - 1e17 are big they're rounded to one number, hence x2 = 1 (rounded)
But then x1 = (1 - x2) 1e17 = (1 - 1) 1e17 = 0

100 Sherman–Morrison updates: 0.523 ms
One inverse from scratch:     0.025 ms

So row updates are clearly slower