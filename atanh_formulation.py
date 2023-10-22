import sympy as sp

# Symbolic variable declaration
n, k, N = sp.symbols('n k N')
a_n = sp.atanh(1/n**3)

# Initial value for T_2
T_2 = sp.tanh(a_n.subs(n, 2))

# Recursive formula for T_k
T_k = sp.Function('T')(k)
T_k_minus_1 = sp.Function('T')(k-1)
tanh_sum_formula = (T_k_minus_1 + sp.tanh(a_n.subs(n, k))) / (1 + T_k_minus_1 * sp.tanh(a_n.subs(n, k)))

# Expressing T_k in terms of T_{k-1}
T_k_expr = sp.Eq(T_k, tanh_sum_formula)

# Generating the expressions for several terms
results = [T_2]
for i in range(3, N+1):
    term = T_k_expr.subs(k, i)
    results.append(term)

for result in results:
    print(result)

