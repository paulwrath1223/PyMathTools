from sympy import *
import sympy
init_printing(use_unicode=True)
x, y, z = symbols("x y z")
originalEq = input("enter equation with \"x\" and \"y\"")
inverse = (parse_expr(originalEq, evaluate=False))
inverse.subs(x, z)
inverse.subs(y, x)
inverse.subs(z, x)
print(inverse)