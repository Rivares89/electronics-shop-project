import pytest

from src.item import Item


@pytest.fixture
def item() -> Item:
    return Item(
        name='Тест',
        price=34500.4,
        quantity=10,
       )



