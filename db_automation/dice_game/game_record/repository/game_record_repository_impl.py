from dice_game.game_record.repository import gameRecordRepository
from dice_game.game_record.entity.game_record_entity import GameRecord

class gameRecordRepositoryImpl(gameRecordRepository):

    @classmethod
    def save_record(self, game_id, player_number, dice_values, total_score, is_winner):
        record = GameRecord(
            game_id = game_id,
            player_number = player_number,
            dice_values = dice_values,
            total_score = total_score,
            is_winner = is_winner
        )
        record.save

    def get_all_records(self):
        return GameRecord.objects.all()
    
    def get_records_by_game(self, game_id):
        return GameRecord.objects.filter(game_id = game_id)