from abc import ABC, abstractmethod

class GameRepository(ABC):

    @abstractmethod
    def sumDice(self):
        pass
    @abstractmethod
    def create(self, gameCount):
        pass