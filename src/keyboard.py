from src.item import Item


class Keyboard(Item):
    """Класс для представления товара в магазине, тип клавиатура"""
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        self.language = "EN"

    def change_lang(self):
        """Меняет язык раскладки клавиатуры между RU и EN"""
        if self.language == "EN":
            self.language = "RU"
        elif self.language == "RU":
            self.language = "EN"
