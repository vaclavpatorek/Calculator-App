##
# @file calculator.py
# @brief Calculator application based on mathli
# @author Radim Mifka (xmifka00)
# @date April 2023

import re

import mathlib
from config import OPS, PRECEDENCE
from exceptions.syntax import SyntaxError


##
# @brief Check if string is number
# @param s String to check
# @return True if string is number, False otherwise
def is_number(s):
    pattern = r'^-?\d+(?:\.\d+)?$'
    return bool(re.match(pattern, s))


##
# @brief Check if can prepend character
# @param tokens: list of tokens
# @return: boolean (True or False)
def can_prepend(tokens):
    # TRUE -> tokens empty
    # TRUE -> last token is not number or is not closing bracket
    # FALSE -> otherwise
    return not tokens or (not is_number(tokens[-1]) and tokens[-1] != ')')


##
# @brief Check if log exist before in tokens
# @param tokens: list of tokens
# @return: boolean (True or False)
def log_exist_before(tokens):
    return len(tokens) > 1 and tokens[-2] == 'log'


##
# @brief Check if log is last in tokens
# @param tokens: list of tokens
# @return: boolean (True or False)
def log_last(tokens):
    return tokens and tokens[-1] == 'log'


##
# @brief Tokenize expression
# @param expression: expression to tokenize
# @return: list of tokens
def tokenize(expression):
    expression = expression.replace(" ", "")
    wops = {
        'l': 'log',
        'n': 'ln',
    }

    for key in wops:
        expression = expression.replace(wops.get(key), key)
    tokens = []
    current_token = ""
    for c in expression:
        if c in OPS or c in wops.keys():
            # already have number
            if current_token:
                if current_token[0] == '.':
                    current_token = "0" + current_token
                tokens.append(current_token)

            # same operations in succession
            if tokens and c == tokens[-1]:
                continue

            # insert 10 after blank log as base
            if log_exist_before(tokens) and is_number(tokens[-1]):
                tokens.insert(-1, '10')

            # check if number should be negative
            if c == '-' and can_prepend(tokens):
                current_token = '-'
                continue

            current_token = ""
            # if log or ln append full name token
            if c in wops.keys():
                if not can_prepend(tokens):
                    tokens.append('*')
                tokens.append(wops.get(c))
                continue

            # prepend 2 before blank root
            if c == '√' and can_prepend(tokens):
                tokens.append('2')
            tokens.append(c)

        elif c in "()":
            if current_token:
                tokens.append(current_token)
                current_token = ""

            if c == "(" and not can_prepend(tokens) and not log_exist_before(tokens):
                tokens.append('*')

            # insert 10 after blank log as base
            if c == "(" and log_last(tokens):
                tokens.append('10')

            if c == ")" and log_exist_before(tokens) and is_number(tokens[-1]):
                tokens.insert(-1, '10')

            tokens.append(c)
            current_token = ""
        else:
            # concat new number
            if tokens and tokens[-1] == ')':
                tokens.append('*')

            current_token += c

    if current_token:
        # insert 10 after blank log as base
        if log_last(tokens):
            tokens.append('10')
        if current_token[0] == '.':
            current_token = "0" + current_token
        tokens.append(current_token)
    return tokens


##
# @brief Convert infix expression to postfix
# @param expression: expression to convert
# @return: queue of operations
def shunting_yard(expression):
    tokens = tokenize(expression)
    operators = []
    queue = []

    for token in tokens:
        if token in OPS:
            while operators and operators[-1] != '(' \
                    and (PRECEDENCE[token] < PRECEDENCE[operators[-1]]
                         or PRECEDENCE[token] == PRECEDENCE[operators[-1]]):
                queue.append(operators.pop())
            operators.append(token)
        elif token == '(':
            operators.append(token)
        elif token == ')':
            while operators and operators[-1] != '(':
                queue.append(operators.pop())
            if not operators:
                raise SyntaxError("Unmatched opening bracket '(' found")
            operators.pop()
        else:
            if not is_number(token):
                raise SyntaxError(
                    f"Expected a number but received: '{token}'")

            queue.append(float(token))

    while operators:
        queue.append(operators.pop())
    return queue


##
# @brief Calculate expression
# @param expression: expression to calculate
# @return: result of expression
def calculate(expression):
    queue = shunting_yard(expression)
    stack = []
    for token in queue:
        if token in OPS:
            if not stack:
                raise SyntaxError("Insufficient operands for the operation")
            b = stack.pop()
            if not isinstance(b, float):
                raise SyntaxError(
                    f"Expected a number but received a value of type {type(b)}")
            if token not in "!ln":
                if not stack:
                    raise SyntaxError(
                        "Insufficient operands for the operation")
                a = stack.pop()
                if not isinstance(a, float):
                    raise SyntaxError(
                        f"Expected a number but received a value of type {type(a)}")
            if token == "+":
                result = mathlib.addition(a, b)
            elif token == "-":
                result = mathlib.subtraction(a, b)
            elif token == "*":
                result = mathlib.multiplication(a, b)
            elif token == "÷":
                result = mathlib.division(a, b)
            elif token == "^":
                result = mathlib.power(a, b)
            elif token == "%":
                result = mathlib.mod(a, b)
            elif token == "√":
                result = mathlib.root(a, b)
            elif token == "!":
                if b.is_integer():
                    b = int(b)
                result = mathlib.factorial(b)
            elif token == "log":
                result = mathlib.logarithm(b, a)
            elif token == "ln":
                result = mathlib.ln(b)
            if isinstance(result, complex):
                raise ValueError("Expected real number not 'complex'")
            try:
                stack.append(float(result))
            except OverflowError:
                raise ValueError("int too large to convert to float")
        else:
            stack.append(token)

    if not stack:
        return 0
    return stack[0]
