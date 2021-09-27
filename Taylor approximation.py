from sympy import *
from sympy.plotting import plot
from sympy.solvers import solve


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


def diff(x_derivs_known, func_t, func_k, bool_simplify=False):
    try:
        func_n = len(x_derivs_known)
    except TypeError:
        func_n = None
    if func_n is None:
        result = diff(x_derivs_known, func_t, func_k)
        if bool_simplify:
            result = result.simplify()
    elif func_k < func_n:
        result = x_derivs_known[func_k]
    else:
        i = func_n - 1
        result = x_derivs_known[i]
        while i < func_k:
            result = result.diff(func_t)
            j = len(x_derivs_known)
            x0 = None
            while j > 1:
                j -= 1
                result = result.subs(Derivative(x_derivs_known[0], func_t, j), x_derivs_known[j])
            i += 1
            if bool_simplify:
                result = result.simplify()
    return result


a, b, c, d, f, g, h, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z = symbols(
    "a b c d f g h j k l m n o p q r s t u v w x y z")  # declare a mathematical symbol for all letters except e and i

originalEq = multiplify(input(
        "enter equation with variables represented by lowercase letters. "))

