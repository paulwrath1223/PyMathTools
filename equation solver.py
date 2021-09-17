from sympy import *

from sympy.solvers import solve
init_printing(use_unicode=True)


a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z = symbols\
    ("a b c d e f g h i j k l m n o p q r s t u v w x y z")
while True:
    originalEq = input\
        ("enter equation with variables represented by lowercase variables. You MUST add \"*\", you cannot do \"2x\"\n")

    originalEq = "("+originalEq.replace("=", ")-(")+")".replace("^", "**")
    varLetter = input("What variable should be solved for?\n")

    expression = sympify(originalEq)
    varToSolveFor = sympify(varLetter)

    answer = sympify(solve(expression, varToSolveFor))
    answerFormatted = (str(answer)).replace("[", "").replace("]", "").replace("**", "^")
    print(f"Solution:\n{varToSolveFor} = {answerFormatted}")

    # NOT WORKING, Try subbing before the solution and resolving

    subLetter = sympify(input("What variable should be substituted? (\"none\" to skip)\n"))
    while subLetter != sympify("none"):
        replacement = input("What should it be replaced with?\n")
        for i in range(len(answer)):
            x = answer[i]
            x = x.subs(subLetter, replacement)
            answer[i] = x

        answerFormatted = (str(answer)).replace("[", "").replace("]", "").replace("**", "^")
        print(f"Solution:\n{varToSolveFor} = {answerFormatted}")
        subLetter = sympify(input("Next variable to be substituted?\n"))
    if input("evaluate? (y/n)") == "y":
        for i in range(len(answer)):
            x = answer[i]
            x = x.evalf(10)
            answer[i] = x
        answerFormatted = (str(answer)).replace("[", "").replace("]", "").replace("**", "^")
        print(f"Solution:\n{varToSolveFor} = {answerFormatted}")
