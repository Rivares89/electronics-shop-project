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
        def get_name(self):
            '''геттер для name'''
            return self.__name

        @get_name.setter
        def setter_name(self, __name):
            if len(__name) <= 10:
                return __name
            else:
                return __name[:10]




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
        self.price = self.price * self.pay_rate
        return self.price


    # csv_file = 'src/item.csv'
    @classmethod
    def instantiate_from_csv(cls, csv_file):
        items = []
        with open(csv_file, mode='r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)
            for row in csv_reader:
                name, price, quantity = row
                item = cls(name, float(price), int(quantity))
                items.append(item)
        return items