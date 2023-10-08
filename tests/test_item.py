"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import calculate_total_price

def test_calculate_total_price():
    assert calculate_total_price(10000, 20) == 200000

def test_apply_discount():
    assert apply_discount(10000, 0.8) == 8000.0