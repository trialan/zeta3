import sympy as sp
from zeta3.latex import generate_pdf

n, k = sp.symbols('n k')
a_n = sp.Symbol('a_n')


def tanh_add_formula(a, b):
    return (a + b) / (1 + a * b)


def construct_recursive_formula(k, previous_formula, a_n_seq):
    """
    Parameters:
    - k: The current index for which the formula is to be generated.
    - previous_formula: The formula for T_{k-1}.
    - a_n_seq: The symbolic representation of the sequence a_n.
    """
    return tanh_add_formula(previous_formula, sp.tanh(a_n_seq.subs(n, k)))


def generate_formulas(N, a_n_seq):
    formulas = {2: sp.tanh(a_n_seq.subs(n, 2))}
    for i in range(3, N+1):
        formula = formulas[i-1]
        for j in range(i-1, 2, -1):
            formula = formula.subs(formulas[j], construct_recursive_formula(j, formulas[j-1], a_n_seq))
        formulas[i] = construct_recursive_formula(i, formula, a_n_seq)
    return formulas



if __name__ == '__main__':
    example_formulas = generate_formulas(10, a_n)
    generate_pdf(example_formulas)
