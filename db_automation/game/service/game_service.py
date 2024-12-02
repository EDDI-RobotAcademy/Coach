from abc import ABC, abstractmethod

class GameServiceRepository(ABC):

    @abstractmethod
    def gameStart(self):
        pass

    @abstractmethod
    def sumDiceFirst(self):
        pass