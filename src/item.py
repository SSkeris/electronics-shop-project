import csv
from pathlib import Path


class Item:
    """Класс для представления товара в магазине."""
    pay_rate = 1.0
    all = []
    DATA_DIR = Path(__file__).parent.joinpath('items.csv')

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
        self.all.append(self)

    def __repr__(self):
        """Возвращает: имя класса('имя экземпляра', цена экземпляра, количество экземпляра"""
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        """Возвращает: имя экземпляра"""
        return f'{self.__name}'

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.
        :return: Общая стоимость товара.
        """
        return self.quantity * self.price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate

    @property
    def name(self) -> str:
        """
        name геттер
        """
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        """
        name сеттер
        value - новое имя, не длиннее 10 символов
        """
        self.__name = value[:10]

    @classmethod
    def instantiate_from_csv(cls):
        """класс-метод, инициализирующий экземпляры класса
        `Item` данными из файла _../src/items.csv_"""
        with cls.DATA_DIR.open(newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            cls.all.clear()
            for row in reader:
                # print(row['name'], row['price'], row['quantity'])
                name = row['name']
                price = row['price']
                quantity = row['quantity']
                cls(name, price, quantity)
            return cls

    @staticmethod
    def string_to_number(param: str) -> int:
        """Метод, возвращающий число из числа-строки"""
        return int(float(param))
