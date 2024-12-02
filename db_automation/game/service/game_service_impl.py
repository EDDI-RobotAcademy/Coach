from django.forms import model_to_dict

from dice.repository.dice_repository_impl import DiceRepositoryImpl
from game.repository.game_repository import GameRepository
from game.service.game_service import GameServiceRepository
from game.repository.game_repository_impl import GameRepositoryImpl

class GameServiceRepositoryImpl(GameServiceRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__gameRepository = GameRepositoryImpl.getInstance()
            cls.__instance.__diceRepository=DiceRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def gameStart(self):
        start = input("주사위를 굴리시겠습니까?")
        if start=="yes":
            for i in range(2):
                self.__diceRepository.rollDice()
        else:
            print("게임을 종료합니다.")


    def sumDiceFirst(self):
        sumDice1,sumDice2=0
        for id in range(1,5):
            if 0<id<=2:
                sumDice1+=self.__diceRepository.findById(id)
                return sumDice1

            elif 3<=id<5:
                sumDice2+=self.__diceRepository.findById(id)
                return sumDice2
