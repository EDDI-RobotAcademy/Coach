from abc import ABC, abstractmethod

class GameServiceRepository(ABC):

    @abstractmethod
    def sumDiceFirst(self):
        pass