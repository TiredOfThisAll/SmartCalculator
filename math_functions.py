class MathFunctions:
    def div_and_mul(self, expression):
        expr_list = expression.split()
        i = 0
        n = 0
        while "/" in expr_list or "*" in expr_list:
            if expr_list[i] == "/" and expr_list[i + 1] == "-" and \
                    float(expr_list[i+2] != 0):
                expr_list[i - 1] = str(-1 * (float(expr_list[i - 1]) /
                                             float(expr_list[i + 2])))
                del (expr_list[i])
                del (expr_list[i])
                del (expr_list[i])
                i -= 3
            elif expr_list[i] == "*" and expr_list[i + 1] == "-":
                expr_list[i - 1] = str(-1 * (float(expr_list[i - 1]) *
                                             float(expr_list[i + 2])))
                del (expr_list[i])
                del (expr_list[i])
                del (expr_list[i])
                i -= 3
            elif expr_list[i] == "/" and expr_list[i + 1] == "-" and \
                    float(expr_list[i + 2] == 0):
                print("Division by zero!")
                return
            elif expr_list[i] == "/" and float(expr_list[i + 1]) != 0:
                expr_list[i-1] = str(float(expr_list[i-1]) / float(expr_list[i+1]))
                del (expr_list[i])
                del (expr_list[i])
                i -= 2
            elif expr_list[i] == "/" and float(expr_list[i + 1]) == 0:
                print("Division by zero!")
                return
            elif expr_list[i] == "*" and expr_list[i + 1].isnumeric():
                expr_list[i-1] = str(float(expr_list[i-1]) * float(expr_list[i+1]))
                del (expr_list[i])
                del (expr_list[i])
                i -= 2
            i += 1
        list_size = len(expr_list)
        for i in range(list_size):
            if expr_list[i] == "+" or expr_list[i] == "-":
                n += 1
        for i in range(1, list_size + n * 2, 2):
            expr_list.insert(i, " ")
        return "".join(expr_list)

    def plus_and_minus(self, expression):
        i = 0
        expr_list = expression.split()
        while "+" in expr_list or "-" in expr_list:
            if expr_list[i] == "+":
                expr_list[i-1] = str(float(expr_list[i-1]) + float(expr_list[i+1]))
                del (expr_list[i])
                del (expr_list[i])
                i -= 2
            elif expr_list[i] == "-":
                expr_list[i-1] = str(float(expr_list[i-1]) - float(expr_list[i+1]))
                del (expr_list[i])
                del (expr_list[i])
                i -= 2
            i += 1
        return "".join(expr_list)

    def power(self, expression):
        i = 0
        expr_list = expression.split()
        while "^" in expr_list:
            if expr_list[i] == "^":
                expr_list[i-1] = str(pow(float(expr_list[i-1]), float(expr_list[i+1])))
                del (expr_list[i])
                del (expr_list[i])
                i -= 2
            i += 1
        return "".join(expr_list)
