from pprint import pprint
import sympy as sp
from zeta3.latex import generate_pdf


def tanh_add_formula(a, b):
    return (sp.tanh(a) + sp.tanh(b)) / (1 + sp.tanh(a) * sp.tanh(b))


def generate_specific_formulas(N):
    a_terms = [sp.Symbol(f'a_{i}') for i in range(0, N)]
    formulas = {0: sp.tanh(a_terms[0])}
    for i in range(1, N):
        formulas[i] = (formulas[i-1] + sp.tanh(a_terms[i])) / (1 + formulas[i-1] * sp.tanh(a_terms[i]))
    return formulas


if __name__ == '__main__':
    example_formulas = generate_specific_formulas(5)
    pprint(example_formulas)
