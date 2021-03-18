

def is_numeric(char: str) -> bool:
    """accepts string character and checks it for validation"""
    validate = False
    if char in [".", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        validate = True
    return validate


def is_math_symbol(operand: str) -> bool:
    """accepts a string character and validates as operator"""
    validate = False
    if operand in ["+", "-", "x", "/", '\\' , "%"]:
        validate = True
    return validate


def get_math_answer(operator: str, operand1: str, operand2: str) -> float:
    """accepts 2 operands and an operator and returns the value of the
    operands: product or sum or difference as float"""
    operand1_val = float(operand1)
    operand2_val = float(operand2)

    if operator == "+":
        function = operand1_val + operand2_val
    elif operator == "-":
        function = operand1_val - operand2_val
    elif operator == "x":  # or operator == "*":
        function = operand1_val * operand2_val
    elif operator == "/":
        function = operand1_val / operand2_val
    elif operator == "\\":
        function = operand1_val // operand2_val
    elif operator == "%":
        function = operand1_val % operand2_val
    else:
        function = 0.0000
    return function
