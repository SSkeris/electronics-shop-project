from src.item import Item


class Keyboard(Item):
    """Класс для представления товара в магазине, тип клавиатура"""

    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        self._language = "EN"

    @property
    def language(self):
        return self._language

    def change_lang(self):
        """Меняет язык раскладки клавиатуры между RU и EN"""

        if self._language == "EN":
            self._language = "RU"
        elif self._language == "RU":
            self._language = "EN"
