from abc import ABC, abstractmethod


class OrderService(ABC):

    @abstractmethod
    def buyFruit(self, customer, fruit, number):
        pass

    @abstractmethod
    def findAllBuy(self):
        pass

