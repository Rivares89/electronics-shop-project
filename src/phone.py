from src.item import Item


class Phone(Item):
    '''Дочерний класс класса  Item'''
    def __init__(self, name, price, quantity, number_of_sim: int):
        super().__init__(name, price, quantity)
        self._number_of_sim = number_of_sim

    def __str__(self):
        return f'{self.name}'

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self._number_of_sim})"

    def __add__(self, other):
        if not isinstance(other, Item):
            raise ValueError('Складывать можно только объекты Item и дочерние от них.')
        return self.quantity + other.quantity

    @property
    def number_of_sim(self):
        return f'{int(self._number_of_sim)}'

    @number_of_sim.setter
    def number_of_sim(self, value):
        if isinstance(value, int) and value != 0:
            self._number_of_sim = int(value)
        else:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')


class Tv:
    '''класс  Телевизоры'''
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

