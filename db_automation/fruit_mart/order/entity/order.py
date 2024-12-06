from django.db import models
#from fruit_mart.customer.entity.cumstomer import Customer
from fruit_mart.mart.entity.mart import Mart

class Order(models.Model):
    id=models.AutoField(primary_key=True) #계속 증가하는 id생성
    customerNickName = models.CharField(max_length=225)
    # 소비자 이름 입력받기
    buyNumber=models.IntegerField()
    #구매갯수 입력받기
    fruitType= models.CharField(max_length=50, unique=True)
    # 구매할 과일종류 입력받기

    def __str__(self):
        return f"소비자:{self.customerNickName},구매과일:{self.fruitType},구매갯수:{self.buyNumber}"


    def getId(self):
        return self.id

    def getNumber(self):
        return self.buyNumber

    def getCustomer(self):
        return self.customerNickName

    def getFruit(self):
        return self.fruitType

    class Meta:
        db_table="Order"


