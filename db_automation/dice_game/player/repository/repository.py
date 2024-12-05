class GameRepository:
    def __init__(self):
        self.game_history = []  # 게임 기록을 저장할 리스트

    # 게임 결과 저장
    def save_game_result(self, player1, player2):
        if player1.total_score > player2.total_score:
            winner = player1.name
        elif player2.total_score > player1.total_score:
            winner = player2.name
        else:
            winner = "무승부"

        self.game_history.append({
            "player1": player1.name,
            "player1_rolls": player1.dice_rolls,
            "player1_score": player1.total_score,
            "player2": player2.name,
            "player2_rolls": player2.dice_rolls,
            "player2_score": player2.total_score,
            "winner": winner
        })