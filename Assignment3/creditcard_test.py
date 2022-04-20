""" 
Skeleton test file for credit card program
"""
from Assignment3.creditcard_part1 import sum_digits
import pytest

import creditcard_part1 
import creditcard

## creditcard_part1

def test_last_digit():
    assert type(creditcard_part1.last_digit(123)) == int
    assert creditcard_part1.last_digit(123) == 3

def test_decimal_right_shift():
    assert type(creditcard_part1.decimal_right_shift(123)) == int
    assert creditcard_part1.decimal_right_shift(456) == 45

def test_sum_digits():
    pass

## creditcard

def test_verify():
    pass

def test_generate():
    pass
