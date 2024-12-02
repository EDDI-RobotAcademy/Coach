from dice_game.game.repository.game_repository_impl import GameRepositoryImpl
from dice_game.dice.repository.dice_repository_impl import DiceRepositoryImpl
from dice_game.game.service.game_service_repository import GameServiceRepository


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

    def rollDice(self):
        for i in range(1,5):
            return self.__diceRepository.rollDice()

    def __sumDice(self):
        sumDice1,sumDice2=0
        sumDice1=self.__diceRepository.findById(1)+self.__diceRepository.findById(2)
        sumDice2=self.__diceRepository.findById(3)+self.__diceRepository.findById(4)

        if sumDice1>sumDice2:
            return sumDice1
        elif sumDice1<sumDice2:
            return sumDice2
        else:
            print("무승부 입니다.")

    def checkWinner(self):
        lastSumNumber=self.__sumDice()

        return lastSumNumber