import sympy as sp
import subprocess
import os


def generate_list_latex_document(formulas):
    document = """
\\documentclass{article}
\\usepackage{graphicx} % Required for inserting images
\\usepackage[landscape]{geometry} % For landscape orientation
\\usepackage{amsmath} % For mathematical formatting

\\title{Atanh - Zeta3}
\\author{thomas.rialan}
\\date{October 2023}

\\begin{document}

\\maketitle

\\section{Introduction}
"""
    for i, formula in enumerate(formulas):
        numerator_terms = formula.as_numer_denom()[0].as_ordered_terms()
        denominator_terms = formula.as_numer_denom()[1].as_ordered_terms()
        numerator_latex = ', '.join([sp.latex(term) for term in numerator_terms])
        denominator_latex = ', '.join([sp.latex(term) for term in denominator_terms])
        document += f"\nNumerator terms: \\[{numerator_latex}\\]\n"
        document += f"Denominator terms: \\[{denominator_latex}\\]\n"
    document += "\n\\end{document}"
    return latex_to_pdf(document)


def generate_latex_document(formulae):
    document = """
\\documentclass{article}
\\usepackage{graphicx} % Required for inserting images
\\usepackage[landscape]{geometry} % For landscape orientation
\\usepackage{breqn} % For automatic equation breaking

\\title{zeta(3) approximation}
\\author{thomas.rialan}
\\date{October 2023}

\\begin{document}

\\maketitle

\\section{Introduction}
"""
    for i, formula in formulae.items():
        formula_latex = sp.latex(formula)
        document += f"\n\\begin{{dmath*}}\n{formula_latex}\n\\end{{dmath*}}\n"
    document += "\n\\end{document}"
    return latex_to_pdf(document)


def latex_to_pdf(latex_content, output_filename="output_latex/output"):
    with open(output_filename + ".tex", 'w') as file:
        file.write(latex_content)
    subprocess.run(["pdflatex", output_filename + ".tex"])
    if os.path.exists(output_filename + ".pdf"):
        print(f"PDF generated: {output_filename}.pdf")
    else:
        print("Error generating PDF.")
