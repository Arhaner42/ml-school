Programming exercises
Answer to the question for polynomial interpolation

Lagrange polynomials are basis for $P_d(R)$ (polymomials of degree <= d) 

Vectors (1, t, ..., t^d) form a basis of P_d(R). 

Define functional phi_k(p) = p(t_k), so is relative to standard basis of P_d(R) phi_k = (1, t_k, ..., (t_k)^d) which is Vandemort matrix. and phi_k are basis to dual space of P_d(R)

Let's check dual basis condition phi_k(L_m) = L_m(t_k) = \delta_{k, m} precisely

So recalling proposition 8.7 (swapping R^n and (R^n)^*) we get desired

Near ends of interval, interpolation polnomial strongly deviates with oscilatory manner (up, then down, then up)