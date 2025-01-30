##
# @file mathlib.py
# @brief Math Library for IVS Project 2
# @author Peter Balážec (xbalaz12)
# @date April 2023

##
# @brief Addition function
# @param num1 first number to add
# @param num2 second number to add
# @return Sum of two numbers
def addition(num1, num2):
    res = num1 + num2
    return res


##
# @brief Subtraction function
# @param num1 first number to subtract
# @param num2 second number to subtract
# @return Difference of two numbers
def subtraction(num1, num2):
    res = num1 - num2
    return res


##
# @brief Multiplication function
# @param num1 first number to multiply
# @param num2 second number to multiply
# @return Product of the two numbers
def multiplication(num1, num2):
    res = num1 * num2
    return res


##
# @brief Division function
# @param num1 first number that we want to be divided
# @param num2 second number that the first number should be divided by
# @return Quotient of the two numbers
def division(num1, num2):
    if num1 >= 0 and num2 == 0:
        raise ZeroDivisionError('DivisionPositiveNumberByZeroError')
    elif num1 < 0 and num2 == 0:
        raise ZeroDivisionError('DivisionNegativeNumberByZeroError')
    else:
        res = num1 / num2
        return res


##
# @brief Mod function
# @param num1 first number that we want to be divided
# @param num2 second number that the first number should be divided by
# @return Remainder after divison
def mod(num1, num2):
    res = num1 % num2
    return res


##
# @brief Factorial function
# @param num1 number we want to use factorial on
# @return Factorial of a number
def factorial(num1):
    res = 1
    if type(num1) is float and num1 > 0:
        raise ValueError('FactorialOfDecimalPositiveNumberError')
    elif num1 < 0 and type(num1) is int:
        raise ValueError('FactorialOfNegativeNumberError')
    elif type(num1) is float and num1 < 0:
        raise ValueError('FactorialOfDecimalNegativeNumberError')
    for i in range(1, num1+1):
        res = res * i
    return res


##
# @brief Power function
# @param num1 number we want to use the power on
# @param power power of a number
# @return Result of one number to the nth power
def power(num1, power):
    if num1 == 0 and power < 0:
        raise ValueError('PowerZeroNumberAtNegativeNumberError')
    else:
        res = num1 ** power
        return res


##
# @brief Root function
# @param num1 number under the root
# @param num2 nth root of a number
# @return Sum of the two numbers
def root(num2, num1):
    if num2 > 0 and (mod(num2, 2) == 0) and num1 < 0 and (mod(num1, 2) == 0):
        raise ValueError('RootPositiveEvenNumberOfNegativeEvenNumberError')
    elif num2 == 0 and num1 == 0:
        raise ValueError('RootZeroNumberOfZeroNumberError')
    elif num2 < 0 and (mod(num2, 2) == 0) and num1 < 0 and (mod(num1, 2) == 0):
        raise ValueError('RootNegativeEvenNumberOfNegativeEvenNumberError')
    elif num2 < 0 and (mod(num2, 2) == 0) and num1 == 0:
        raise ValueError('RootNegativeEvenNumberOfZeroNumberError')
    elif num2 == 0 and num1 > 0 and (mod(num1, 2) == 0):
        raise ValueError('RootZeroNumberOfPositiveEvenNumberError')
    elif num2 == 0 and num1 < 1 and (mod(num1, 2) == 0):
        raise ValueError('RootZeroNumberOfNegativeEvenNumberError')
    elif num2 < 0 and (mod(num2, 2) == 1) and num1 == 0:
        raise ValueError('RootNegativeOddNumberOfZeroNumberError')
    elif num2 == 0 and num1 > 0 and (mod(num1, 2) == 1):
        raise ValueError('RootZeroNumberOfPositiveOddNumberError')
    elif num2 == 0 and num1 < 0 and (mod(num1, 2) == 1):
        raise ValueError('RootZeroNumberOfNegativeOddNumberError')
    else:
        if (mod(num2, 2) == 1) and num1 < 0:
            res = (abs(num1) ** (1/num2))
            res = res * (-1)
        else:
            res = num1 ** (1/num2)
        return res


##
# @brief Natural logarithm function using Taylor series expansion
# @param num1 number of which we want to calculate natural logarithm
# @return Result of calculating natural logarithm
def ln(num1):
    if num1 == 0:
        raise ValueError('NaturalLogarithmZeroNumberError')
    elif num1 < 0:
        raise ValueError('NaturalLogarithmNegativeNumberError')
    num_of_terms = 100000
    res = 0
    tmp = (num1 - 1) / (num1 + 1)
    for i in range(1, num_of_terms, 2):
        res += (tmp ** i) / i
    return 2 * res


##
# @brief Logarithm function using natural logarithms
# @param num1 number of which we want to calculate logarithm
# @param base base of a logarithm
# @return Result of calculating logarithm
def logarithm(num1, base):
    if num1 > 0 and base < 0:
        raise ValueError('LogarithmPositiveNumberAndNegativeNumberBaseError')
    elif num1 == 0 and base == 0:
        raise ValueError('LogarithmZeroNumberAndZeroNumberBaseError')
    elif num1 < 0 and base > 0:
        raise ValueError('LogarithmNegativeNumberAndPositiveNumberBaseError')
    elif num1 < 0 and base < 0:
        raise ValueError('LogarithmNegativeNumberAndNegativeNumberBaseError')
    elif num1 == 0 and base > 0:
        raise ValueError('LogarithmZeroNumberAndPositiveNumberBaseError')
    elif num1 > 0 and base == 0:
        raise ValueError('LogarithmPositiveNumberAndZeroNumberBaseError')
    elif num1 == 0 and base < 0:
        raise ValueError('LogarithmZeroNumberAndNegativeNumberBaseError')
    elif num1 < 1 and base == 0:
        raise ValueError('LogarithmNegativeNumberAndZeroNumberBaseError')
    elif num1 == 1 and base != 0:
        res = 0
        return res
    else:
        res = round(ln(num1) / ln(base), 8)
        return res
