import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

        @property
        def name(self):
            '''геттер для name'''
            return self.__name

        @name.setter
        def name(self, name):
            if len(name) <= 10:
                return name
            else:
                return name[:10]

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate
        return self.price

    # csv_file = 'src/item.csv'
    @classmethod
    def instantiate_from_csv(cls, csv_file):
        items = []
        with open(csv_file, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                name, price, quantity = row
                item = cls(name, float(price), int(quantity))
                items.append(item)
        return items

    @staticmethod
    def string_to_number():
        self.price = int(self.price)
