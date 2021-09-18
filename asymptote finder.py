
from sympy import *
from sympy.plotting import plot
from sympy.solvers import solve


# test eq: (x^2-1)/(x^2-2*x-3)

holeRadius = 0.2  # constant representing the radius of the holes drawn on the plot

holes = []
vAsymptotes = []
holeXY = []

x, y = symbols("x y")  # declare x and y as mathematical symbols
while True:
    originalEq = input("enter equation with x.\ny = ").replace("^", "**")  # sympy uses '**' for powers

    brokenExpr = originalEq.split("/")  # split the equation into a list containing the numerator and denominator
    numerator = sympify(brokenExpr[0])
    denominator = sympify(brokenExpr[1])  # sympify converts strings to mathematical expressions
    nIssues = solve(numerator, x)
    dIssues = solve(denominator, x)  # finds all values of x that make the denominator = 0
    for num in dIssues:  # loop through undefined x values
        if num in nIssues:
            holes.append(num)  # if the x value also makes the numerator = 0, then it is a hole, not an asymptote
        else:
            vAsymptotes.append(num)  # else: its a vertical asymptote

    simpleIn = simplify(originalEq)  # factor the original equation
    print(f"factored equation: {simpleIn}")
    for a in holes:
        holeX = float(a)
        holeY = float(simpleIn.subs(x, holeX))  # use factored eq to find what the y value of the holes 'should' be
        holeXY.append((holeX, holeY))  # add coordinate pair to the list 'holeXY' as a float tuple

    holesFormatted = str(holeXY).replace("[", "").replace("]", "")  # make the coordinates look nice when printed
    vAsymptotesFormatted = str(vAsymptotes).replace("[", "").replace("]", "")  # format the strings for humans
    print(f"Holes: {holesFormatted}\nVertical Asymptotes: x = {vAsymptotesFormatted}")
    fullNum = expand(numerator)
    fullDen = expand(denominator)  # expand both numerator and denominator to unfactored form
    firstTermNum = sympify(str(fullNum).split()[0])  # find the first (biggest) term in each
    firstTermDen = sympify(str(fullDen).split()[0])
    sAsymptote = firstTermNum/firstTermDen  # find slant asymptote by dividing the highest degree terms
    print(f"Slant asymptote: y = {sAsymptote}")
    if input("see graph? (y/n) ") == "y":
        rangeX = (input("range of x values to render: ex. \"a, b\"\n")
                  ).split(",")  # returns list containing the bounds for X
        if rangeX[0] > rangeX[1]:  # if bounds are backwards, switch them
            temp = rangeX[0]
            rangeX[0] = rangeX[1]
            rangeX[1] = temp
        elif rangeX[0] == rangeX[1]:
            raise Exception("The range must be greater than 0")  # raise error if the range = 0
        else:  # if the range provided is valid

            p1 = plot(sympify(originalEq), (x, rangeX[0], rangeX[1]), show=False)  # add original equation to p1
            for expr in vAsymptotes:
                p1.append(plot_implicit((Eq(x, expr)), (x, rangeX[0], rangeX[1]),  # add all vertical asymptotes
                                        show=False, line_color="r")[0])
            for h in holeXY:
                hX = h[0]
                hY = h[1]
                ex = sympify("(x-"+str(hX)+")**2+(y-"+str(hY)+")**2")
                p1.append(plot_implicit(Eq(ex, holeRadius**2), (x, hX - holeRadius, hX + holeRadius), show=False,
                                        line_color="b", adaptive=False, nb_of_points=400)[0])  # add circles for holes

            p1.append(plot(sympify(sAsymptote), (x, rangeX[0], rangeX[1]),
                           show=False, line_color="g")[0])  # add slant asymptote
            p1.show()  # render plot
