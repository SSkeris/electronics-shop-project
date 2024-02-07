"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item

test_item = Item("apple", 50000, 10)


def test_Item_init():
    """Тест функции __init__ для класса Item"""
    assert test_item.name == 'apple'
    assert test_item.price == 50000
    assert test_item.quantity == 10


def test_Item_calculate_total_price():
    """Тест функции calculate_total_price для класса Item"""
    assert test_item.calculate_total_price() == 500000


def test_Item_apply_discount():
    """Тест функции apply_discount для класса Item"""
    Item.pay_rate = 0.5
    test_item.apply_discount()
    assert test_item.price == 25000


def test_name():
    Item.instantiate_from_csv()
    item1 = Item.all[0]
    assert item1.name == 'Смартфон'


def test__repr__str__():
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"
    assert str(item1) == 'Смартфон'


def test__add__():
    assert test_item + test_item == 20
    # assert test_item + 10 != 20
