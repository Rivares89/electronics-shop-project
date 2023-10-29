import csv
import inspect
import os.path

class InstantiateCSVError(Exception):
    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else 'Файл Item.csv поврежден'
        # self.messag = kwargs[0] if kwargs else 'Файл Item.csv поврежден'

    def __str__(self):
        return self.message
    pass
class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 0.5
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
        # Item.all.append(self)

    def __repr__(self):
        return f'{self.__class__.__name__}({self.__name}, {self.price}, {self.quantity})'

    def __str__(self):
        return f'{self.__name}'

    def __add__(self, other):
        if not isinstance(other, Item):
            raise ValueError('Складывать можно только объекты Item и дочерние от них.')
        return self.quantity + other.quantity

    @property
    def name(self):
        '''геттер для name'''
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name[:10]

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

    # csv_file = 'src/item.csv'
    @classmethod
    def instantiate_from_csv(cls, csv_file):
        cls.all = []
        class_file = inspect.getfile(cls)
        path_to_dir = os.path.dirname(class_file)
        temp_file = path_to_dir + csv_file
        with open(temp_file) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                item = (cls(row["name"], row["price"], row["quantity"]))
                cls.all.append(item)
        # return cls.all

    @staticmethod
    def string_to_number(str_number):
        if str_number.isdigit():
            return int(str_number)
        return float(str_number)// 1#

    @classmethod
    def instantiate_from_csv(cls, filename='../src/items.csv'):
        try:
            with open (filename, encoding='windows-1251') as csvfile:
                reader = csv.DictReader(csvfile)
                items = []
                for row in reader:
                    if (row['name'] == None) or (row['price'] == None) or (row['quantity'] == None):
                        raise InstantiateCSVError
                    else:
                        name = str(row['name'])
                        price = float(row["price"])
                        quantity = int(row["quantity"])
                        item = cls(name, price, quantity)
                        items.append(item)
                    cls.all = items
        except FileNotFoundError:
            raise FileNotFoundError("Отсутствует файл item.csv")
        except InstantiateCSVError:
            raise InstantiateCSVError('Файл item.csv поврежден')

