import math
from sympy import *

ac = Symbol("ac")


# TODO implement numerical solve

def area_from_minus_one_to_f(f):
    return sympify(((f * (1 - f ** 2) ** 0.5) + asin(f)) + math.pi / 2)


def get_distances_abs(num_sections, radius):
    target = math.pi / num_sections
    for i in range(num_sections - 1):
        pauls_expression = area_from_minus_one_to_f(ac)
        answer = nsolve(pauls_expression - (target * (i + 1)), ac, 0)
        print(f"cut {i + 1} at {radius + answer * radius} units from the side")


get_distances_abs(3, 1)
