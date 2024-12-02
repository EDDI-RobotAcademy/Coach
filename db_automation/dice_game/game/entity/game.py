from django.db import models

class Game(models.Model):

    def __str__(self):
        return f"주사위 id:{self.id},합:{self.number}"

    def getId(self):
        return self.id

    def getNumber(self):
        return self.number

    class Meta:
        db_table="dice"