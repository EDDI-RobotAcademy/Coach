from dice_game.player.entity.player import Player
from dice_game.player.repository.player_repository import PlayerRepository

class PlayerRepositoryImpl(PlayerRepository):
    __instance = None

    def __new__(cls):
        #진짜 생성자 생성
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance
    #싱글톤 생성


    def createPlayer(self):
        player1 = Player(name='player1')
        player2 = Player(name='player2')
        players=Player.objects.all()
        return players

    #플레이어 Id찾기
    def findById(self, id):
        return Player.objects.get(id=id)