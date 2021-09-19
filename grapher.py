
from sympy import *


def multiplify(express):  # adds '*' in between ")(", "
    express_list = list(str(express))
    out = ""
    counter = 0
    for counter in range(len(express_list)-1):
        char = express_list[counter]
        out += char
        if char.isnumeric() or char == "x" or char == ")":
            next_char = express_list[counter+1]
            if next_char == "x" or next_char == "(":
                out += "*"
    out += express_list[counter+1]
    return out
    # sample: "2(x-1)" -> "2*(x-1)"


x = symbols('x')
expr = sympify(multiplify(input("expression: \ny = ").replace("^", "**")))
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
