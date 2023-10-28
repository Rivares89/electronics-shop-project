from src.item import Item


class MixinKeyboard():

    def __init__(self):
        self.__language = 'EN'
        
    def change_lang(self):
        if self.__language == 'EN':
            self.__language = 'RU'
        elif self.__language == 'RU':
            self.__language = 'EN'

    @property
    def language(self):
        '''геттер для name'''
        return self.__language

    @language.setter
    def language(self, new_language):
        if new_language not in {"RU", "EN"}:
            raise AttributeError("property 'language' of 'Keyboard' object has no setter")
        self.__language = new_language

    def __str__(self):
        return f'{self.language}'

class Keyboard(Item, MixinKeyboard):
    '''Дочерний класс клавиатура'''
    
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        MixinKeyboard.__init__(self)


    def __str__(self):
        return f'{self.name}'
    








