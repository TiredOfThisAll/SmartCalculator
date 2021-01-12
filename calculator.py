from string_formatting import StringFormatting
from math_functions import MathFunctions
from my_dictionary import replace_variable_with_value, allowed_symbols_checker


def calculate(expression):
    expr = expression
    if "+" not in expr and "-" not in expr and "*" \
            not in expr and "/" not in expr:
        print("Error: Invalid expression")
        return
    expr = allowed_symbols_checker(expr)
    if expr is None:
        return
    expr = StringFormatting.space_inserter(expr)
    expr = replace_variable_with_value(expr)
    expr = StringFormatting.space_inserter(expr)
    expr = StringFormatting.string_cleaner(expr)
    if expr is None:
        return
    expr = StringFormatting.space_inserter(expr)

    math_functions = MathFunctions()
    if "^" in expr and ("*" not in expr and "/" not in expr and "+" not in
                        expr and "-" not in expr):
        expr = math_functions.power(expr)
        return expr
    if "^" in expr:
        expr = math_functions.power(expr)
        expr = StringFormatting.space_inserter(expr)
        expr = math_functions.div_and_mul(expr)
        if expr is None:
            return
        expr = math_functions.plus_and_minus(expr)
        return expr
    if ("/" in expr or "*" in expr) and ("+" not in expr and "-" not in expr):
        expr = math_functions.div_and_mul(expr)
        return expr
    if ("/" in expr or "*" in expr) and ("+" in expr or "-" in expr):
        expr = math_functions.div_and_mul(expr)
        if expr is None:
            return
        expr = math_functions.plus_and_minus(expr)
        return expr
    if "+" in expr or "-" in expr:
        expr = math_functions.plus_and_minus(expr)
        return expr
    else:
        return "Whoops, smth went wrong"
