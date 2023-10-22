from sympy.printing import latex
import os
import shutil
import tempfile


def generate_pdf(formulas, output_dir="."):
    latex_content = generate_latex_content(formulas)
    generate_pdf_from_latex(latex_content, output_dir)


def generate_latex_content(formulas):
    """Generate LaTeX content based on the provided formulas."""
    latex_content = r"""
\documentclass{article}
\usepackage{amsmath}
\begin{document}
"""
    for k, formula in formulas.items():
        latex_formula = latex(formula)
        latex_content += r"\[ T_{" + str(k) + "} = " + latex_formula + r" \]" + "\n"
    latex_content += r"\end{document}"
    return latex_content


def generate_pdf_from_latex(latex_content, output_path):
    temp_dir = tempfile.mkdtemp()
    latex_file_path = os.path.join(temp_dir, "output.tex")
    with open(latex_file_path, "w") as latex_file:
        latex_file.write(latex_content)
    os.system(f"pdflatex -output-directory={temp_dir} {latex_file_path}")
    shutil.move(os.path.join(temp_dir, "output.pdf"), output_path)
    shutil.rmtree(temp_dir)
