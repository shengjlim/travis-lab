import pytest
from hello import add_numbers, subtract_numbers

def test_addition():
    assert add_numbers(1,1) == 2

def test_subtraction():
    assert subtract_numbers(2,1) == 1