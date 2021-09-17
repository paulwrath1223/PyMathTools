from sympy import *

from sympy.solvers import solve
init_printing(use_unicode=True)

# test eq: (x^2-1)/(x^2-2*x-3)

holes = []
vAsymptotes = []

x = symbols("x")
while True:
    originalEq = input("enter equation with x.\ny = ").replace("^", "**")

    brokenExpr = originalEq.split("/")
    numerator = sympify(brokenExpr[0])
    denominator = sympify(brokenExpr[1])
    nIssues = solve(numerator, x)
    dIssues = solve(denominator, x)
    for num in dIssues:
        if num in nIssues:
            holes.append(num)
        else:
            vAsymptotes.append(num)
    holesFormatted = str(holes).replace("[", "").replace("]", "")
    vAsymptotesFormatted = str(vAsymptotes).replace("[", "").replace("]", "")
    print(f"Holes: x = {holesFormatted}\nVertical Asymptotes: x = {vAsymptotesFormatted}")
    fullNum = expand(numerator)
    fullDen = expand(denominator)
    firstTermNum = sympify(str(fullNum).split()[0])
    firstTermDen = sympify(str(fullDen).split()[0])
    sAsymptote = firstTermNum/firstTermDen
    print(f"Slant asymptote: y = {sAsymptote}")
