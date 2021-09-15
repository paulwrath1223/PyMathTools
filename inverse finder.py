from sympy import *
from sympy.solvers import solve
init_printing(use_unicode=True)
x, y = symbols("x y")
originalEq = input("enter expression with \"x\".\ny = ")
inverse = sympify(originalEq)
inverse = inverse.subs(x, y)
inverseSimplified = (solve(inverse-x, y))
inverseSimplifiedFormatted = (str(inverseSimplified)).replace("[","").replace("]","")
print(f"Y = {inverseSimplifiedFormatted}")

