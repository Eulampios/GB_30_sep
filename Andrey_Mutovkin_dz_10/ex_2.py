from abc import ABC, abstractmethod, abstractproperty


class Clothes(ABC):
    @abstractmethod
    def __init__(self, param: int):
        pass

    @abstractproperty
    def fabric_amount(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


class Coat(Clothes):
    def __init__(self, size: int):
        self.__size = size

    @property
    def fabric_amount(self):
        return self.__size / 6.5 + 0.5

    def __str__(self):
        return f"На пальто размера {self.__size} потребуется ткани: {self.fabric_amount:.2f}"


class Suit(Clothes):
    def __init__(self, height: int):
        self.__height = height

    @property
    def fabric_amount(self):
        return self.__height * 2 + 0.3

    def __str__(self):
        return f"На костюм ростом {self.__height} потребуется ткани: {self.fabric_amount:.2f}"


print(
    Coat(24),
    Suit(12),
    sep='\n'
)
