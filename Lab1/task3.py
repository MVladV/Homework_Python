# task3

sign = ('+', '-')
number = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
symbol = ("number", "function")

#number = true, sign = false


def is_legal_statement(expression, symb):
    if len(expression) == 0:
        return True
    if expression[0] in number and symb:
        symb = False
        return is_legal_statement(expression[1:], symb)
    elif expression[0] in sign and not symb:
        symb = True
        return is_legal_statement(expression[1:], symb)
    else:
        return False


def main():
    try:    
        user_string = input("Input expression: ")
        if len(user_string) > 2:
            if is_legal_statement(user_string, True):
                print("(True,", eval(''.join(user_string)), ")")
            else:
                print("(False,None)")
    except Exception:
        print("Exeption!")

main()    