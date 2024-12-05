from abc import ABC, abstractmethod


class OrderRepository(ABC):
    @abstractmethod
    def findById(self, id):
        pass

    @abstractmethod
    def findByFruit(self, fruit):
        pass

    @abstractmethod
    def findByNumber(self, number):
        pass

    @abstractmethod
    def findByCustomer(self, customer):
        pass

    @abstractmethod
    def create(self, customer, fruit, number):
        pass

    @abstractmethod
    def findAll(self):
        pass