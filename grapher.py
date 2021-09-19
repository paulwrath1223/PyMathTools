
from sympy import *
x = symbols('x')
expr = sympify(input("expression: \ny = ").replace("^", "**"))
rangeX = (input("range of x values to render: ex. \"a, b\"\n")).split(",")
if rangeX[0] > rangeX[1]:
    temp = rangeX[0]
    rangeX[0] = rangeX[1]
    rangeX[1] = temp
elif rangeX[0] == rangeX[1]:
    raise Exception("The range must be greater than 0")
else:
    yRange = (float(rangeX[0]), float(rangeX[1]))
    p1 = plot(sympify(expr), (x, rangeX[0], rangeX[1]), ylim=yRange, aspect_ratio=(1.0, 1.0))
