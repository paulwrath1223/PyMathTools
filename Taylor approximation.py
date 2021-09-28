from sympy import *
# from sympy.plotting import plot
# from sympy.solvers import solve


def multiplify(express):  # adds '*' in between ")(", "x(", "2x"
    express_list = list(str(express))
    out = ""
    counter1 = 0
    for counter1 in range(len(express_list)-1):
        char = express_list[counter1]
        out += char
        if char.isnumeric() or char == "x" or char == ")":
            next_char = express_list[counter1+1]
            if next_char == "x" or next_char == "(":
                out += "*"
    out += express_list[counter1+1]
    return out
    # sample: "2(x-1)" -> "2*(x-1)"


a, b, c, d, f, g, h, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, z = symbols(
    "a b c d f g h j k l m n o p q r s t u v w x z")  # declare a mathematical symbol for all letters except e and i

originalEq = multiplify(input(
        "enter equation with variables represented by lowercase letters. \ny = "))
originalEq = sympify(originalEq.replace("^", "**"))

tempIn = input("what point should the series center about\n")
targetX = float(tempIn)

tempIn = input("How many terms in the series? (int)\n")
try:
    seriesDegree = int(tempIn)
except:
    raise Exception("number of terms must be a positive integer")
if not (seriesDegree >= 1 and seriesDegree % 1 == 0):
    raise Exception("number of terms must be a positive integer")
else:
    factors = [sympify("1")]
    derivs = [originalEq]
    numerators = [originalEq.subs(x, targetX)]
    denominators = [1]
    assembledTerm = [(numerators[0] / denominators[0]) * factors[0]]
    completeSeries = assembledTerm[0]

    for counter in range(1, seriesDegree):
        lastFunc = derivs[counter-1]
        derivs.append(diff(lastFunc, x))
        numerators.append(simplify(derivs[counter].subs(x, targetX)))
        denominators.append(denominators[counter-1]*counter)
        factors.append(sympify((x-targetX)**counter))  # Make this not nasty pls
        assembledTerm.append((numerators[counter] / denominators[counter]) * factors[counter])
        completeSeries += assembledTerm[counter]
print(str(completeSeries).replace("**", "^"))
