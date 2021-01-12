import re

dictionary = {}
all_keys = []
all_values = []

operand_string = "+-/*^"


def add_variable_to_dictionary(expression):
    pattern = "(\d+)(.(\d+))?"
    expr = expression.split()
    if not expr[0].isalpha():
        print("Invalid identifier")
        return
    elif not expr[2].isalpha() and not re.search(pattern, expr[2]):
        print("Invalid assignment")
        return
    elif len(expr) > 3:
        print("Invalid assignment")
        return
    elif expr[2].isalpha() and expr[2] not in all_keys:
        print("Unknown variable")
        return
    else:
        if expr[2].isalpha() and expr[2] in all_keys:
            expr[2] = dictionary[expr[2]]
        expr.remove("=")
        keys = expr[0]
        all_keys.append(keys)
        values = expr[1]
        all_values.append(values)
        dictionary[keys] = values


def replace_variable_with_value(expression):
    expr = expression.split()
    size = len(expr)
    for i in range(size):
        if expr[i] in all_keys:
            expr[i] = dictionary[expr[i]]
    return "".join(expr)


def show_variable_value(expression):
    if expression in all_keys:
        for key in dictionary.keys():
            if expression == key:
                print(dictionary[key])
                return
    else:
        print("Unknown variable")
        return


def allowed_symbols_checker(expression):
    pattern = "([a-zA-z]|[1234567890]|[\+\-\/\*\^]|\s)"
    if re.search(pattern, expression):
        return expression
    else:
        print("Forbidden symbols in expression")
        return None
