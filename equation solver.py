from sympy import *

from sympy.solvers import solve
init_printing(use_unicode=True)


a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z = symbols("a b c d e f g h i j k l m n o p q r s t u v w x y z")
originalEq = input("enter equation with variables represented by lowercase variables.\n")
originalEq = "("+originalEq.replace("=",")-(")+")"
varLetter = input("What variable should be solved for? ")

expression = sympify(originalEq)
varToSolveFor = sympify(varLetter)

answer = (solve(expression, varToSolveFor))
answerFormatted = (str(answer)).replace("[","").replace("]","")
print(f"Solution:\n{varToSolveFor} = {answerFormatted}")

