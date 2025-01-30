##
# @file test_mathlib.py
# @brief Tests for mathlib (IVS Project 2)
# @author Václav Paťorek (xpator00)
# @date April 2023

import mathlib
import pytest

# ADDITION


def test_addition_positive_number_and_positive_number():
    assert mathlib.addition(2, 7) == 9


def test_addition_positive_number_and_negative_number():
    assert mathlib.addition(4, -6) == -2


def test_addition_negative_number_and_positive_number():
    assert mathlib.addition(-5, 4) == -1


def test_addition_negative_number_and_negative_number():
    assert mathlib.addition(-1, -3) == -4

# SUBTRACTION


def test_subtraction_positive_number_and_positive_number():
    assert mathlib.subtraction(5, 1) == 4


def test_subtraction_positive_number_and_negative_number():
    assert mathlib.subtraction(7, -2) == 9


def test_subtraction_negative_number_and_positive_number():
    assert mathlib.subtraction(-1, 4) == -5


def test_subtraction_negative_number_and_negative_number():
    assert mathlib.subtraction(-4, -2) == -2

# MULTIPLICATION


def test_multiplication_positive_number_and_positive_number():
    assert mathlib.multiplication(3, 1) == 3


def test_multiplication_positive_number_and_negative_number():
    assert mathlib.multiplication(4, -2) == -8


def test_multiplication_negative_number_and_positive_number():
    assert mathlib. multiplication(-1, 5) == -5


def test_multiplication_negative_number_and_negative_number():
    assert mathlib.multiplication(-1, -4) == 4


def test_multiplication_zero_number_and_positive_number():
    assert mathlib.multiplication(0, 9) == 0


def test_multiplication_zero_number_and_negative_number():
    assert mathlib.multiplication(0, -3) == 0


def test_multiplication_positive_number_and_zero_number():
    assert mathlib.multiplication(7, 0) == 0


def test_multiplication_negative_number_and_zero_number():
    assert mathlib.multiplication(-3, 0) == 0

# DIVISION


def test_division_positive_number_and_positive_number():
    assert mathlib.division(8, 4) == 2


def test_division_positive_number_and_negative_number():
    assert mathlib.division(6, -3) == -2


def test_division_negative_number_and_positive_number():
    assert mathlib.division(-8, 1) == -8


def test_division_negative_number_and_negativ_number():
    assert mathlib.division(-6, -6) == 1


def test_division_zero_number_and_positive_number():
    assert mathlib.division(0, 4) == 0


def test_division_zero_number_and_negative_number():
    assert mathlib.division(0, -2) == 0


def test_division_positive_number_by_zero_number():
    with pytest.raises(ZeroDivisionError, match='DivisionPositiveNumberByZeroError'):
        mathlib.division(8, 0)


def test_division_negative_number_by_zero_number():
    with pytest.raises(ZeroDivisionError, match='DivisionNegativeNumberByZeroError'):
        mathlib.division(-4, 0)

# MODULO


def test_modulo_division_positive_number_and_positive_number():
    assert mathlib.mod(4, 2) == 0
    assert mathlib.mod(8, 5) == 3
    assert mathlib.mod(4, 7) == 4


def test_modulo_division_positive_number_and_negative_number():
    assert mathlib.mod(3, -1) == 0
    assert mathlib.mod(9, -2) == -1
    assert mathlib.mod(3, -6) == -3


def test_modulo_division_negative_number_and_positive_number():
    assert mathlib.mod(-8, 2) == 0
    assert mathlib.mod(-4, 3) == 2
    assert mathlib.mod(-4, 6) == 2


def test_modulo_division_negative_number_and_negative_number():
    assert mathlib.mod(-6, -3) == 0
    assert mathlib.mod(-8, -6) == -2
    assert mathlib.mod(-3, -7) == -3

# FACTORIAL


def test_factorial_positive_number():
    assert mathlib.factorial(5) == 120


def test_factorial_zero_number():
    assert mathlib.factorial(0) == 1


def test_factorial_negative_number():
    with pytest.raises(ValueError, match='FactorialOfNegativeNumberError'):
        mathlib.factorial(-5)


def test_factorial_decimal_positive_number():
    with pytest.raises(ValueError, match='FactorialOfDecimalPositiveNumberError'):
        mathlib.factorial(1.5)


def test_factorial_decimal_negative_number():
    with pytest.raises(ValueError, match='FactorialOfDecimalNegativeNumberError'):
        mathlib.factorial(-4.8)

# POWER


def test_power_positive_number_and_positive_number():
    assert mathlib.power(2, 2) == 4


def test_power_positive_number_and_negative_number():
    assert mathlib.power(2, -2) == 0.25


def test_power_negative_number_and_positive_number():
    assert mathlib.power(-2, 2) == 4


def test_power_negative_number_and_negative_number():
    assert mathlib.power(-2, -2) == 0.25


def test_power_positive_number_and_zero_number():
    assert mathlib.power(2, 0) == 1


def test_power_zero_number_and_positive_number():
    assert mathlib.power(0, 2) == 0


def test_power_negative_number_and_zero_number():
    assert mathlib.power(-2, 0) == 1


def test_power_zero_number_and_negative_number():
    with pytest.raises(ValueError, match='PowerZeroNumberAtNegativeNumberError'):
        mathlib.power(0, -2)

# ROOT


def test_root_positive_even_number_and_positive_even_number():
    assert mathlib.root(2, 4) == 2


def test_root_negative_even_number_and_positive_even_number():
    assert mathlib.root(-2, 4) == 0.5


def test_root_positive_even_number_and_negative_even_number():
    with pytest.raises(ValueError, match='RootPositiveEvenNumberOfNegativeEvenNumberError'):
        mathlib.root(2, -4)


def test_root_negative_even_number_and_negative_even_number():
    with pytest.raises(ValueError, match='RootNegativeEvenNumberOfNegativeEvenNumberError'):
        mathlib.root(-2, -4)


def test_root_positive_even_number_and_zero_number():
    assert mathlib.root(2, 0) == 0


def test_root_negative_even_number_and_zero_number():
    with pytest.raises(ValueError, match='RootNegativeEvenNumberOfZeroNumberError'):
        mathlib.root(-2, 0)


def test_root_zero_number_and_positive_even_number():
    with pytest.raises(ValueError, match='RootZeroNumberOfPositiveEvenNumberError'):
        mathlib.root(0, 2)


def test_root_zero_number_and_negative_even_number():
    with pytest.raises(ValueError, match='RootZeroNumberOfNegativeEvenNumberError'):
        mathlib.root(0, -2)


def test_root_positive_odd_number_and_positive_number():
    assert mathlib.root(3, 8) == 2


def test_root_negative_odd_number_and_positive_number():
    assert mathlib.root(-3, 8) == 0.5


def test_root_positive_odd_number_and_negative_number():
    assert mathlib.root(3, -8) == -2


def test_root_negative_odd_number_and_negative_number():
    assert mathlib.root(-3, -8) == -0.5


def test_root_positive_odd_number_and_zero_number():
    assert mathlib.root(3, 0) == 0


def test_root_negative_odd_number_and_zero_number():
    with pytest.raises(ValueError, match='RootNegativeOddNumberOfZeroNumberError'):
        mathlib.root(-3, 0)


def test_root_zero_number_and_positive_odd_number():
    with pytest.raises(ValueError, match='RootZeroNumberOfPositiveOddNumberError'):
        mathlib.root(0, 3)


def test_root_zero_number_and_negative_odd_number():
    with pytest.raises(ValueError, match='RootZeroNumberOfNegativeOddNumberError'):
        mathlib.root(0, -3)


def test_root_zero_number_and_zero_number():
    with pytest.raises(ValueError, match='RootZeroNumberOfZeroNumberError'):
        mathlib.root(0, 0)

# LOGARITHM


def test_logarithm_positive_number_and_positive_number_base():
    assert mathlib.logarithm(2, 4) == 0.5


def test_logarithm_positive_number_and_negative_number_base():
    with pytest.raises(ValueError, match='LogarithmPositiveNumberAndNegativeNumberBaseError'):
        mathlib.logarithm(2, -4)


def test_logarithm_negative_number_and_positive_number_base():
    with pytest.raises(ValueError, match='LogarithmNegativeNumberAndPositiveNumberBaseError'):
        mathlib.logarithm(-2, 4)


def test_logarithm_negative_number_and_negative_number_base():
    with pytest.raises(ValueError, match='LogarithmNegativeNumberAndNegativeNumberBaseError'):
        mathlib.logarithm(-2, -4)


def test_logarithm_zero_number_and_positive_number_base():
    with pytest.raises(ValueError, match='LogarithmZeroNumberAndPositiveNumberBaseError'):
        mathlib.logarithm(0, 2)


def test_logarithm_positive_number_and_zero_number_base():
    with pytest.raises(ValueError, match='LogarithmPositiveNumberAndZeroNumberBaseError'):
        mathlib.logarithm(2, 0)


def test_logarithm_zero_number_and_negative_number_base():
    with pytest.raises(ValueError, match='LogarithmZeroNumberAndNegativeNumberBaseError'):
        mathlib.logarithm(0, -2)


def test_logarithm_negative_number_and_zero_number_base():
    with pytest.raises(ValueError, match='LogarithmNegativeNumberAndZeroNumberBaseError'):
        mathlib.logarithm(-2, 0)


def test_logarithm_zero_number_and_zero_number_base():
    with pytest.raises(ValueError, match='LogarithmZeroNumberAndZeroNumberBaseError'):
        mathlib.logarithm(0, 0)

#NATURAL LOGARITHM


def test_natural_logarithm_positive_number():
    assert mathlib.ln(1) == 0
    

def test_natural_logarithm():
    with pytest.raises(ValueError, match='NaturalLogarithmZeroNumberError'):
        mathlib.ln(0)


def test_natural_logarithm_negative_number():
    with pytest.raises(ValueError, match='NaturalLogarithmNegativeNumberError'):
        mathlib.ln(-1)
