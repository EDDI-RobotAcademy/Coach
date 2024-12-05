from fruit_mart.order.service.service_repository import OrderService
from fruit_mart.mart.repository.mart_repository_impl import MartRepositoryImpl
#from fruit_mart.커스터머임플 import 커스터머임플
from fruit_mart.order.repository.order_repository_impl import OrderRepositoryImpl

class OrderServiceImpl(OrderService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

            cls.__instance.__martRepository = MartRepositoryImpl()
            #cls.__instance.__customerRepository = 커스터임플.getInstance()
            cls.__instance.__orderRepository = OrderRepositoryImpl.getInstance()
        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def buyFruit(self, customerId, fruitId,numberId):
        fruit = self.__martRepository.find_by_fruit_name(fruitId)
        customer = self.__customerRepository.커스터머Id(customerId)
        buyNumber=self.__orderRepository.findById(numberId)
        return self.__orderRepository.create(customer, fruit,buyNumber)

    # def findFruit(self, requestFruitId):
    #     return self.__martRepository.findById(requestFruitId)

    def findAllBuy(self):
        return self.__orderRepository.findAll()