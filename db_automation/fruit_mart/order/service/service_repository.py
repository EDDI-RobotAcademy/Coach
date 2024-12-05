from abc import ABC, abstractmethod


class OrderService(ABC):

    @abstractmethod
    def buyFruit(self, customerId, fruitId,numberId):
        pass

    @abstractmethod
    def findAllBuy(self):
        pass

