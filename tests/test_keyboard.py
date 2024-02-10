import pytest

from src.keyboard import Keyboard

test_kb = Keyboard('KB-90Bk', 10000, 3)


def test_case1():
    """Тест класса Keyboard"""
    assert test_kb.name == 'KB-90Bk'
    assert test_kb.quantity == 3
    assert test_kb.language == "EN"
    test_kb.change_lang()
    assert str(test_kb.language) == "RU"
    test_kb.change_lang()
    assert test_kb.language == "EN"
