##
# @file test_calculate.py
# @brief Tests for calculate function
# @author Radim Mifka (xmifka00)
# @date April 2023

import pytest

from calculator import calculate
from exceptions.syntax import SyntaxError


def test_calculate_base():
    assert calculate("") == 0.0
    assert calculate("1") == 1.0
    assert calculate("1534") == 1534.0
    assert calculate("-1534") == -1534.0
    assert calculate("1.5") == 1.5
    assert calculate("-1.5") == -1.5
    assert calculate("(4)") == 4.0
    assert calculate("(400)") == 400.0
    with pytest.raises(ValueError, match='int too large to convert to float'):
        calculate("400!")
    assert calculate(".5") == 0.5


def test_calculate_syntax():
    with pytest.raises(SyntaxError, match='Insufficient operands for the operation'):
        calculate("--1")
        calculate("+-1")
        calculate("+-*1")
        calculate("+-*")
        calculate("+-*")


def test_calculate_addition():
    with pytest.raises(ValueError, match='int too large to convert to float'):
        calculate("400!+2!")
    assert calculate("1+2+3") == 6.0
    assert calculate(
        "1+2+3+4+5+6+7") == 28.0
    assert calculate(
        "1223+2414+3135+4090+52313+6123+7123123") == 7192421.0
    assert calculate("1+2") == 3
    assert calculate("1013+2231") == 3244
    assert calculate("10.13+22.31") == 32.44
    pytest.approx(calculate(
        "10.13+22.31+11.3"), 43.74)
    assert calculate(".5 + .3") == 0.8


def test_calculate_substraction():
    assert calculate("1-2-3") == -4.0
    assert calculate(
        "1-2-3-4-5-6-7") == -26.0
    assert calculate(
        "1223-2414-3135-4090-52313-6123-7123123") == -7189975.0

    assert calculate("1-2") == -1
    assert calculate("1013-2231") == -1218.0
    assert calculate("-1013-2231") == -3244.0
    assert calculate(
        "-1013-(-2231)") == 1218.0
    pytest.approx(calculate("10.13-22.31"), -12.18)


def test_calculate_multiplication():
    assert calculate("4(423)") == 1692.0
    assert calculate("4.1(4.2)") == 17.22
    assert calculate("4(42)(41)") == 6888.0

    assert calculate("(4)4") == 16.0
    assert calculate("(4)(4)") == 16.0
    assert calculate("1*2*3") == 6.0
    assert calculate(
        "1*2*3*4*5*6*7") == 5040.0
    assert calculate(
        "1223*2414*3135*4090*52313*6123*7123123") == 86371190423690217516247877100.0
    assert calculate("1*2") == 2.0
    assert calculate("1013*2231") == 2260003.0
    assert calculate("10.13*22.31") == 226.0003
    pytest.approx(calculate(
        "10.13*22.31*11.3"), 2553.80339)

    assert calculate(
        "(3+4)*(5-6)") == -7.0
    assert calculate("(2+3)(4-5)(6+7)") == -65.0
    assert calculate("(8+9)(10-11)(12+13)(14-15)") == 425.0
    assert calculate("2(3(4(5(6))))") == 720.0
    assert calculate("(1+2)(3+4)(5+6)(7+8)(9+10)") == 65835


def test_calculate_log():
    assert calculate("log3") == 0.47712125
    assert calculate("log2(10)") == 3.32192809
    assert calculate("log400ln20") == 7.795075089766572
    assert calculate("ln400ln20") == 17.948823709625746
    assert calculate("log(100)") == 2.0
    assert calculate("log10+log20") == 2.30103
    assert calculate("ln(100)") == 4.6051701859880785
    assert calculate("ln2+ln3") == 1.791759469228054
    assert calculate("3(log3)") == 1.43136375
    assert calculate("3log3") == 1.43136375

    with pytest.raises(ValueError, match="LogarithmPositiveNumberAndNegativeNumberBaseError"):
        calculate("log-2(10)")
    with pytest.raises(ValueError, match="LogarithmNegativeNumberAndPositiveNumberBaseError"):
        calculate("log2(-10)")
    with pytest.raises(ValueError, match="LogarithmNegativeNumberAndNegativeNumberBaseError"):
        calculate("log-2(-10)")
    with pytest.raises(ValueError, match="LogarithmZeroNumberAndPositiveNumberBaseError"):
        calculate("log2(0)")
    with pytest.raises(ValueError, match="LogarithmZeroNumberAndNegativeNumberBaseError"):
        calculate("log-2(0)")
    with pytest.raises(ValueError, match="LogarithmPositiveNumberAndZeroNumberBaseError"):
        calculate("log0(2)")
    with pytest.raises(ValueError, match="LogarithmNegativeNumberAndZeroNumberBaseError"):
        calculate("log0(-2)")
    with pytest.raises(ValueError, match="LogarithmZeroNumberAndZeroNumberBaseError"):
        calculate("log0(0)")


def test_calculate_mod():
    assert calculate("3%2") == 1.0
    assert calculate("27%5") == 2.0
    assert calculate("1000%25") == 0.0
    assert calculate(
        "10+15%3-27%5") == 8.0


def test_calculate_exponents():
    assert calculate("2^3") == 8.0
    assert calculate("-2^3") == -8.0
    assert calculate("2^-3") == 0.125
    assert calculate("-2^-3") == -0.125
    assert calculate("2.5^3.5") == 24.705294220065465
    assert calculate("2^3^4") == 4096.0
    with pytest.raises(ValueError, match="PowerZeroNumberAtNegativeNumberError"):
        calculate("0^-3")


def test_calculate_root():
    assert calculate("2√3") == 1.7320508075688772
    assert calculate("√3") == 1.7320508075688772
    assert calculate("(-2)√3") == 0.5773502691896257
    assert calculate("2-3*2+√3") == -2.267949192431123
    assert calculate("3√-3") == -1.4422495703074083
    assert calculate("-2√3") == 0.5773502691896257
    assert calculate("2.5√3.5") == 1.6505444239489884
    assert calculate("2√3√4") == 2.226381056397932
    assert calculate("2√(2+2)") == 2.0
    assert calculate("3√(5+2√3)") == 1.8882049348324292
    assert calculate("(√5+2)√(3+√2)") == 1.4198067087659296
    assert calculate("(√2+√3)√(3-√2)") == 1.157831134097481
    assert calculate("2√(8-2√7)") == 2.3139249531770494
    assert calculate("(√3+√2)√(5-√6)") == 1.3466081207529963
    assert calculate("2√(2+3√2)√(3-2√2)") == 1.29094168471842
    assert calculate("(√2+√3)√(3-√2)+4√(2+√3)") == 2.5477417976216286

    # Even of negative odd
    with pytest.raises(ValueError, match="Expected real number not 'complex'"):
        # Even of negative odd
        calculate("2√-3")
        # Even of negative even
        calculate("2√-4")
        # Negative even of negative odd
        calculate("-2√-3")
        # Negative even of negative even
        calculate("-2√-4")
        # 0 of 0
        calculate("0√0")
        # 0 of negative even
        calculate("0√-2")
        # 0 of negative odd
        calculate("0√-3")
        # 0 of even
        calculate("0√2")
        # 0 of odd
        calculate("0√3")


def test_calculate_brackets():
    assert calculate("(1+2)") == 3.0
    assert calculate(
        "((1+2))") == 3.0
    assert calculate(
        "((1+2)*(3+4))") == 21.0


def test_calculate_division():
    assert calculate("4÷2") == 2.0
    assert calculate("10.13÷22.31") == 0.4540564769161812
    assert calculate("10.13÷22.31÷11.3") == 0.04018198910762665
    assert calculate("10.13÷(22.31÷11.3)") == 5.130838189152847
    assert calculate("(10.13÷22.31)÷11.3") == 0.04018198910762665
    assert calculate("10.13÷-22.31") == -0.4540564769161812

    with pytest.raises(ZeroDivisionError, match='DivisionPositiveNumberByZeroError'):
        calculate("3÷0")

    with pytest.raises(ZeroDivisionError, match='DivisionNegativeNumberByZeroError'):
        calculate("-3÷0")


def test_calculate_multiple_operators():
    assert calculate("10.13***22.31") == 226.0003
    assert calculate("10.13+++22.31") == 32.44
    assert calculate("10.13+++22.31****23") == 523.26
    assert calculate("10.13÷÷÷÷÷÷22.31") == 0.4540564769161812


def test_calculate_factorial():
    assert calculate("5!") == 120
    assert calculate("5!+4!") == 144
    with pytest.raises(ValueError, match="FactorialOfDecimalPositiveNumberError"):
        calculate("1.5!")
    with pytest.raises(ValueError, match="FactorialOfNegativeNumberError"):
        calculate("-4!")
    with pytest.raises(ValueError, match="FactorialOfDecimalNegativeNumberError"):
        calculate("-4.1!")


def test_calculate_complex():
    assert calculate("1+2*3-4%2") == 7.0
    assert calculate("2^3%3") == 2.0
    assert calculate("log10+2*(3-4)+(10%3)") == 0.0
    assert calculate("2^3^2") == 64.0
    assert calculate("log3(10)2+3*3") == 13.19180654
    assert calculate("13(2)-3(5)log2(3)") == 2.2255624999999988
    assert calculate("13(2)(-3)(5)log2(3)") == -618.1353750000001
