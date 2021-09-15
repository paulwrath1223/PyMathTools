from sympy import *
import sympy
init_printing(use_unicode=True)
ar = input("A value\n")
br = input("\nB value\n")
cr = input("\nC value\n")
a, b, c = symbols("a b c")
x1 = (-b+(sympy.sqrt(b**2-(4*a*c))))/2*a
x2 = (-b-(sympy.sqrt(b**2-(4*a*c))))/2*a
x1r = x1.evalf(subs={a:ar, b:br, c:cr})
x2r = x2.evalf(subs={a:ar, b:br, c:cr})
print(f"X = {x1r}, {x2r}")
