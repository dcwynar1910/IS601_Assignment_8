from app.operations import add, subtract, multiply, divide, power, root, modulus
import pytest


def test_addition_positive():
    assert add(55, 3) == 58
    assert add(0, 0) == 0


def test_addition_negative():
    assert add(-5, -3) == -8
    assert add(-1, -1) == -2


def test_subtraction_positive():
    assert subtract(5, 1) == 4
    assert subtract(2, 0) == 2


def test_subtraction_negative():
    assert subtract(-5, -3) == -2
    assert subtract(3, 7) == -4


def test_multiplication_positive():
    assert multiply(2, 8) == 16
    assert multiply(0, 1) == 0


def test_multiplication_negative():
    assert multiply(2, -9) == -18
    assert multiply(-2, -2) == 4


def test_division_positive():
    assert divide(6, 2) == 3
    assert divide(-6, -2) == 3


def test_division_negative():
    assert divide(20, -10) == -2
    assert divide(-20, 10) == -2


def test_division_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero!"):
        divide(57, 0)

def test_power():
    assert power(5, 2) == 25
    assert power(10, 2) == 100

def test_root():
    assert root(9, 2) == 3
    assert root(81, 2) == 9

def test_modulus():
    assert modulus(37, 5) == 2
    assert modulus(5, 2) == 1

def test_root_by_negative():
    with pytest.raises(ValueError, match="Root of negative number is not allowed!"):
        root(-5, 2)

def test_root_by_zero():
    with pytest.raises(ValueError, match="Degree of zero is not allowed!"):
        root(5, 0)

def test_power_by_zero():
    with pytest.raises(ValueError, match="Negative power is not allowed!"):
        power(5, -20)

def test_modulus_by_zero():
    with pytest.raises(ValueError, match="Modulus by zero is not allowed!"):
        modulus(74, 0)
