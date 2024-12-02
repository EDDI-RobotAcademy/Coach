from rest_framework import viewsets, status
from rest_framework.response import Response
from dice_game.game_record.repository.game_record_repository_impl import gameRecordRepositoryImpl
from dice_game.game_record.entity.game_record_entity import GameRecord

class gameRecordController(viewsets.ViewSet):
    repository = gameRecordRepositoryImpl()

    def save_game_record(self,request):
        data = request.data
        required_fields = ['game_id', 'player_number', 'dice_values', 'total_score', 'is_winner']

        for field in required_fields:
            if field not in data:
                return Response({"error": f"{field} is required."}, status=status.HTTP_400_BAD_REQUEST)
            
        
        self.repository.save_record(
            game_id = data['game_id'],
            player_number = data['player_number'],
            dice_values = data['dice_values'],
            total_score = data['total_score'],
            is_winner = data['is_winner']
        )
        return Response({"message" : "Game record saved successfully."}, status=status.HTTP_201_CREATED)
    
    def get_all_records(self, request):
        records = self.repository.get_all_records()
        data = [
            {
                "game_id" : record.game_id,
                "player_number" : record.player_number,
                "dice_values" : record.dice_value,
                "total_score" : record.total_score,
                "is_winner" : record.is_winner
            }
            for record in records
        ]
        return Response(data, status=status.HTTP_200_OK)
    
    def get_records_by_gameId(self, request):
        game_id = request.GET.get('game_id')
        if not game_id:
            return Response({"error" : "game_id is required"}, status = status.HTTP_400_BAD_REQUEST)
        
        records = self.repository.get_records_by_gameId(game_id)
        data = [
            {
                "game_id" : record.game_id,
                "player_number" : record.player_number,
                "dice_values" : record.dice_values,
                "total_score" : record.total_score,
                "is_winner" : record.is_winner
            }
            for record in records
        ]
        return Response(data, status= status.HTTP_200_OK)

