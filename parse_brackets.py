from calculator import calculate

operand_string = "+-/*^"


def parse_brackets(expression):
    expr = expression.split()
    calculate_list = []
    k = 0
    x = 0
    y = 0
    a = expression.count("(")
    b = expression.count(")")
    if a != b:
        print("Error: Unequal number of brackets")
        return None
    while "(" in expression or ")" in expression:
        if "-" in expr or "+" in expr or "*" in expr or "/" in expr:
            calculate_list.clear()

            while 1:
                if expr[k] == "(":
                    x = k
                if expr[k] == ")":
                    y = k
                    break
                k += 1

            for i in range(x + 1, y):
                calculate_list.append(expr[i])
                calculate_list.append(" ")
            calculate_str = "".join(calculate_list)
            del expr[x: y + 1]
            result = calculate(calculate_str)

            if float(result) < 0 and expr[x - 1] == "-":
                expr[x - 1] = "+"
                result = float(result) * -1
                result = str(result)
            if float(result) < 0 and expr[x - 1] == "+":
                expr[x - 1] = "-"
                result = float(result) * -1
                result = str(result)
            expr.insert(x, result)
            expression = "".join(expr)
            k = 0
        else:
            print("Smth went wrong, try to type expression correctly")
            return None
    if "(" not in expression and ")" not in expression:
        final_result = calculate(expression)
        return final_result
    else:
        print("Smth went wrong, try to type expression correctly")
        return None
