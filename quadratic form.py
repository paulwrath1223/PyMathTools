from sympy import *
import sympy
init_printing(use_unicode=True)
ar = 1
br = 0
cr = -49
a, b, c = symbols("a b c")
x1 = (-b+(sympy.sqrt(b**2-(4*a*c))))/2*a
print(x1.evalf(subs={a:ar, b:br, c:cr}))
