from pprint import pprint
import sympy as sp
from zeta3.latex import generate_latex_document, generate_list_latex_document


def generate_partial_formulae(N):
    a_terms = [sp.Symbol(f'a_{i}') for i in range(0, N)]
    formulae = [sp.tanh(a_terms[0])]
    for i in range(1, N):
        formulae.append(generate_f_recursively(formulae[i-1], a_terms[i]))
        formulae[i] = simplify(formulae[i])
    return formulae[1:]


def generate_f_recursively(last_f, next_term):
    out = (last_f + sp.tanh(next_term)) / (1 + last_f * sp.tanh(next_term))
    return out


def lambdify_formula(formula):
    """Convert a symbolic formula to a numerical function."""
    symbols = sorted(formula.free_symbols, key=lambda x: x.name)
    numerical_function = sp.lambdify(symbols, formula, 'numpy')
    return numerical_function


def simplify(formula):
    expanded_formula = expand(formula)
    simplified_formula = sp.simplify(expanded_formula)
    return simplified_formula


def expand(formula):
    expanded_formula = sp.expand(formula)
    for symbol in expanded_formula.free_symbols:
        if "tanh" in str(symbol):
            expanded_formula = expanded_formula.subs(symbol,
                                                     sp.atanh(sp.tanh(symbol)))
    return expanded_formula


if __name__ == '__main__':
    formulae = generate_partial_formulae(5)
    doc = generate_list_latex_document(formulae)



