from django.db import models

class Dice(models.Model):
    for i in range(1,5):
        id=i
    number=models.IntegerField()

    def __str__(self):
        return f"주사위 id:{self.id},눈금:{self.number}"

    def getId(self):
        return self.id

    def getNumber(self):
        return self.number

    class Meta:
        db_table="dice"



