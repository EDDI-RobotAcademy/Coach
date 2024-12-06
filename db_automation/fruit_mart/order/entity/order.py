from django.db import models
#from fruit_mart.customer.entity.cumstomer import Customer
from fruit_mart.mart.entity.mart import Mart

class Order(models.Model):
    id=models.AutoField(primary_key=True) #계속 증가하는 id생성
    #customerNickName = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='customer')
    # Customer에서 customer와 order와 관련된것을 참조한다
    buyNumber=models.IntegerField()
    #정수를 저장
    fruitType= models.ForeignKey(Mart, on_delete=models.CASCADE, related_name='fruit_orders')
    # 구매할 Fruit에서 fruittype과 order가 관련된것을 참조한다
    fruitNumber= models.ForeignKey(Mart, on_delete=models.CASCADE, related_name='type_orders')
     # 구매할 Fruit에서 fruitNumber와 order와 관련된 것을 참조한다

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
        db_table="order"


