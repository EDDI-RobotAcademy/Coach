import random


class Player:
    def __init__(self, name):
        self.name = name
        self.dice_rolls = []
        self.total_score = 0

    # 주사위 굴리기
    def roll_dice(self):
        self.dice_rolls = [random.randint(1, 6), random.randint(1, 6)]
        self.total_score = sum(self.dice_rolls)

    def __str__(self):
        return f"{self.name} - 주사위: {self.dice_rolls}, 합계: {self.total_score}"