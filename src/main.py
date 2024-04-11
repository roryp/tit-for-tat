from player import Player
from game import Game

# Create two players
player1 = Player('tit-for-tat')
player2 = Player('random')
game = Game(player1, player2, 10)
game.play_game()

# Print the final scores
print("Player 1 score:", player1.get_score())
print("Player 2 score:", player2.get_score())