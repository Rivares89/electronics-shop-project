from src.item import Item
from src.phone import Phone, Tv

if __name__ == '__main__':

    # смартфон iPhone 14, цена 120_000, количество товара 5, симкарт 2
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert str(phone1) == 'iPhone 14'
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"
    # print(type(phone1.quantity))
    # print(type(phone1.number_of_sim))
    assert phone1._number_of_sim == 2

    item1 = Item("Смартфон", 10000, 20)
    assert item1 + phone1 == 25
    assert phone1 + phone1 == 10

    tv1 = Tv("Самсунг", 7)
    assert phone1 + tv1 == 12

    phone1.number_of_sim = 0
    # ValueError: Количество физических SIM-карт должно быть целым числом больше нуля.
