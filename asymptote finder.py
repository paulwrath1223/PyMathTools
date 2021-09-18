


from sympy import *
from sympy.plotting import plot
from sympy.solvers import solve


init_printing(use_unicode=True)

# test eq: (x^2-1)/(x^2-2*x-3)

holes = []
vAsymptotes = []
holeXY = []

x, y = symbols("x y")  # declare x and y as mathematical symbols
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

    simpleIn = simplify(originalEq)
    print(f"simpleIn: {simpleIn}")
    for a in holes:
        holeX = float(a)
        holeY = float(simpleIn.subs(x, holeX))
        holeXY.append((holeX, holeY))

    holesFormatted = str(holeXY).replace("[", "").replace("]", "")
    vAsymptotesFormatted = str(vAsymptotes).replace("[", "").replace("]", "")
    print(f"Holes: {holesFormatted}\nVertical Asymptotes: x = {vAsymptotesFormatted}")
    fullNum = expand(numerator)
    fullDen = expand(denominator)
    firstTermNum = sympify(str(fullNum).split()[0])
    firstTermDen = sympify(str(fullDen).split()[0])
    sAsymptote = firstTermNum/firstTermDen
    print(f"Slant asymptote: y = {sAsymptote}")
    if input("see graph? (y/n)") == "y":
        rangeX = (input("range of x values to render: ex. \"a, b\"\n")).split(",")
        if rangeX[0] > rangeX[1]:
            temp = rangeX[0]
            rangeX[0] = rangeX[1]
            rangeX[1] = temp
        elif rangeX[0] == rangeX[1]:
            raise Exception("The range must be greater than 0")
        else:

            p1 = plot(sympify(originalEq), (x, rangeX[0], rangeX[1]), show=False)
            for expr in vAsymptotes:
                p1.append(plot_implicit((Eq(x, expr)), (x, rangeX[0], rangeX[1]),
                                        show=False, line_color="r")[0])
            for h in holeXY:
                hX = str(h[0])
                hY = str(h[1])
                ex = sympify("(x-"+hX+")**2+(y-"+hY+")**2")
                p1.append(plot_implicit(Eq(ex, 0.04), (x, rangeX[0], rangeX[1]),
                                        show=False, line_color="b")[0])
            p1.append(plot(sympify(sAsymptote), (x, rangeX[0], rangeX[1]),
                           show=False, line_color="g")[0])
            p1.show()