from sympy import *

from sympy.solvers import solve
init_printing(use_unicode=True)  # Don't even know what this does


a, b, c, d, f, g, h, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z = symbols(
    "a b c d f g h j k l m n o p q r s t u v w x y z")  # declare a mathematical symbol for all letters except e and i


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


while True:
    originalEq = multiplify(input(
        "enter equation with variables represented by lowercase letters. "))

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
        replacement = multiplify(input("What should it be replaced with?\n"))
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
