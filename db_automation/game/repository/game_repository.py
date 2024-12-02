from abc import ABC, abstractmethod

class GameRepository(ABC):

    @abstractmethod
    def sumDice(self):
        pass