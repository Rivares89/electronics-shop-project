"""Здесь надо написать тесты с использованием pytest для модуля item."""
import csv

import pytest

from src.item import Item, InstantiateCSVError
from src.phone import Phone

def test_Item():
    item1 = Item("Телевизор", 5, 2)
    assert item1.name == "Телевизор"
    assert item1.price == 5
    assert item1.quantity == 2
    item1.name = "телек"
    assert item1.name == "телек"
    assert Item.pay_rate == 0.5

def test_calculate_total_price():
    item1 = Item("Телевизор", 5, 2)
    assert item1.calculate_total_price() == 10

def test_apply_discount():
    item1 = Item("Телевизор", 6, 2)
    item1.apply_discount()
    assert item1.price == 3

def test_instantiate_from_csv():
    Item.instantiate_from_csv('/items.csv')
    item1 = Item.all[1]
    assert item1.name == "Ноутбук"
    assert item1.price == '1000'
    assert item1.quantity == '3'

def test_string_to_number():
    assert Item.string_to_number('2.3') == 2
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == "Item(Смартфон, 10000, 20)"
    assert str(item1) == 'Смартфон'

def test_repr():
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == "Item(Смартфон, 10000, 20)"

def test_str():
    item1 = Item("Смартфон", 10000, 20)
    assert str(item1) == 'Смартфон'

def test_add():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    item1 = Item("Смартфон", 10000, 20)
    assert item1 + phone1 == 25

def test_instantiate_from_csv():
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv('../sr/items.csv')