from src.phone import Phone
from src.item import Item

def test_Phone():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert phone1.name == "iPhone 14"
    assert phone1.price == 120_000
    assert phone1.quantity == 5
    assert phone1.number_of_sim == 2
    assert str(phone1) == 'iPhone 14'
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"

def test_add():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    item1 = Item("Смартфон", 10000, 20)
    assert item1 + phone1 == 25