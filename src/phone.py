from src.item import Item


class Phone(Item):
    """Класс для представления товара в магазине, тип мобильный телефон"""
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    def __repr__(self):
        """Возвращает: имя класса('имя экземпляра', цена экземпляра, количество экземпляра, кол-ва сим карт"""
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    @property
    def number_of_sim(self):
        """number_of_sim геттер"""
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, value: int):
        """number_of_sim сеттер
        value - int, больше нуля"""
        if value < 1:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')
        else:
            self.__number_of_sim = value
