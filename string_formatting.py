import re

operand_string = "+-/*^"
pattern = "^([-]?)(\d+)(.(\d+))?(?:([-+*\^\/]|(\*\-)|(\/\-)|(\^\-))(\d+)" +\
          "(.?(\d+))?)+$"


class StringFormatting:

    @staticmethod
    def string_cleaner(expression):
        expr = expression.split()
        expr = "".join(expr)

        if re.search(pattern, expr) is None:
            print("Error: Multiple operators")
            return None
        if expr[0] in operand_string:
            print("Error: Operator at the beginning of the expression")
            return None
        if expr[-1] in operand_string:
            print("Error: Operator in the end of the expression")
            return None
        return "".join(expr)

    @staticmethod
    def space_inserter(expression):
        expr = list(expression)
        size = len(expr)
        n = 0
        for i in range(size):
            if expr[i] in operand_string:
                n += 1
        i = 0
        while i <= n * 3:
            if expr[i] in operand_string:
                expr.insert(i + 1, " ")
                expr.insert(i, " ")
                i += 2
                continue
            i += 1
        return "".join(expr)
