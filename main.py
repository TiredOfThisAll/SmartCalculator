from calculator import calculate
from parse_brackets import parse_brackets
from my_dictionary import show_variable_value, add_variable_to_dictionary

HELP_MESSAGE = """Type your expression in the next format:
              x + y * ( c + ( s + z ) ) 
              Calculator supports addition, subtraction, multiplication, 
              division, alphabetic variables and brackets 
              To use alphabetic variables you should type 'variable' = 'value' 
              -> then you can use your variable in the expression 
              The variable name must be written in English with a lowercase 
              letter 
              You can also set the value of a new variable using an existing one
              """


while True:
    expression = input("Type your expression\n")
    if expression == "":
        continue
    elif expression == "/exit":
        print("Bye!")
        exit()
    elif expression == "/help":
        print(HELP_MESSAGE)
        continue
    elif expression[0] == "/":
        print("Unknown command")
        continue
    elif expression.isalpha():
        show_variable_value(expression)
        continue
    if "(" in expression or ")" in expression:
        result = parse_brackets(expression)
        print(result)
        continue
    if "=" not in expression:
        result = calculate(expression)
        print(result)
        continue
    else:
        add_variable_to_dictionary(expression)
        continue
