from django.forms import model_to_dict

from fruit_mart.order.entity.order import Order
from fruit_mart.order.repository.order_repository import OrderRepository


class OrderRepositoryImpl(OrderRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def create(self,customer,fruit,number):
        buyFruit=Order(customer,fruit,number)
        buyFruit.save()

        return Order.model_to_dict(buyFruit)

    def findAll(self):
        return Order.objects.all()


    def findById(self, id):
        return Order.objects.get(id=id)

    def findByFruit(self,fruit):
        return Order.objects.get(fruitType=fruit)

    def findByNumber(self,number):
        return Order.objects.get(buyNumber=number)

    def findByCustomer(self, customer):
        return Order.objects.get(customerNickName=customer)