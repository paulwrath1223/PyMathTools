
from sympy import *
from sympy.plotting import plot
from sympy.solvers import solve

# test eq: (x^2-1)/(x^2-2x-3)     (3x^2-2x+1)/(x-1)       (3x^5-x^2)/(x+3)     (3x^2+2)/(x^2+4x-5)

holeRadius = 0.2  # constant representing the radius of the holes drawn on the plot

holes = []
vAsymptotes = []
holeXY = []

x, y = symbols("x y")  # declare x and y as mathematical symbols


def multiplify(express):
    express_list = list(str(express))
    out = ""
    for counter in range(len(express_list)):
        char = express_list[counter]
        out += char
        if char.isnumeric() or char == "x":
            next_char = express_list[counter+1]
            if next_char == "x" or next_char == "(":
                out += "*"
    return out
    # sample: "2(x-1)" -> "2*(x-1)"


def get_poly_degree(polynomial):
    broken_first_term_poly = str(polynomial).split("**")  # returns the degree of the biggest term in the polynomial
    if len(broken_first_term_poly) == 2:  # if '**' is present, the degree is what follows
        poly_degree = int(broken_first_term_poly[1])
    elif len(broken_first_term_poly) == 1:  # if the biggest term does not have an exponent, the degree is 1
        poly_degree = 1
    else:
        raise Exception("internal problem within get_poly_degree for polynomial")
    return poly_degree


def get_slant(num, den):
    full_num = expand(num)
    full_den = expand(den)  # expand both numerator and denominator to unfactored form
    first_term_num = sympify(str(full_num).split()[0])  # find the first (biggest) term in each
    first_term_den = sympify(str(full_den).split()[0])

    num_degree = get_poly_degree(first_term_num)  # returns the degree of the biggest term in the numerator
    den_degree = get_poly_degree(first_term_den)  # returns the degree of the biggest term in the denominator

    if num_degree < den_degree:  # case 1 from \/
        # https://courses.lumenlearning.com/ivytech-collegealgebra/chapter/identify-vertical-and-horizontal-asymptotes/
        return 0
    elif num_degree - 1 == den_degree:
        q = div(num, den)
        return q[0]
    else:
        return first_term_num / first_term_den  # find slant asymptote by dividing the highest degree terms


while True:
    originalEq = multiplify(input(
        "enter equation with x.\ny = ").replace("^", "**"))  # sympy uses '**' for powers, but I use '^'

    brokenExpr = originalEq.split("/")  # split the equation into a list containing the numerator and denominator
    numerator = sympify(brokenExpr[0])
    denominator = sympify(brokenExpr[1])
    nIssues = solve(numerator, x)  # finds all values of x that make the numerator = 0
    dIssues = solve(denominator, x)  # finds all values of x that make the denominator = 0
    for numb in dIssues:  # loop through undefined y values
        if numb in nIssues:
            holes.append(numb)  # if the x value also makes the numerator = 0, then it is a hole, not an asymptote
        else:
            vAsymptotes.append(numb)  # else: its a vertical asymptote

    simpleIn = simplify(originalEq)  # factor the original equation
    print(f"factored equation: {simpleIn}")
    for a in holes:
        holeX = float(a)
        holeY = float(simpleIn.subs(x, holeX))  # use factored eq to find what the y value of the holes 'should' be
        holeXY.append((holeX, holeY))  # add coordinate pair to the list 'holeXY' as a float tuple

    holesFormatted = str(holeXY).replace("[", "").replace("]", "")  # make the coordinates look nice when printed
    vAsymptotesFormatted = str(vAsymptotes).replace("[", "").replace("]", "")  # format the strings for humans
    print(f"Holes: {holesFormatted}\nVertical Asymptotes: x = {vAsymptotesFormatted}")
    sAsymptote = get_slant(numerator, denominator)
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
            yRange = (float(rangeX[0]), float(rangeX[1]))
            p1 = plot(sympify(originalEq), (x, rangeX[0], rangeX[1]), ylim=yRange,
                      show=False, aspect_ratio=(1.0, 1.0))  # add original equation to p1
            for expr in vAsymptotes:
                p1.append(plot_implicit((Eq(x, expr)), (x, rangeX[0], rangeX[1]),  # add all vertical asymptotes
                                        show=False, aspect_ratio=(1.0, 1.0), ylim=yRange, line_color="r")[0])
            for h in holeXY:
                hX = h[0]
                hY = h[1]
                ex = sympify("(x-"+str(hX)+")**2+(y-"+str(hY)+")**2")
                p1.append(plot_implicit(Eq(ex, holeRadius**2), (x, hX - holeRadius, hX + holeRadius),
                                        (y, hY - holeRadius, hY + holeRadius),
                                        show=False, line_color="b", aspect_ratio=(1.0, 1.0), ylim=yRange,
                                        adaptive=False, nb_of_points=400)[0])  # add circles for holes

            p1.append(plot(sympify(sAsymptote), (x, rangeX[0], rangeX[1]), ylim=yRange,
                           show=False, line_color="g", aspect_ratio=(1.0, 1.0))[0])  # add slant asymptote
            p1.show()  # render plot
