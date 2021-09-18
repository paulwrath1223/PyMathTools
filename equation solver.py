from sympy import *

from sympy.solvers import solve
init_printing(use_unicode=True)  # Don't even know what this does


a, b, c, d, f, g, h, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z = symbols(
    "a b c d f g h j k l m n o p q r s t u v w x y z")  # declare a mathematical symbol for all letters except e and i
while True:
    originalEq = input(
        "enter equation with variables represented by lowercase variables. You MUST add \"*\", you cannot do \"2x\"\n")

    originalEq = "("+originalEq.replace(  # convert equation to an expression equal to 0
        "=", ")-(")+")".replace("^", "**")
    varLetter = input("What variable should be solved for?\n")

    expression = sympify(originalEq)  # convert these strings to expression objects
    varToSolveFor = sympify(varLetter)

    answer = sympify(solve(expression, varToSolveFor))  # returns list of answers
    answerFormatted = (str(answer)).replace("[", "").replace("]", "").replace("**", "^")  # make it look pretty
    print(f"Solution:\n{varToSolveFor} = {answerFormatted}")

    subLetter = input("What variable should be substituted? (\"none\" to skip)\n")
    while subLetter != "none":
        subLetter = sympify(subLetter)
        replacement = input("What should it be replaced with?\n")
        for i in range(len(answer)):  # substitute all occurrences of subLetter within the expression with replacement
            x = answer[i]
            x = x.subs(subLetter, replacement)
            answer[i] = x

        answerFormatted = (str(answer)).replace("[", "").replace("]", "").replace("**", "^")  # formatting
        print(f"Solution:\n{varToSolveFor} = {answerFormatted}")
        subLetter = sympify(input("Next variable to be substituted?\n"))  # repeat sub loop until user says none
    if input("evaluate? (y/n)") == "y":
        for i in range(len(answer)):
            x = answer[i]
            x = x.evalf(10)  # attempt to evaluate the expressions that represent the variable the user wanted solved
            answer[i] = x
        answerFormatted = (str(answer)).replace("[", "").replace("]", "").replace("**", "^")  # formatting
        print(f"Solution:\n{varToSolveFor} = {answerFormatted}")
