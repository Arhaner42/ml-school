Programming exercises

a)
T.reshape(2, 12)
[[ 0  1  2  3  4  5  6  7  8  9 10 11]
 [12 13 14 15 16 17 18 19 20 21 22 23]]

Clearly not rank 1, since rows are not multiples of each other 
Rank 2 : 
(1, 1) \otimes (0  1  2  3  4  5  6  7  8  9 10 11) + 
(0, 12) \otimes (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)

T.transpose(1, 0, 2).reshape(3, 8)
[[ 0  1  2  3 12 13 14 15]
 [ 4  5  6  7 16 17 18 19]
 [ 8  9 10 11 20 21 22 23]]

Clearly not rank 1, since rows are not multiples of each other 
Rank 2:
(1, 1, 1) \otimes (0  1  2  3 12 13 14 15) +
(0, 4, 8) \otimes (1, 1, 1, 1, 1, 1, 1, 1)

np.kron(A, B) stores (100*100)^2 = 1e8 values

say A, B, X are all 100x100

Multiplying np.kron(A, B) @ X requires to store 1e8 + 1e4 values
Muliplying AXB^T requires to store 3e4 values
So it's cheaper by memory

Assuming two matrices are multiplied in n^3 operations
Multiplying np.kron(A, B) @ X requires (1e8 * 1e4)^3 = 1e36 operations
Muliplying AX requires (1e4 * 1e4)^3 = 1e24 operations
then mutliplying (AX)@B.T requires (1e4 * 1e4)^3 = 1e24 operations
So in totat 2e24 opeations which is severly less, so by time it's a lot of cheaper