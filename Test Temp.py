
# x - x^3/6 + O(x^5)

def big_o_adios(expr_in):
    temp = str(expr_in.split("O")[0])
    return temp[0:len(temp)-2]


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


print(big_o_adios(multiplify("x - x**3/6 + O(x**5")))
