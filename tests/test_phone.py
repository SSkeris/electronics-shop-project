import pytest
from _pytest.fixtures import fixture

from src.phone import Phone

test_phone = Phone("iPhone 14", 120_000, 5, 2)
test_phone2 = Phone("iPhone 13", 80_000, 3, 2)


def test_case1():
    """Тест класса Phone"""
    test_phone.number_of_sim = 1
    assert test_phone.number_of_sim == 1
    assert test_phone.name == "iPhone 14"
    assert test_phone.quantity == 5


def test_case2():
    """Тест класса Phone"""
    assert repr(test_phone2) == "Phone('iPhone 13', 80000, 3, 2)"
