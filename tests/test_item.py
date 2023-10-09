"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item


@pytest.fixture
def item() -> Item:
    return Item(
        name='Тест',
        price=10000.0,
        quantity=3,
    )


def test_calculate_total_price(item):
    assert item.calculate_total_price() == 30000.0

def test_apply_discount(item):
    assert item.apply_discount() == 10000.0