class Game:
    def __init__(self, player1, player2, num_rounds):
        self.player1 = player1
        self.player2 = player2
        self.num_rounds = num_rounds
        self.history = []

    def calculate_payoff(self, move1, move2):
        # This is a simple payoff matrix for the Prisoner's Dilemma
        # You can replace this with the payoff matrix for your game
        if move1 == 'cooperate' and move2 == 'cooperate':
            return 2, 2
        elif move1 == 'cooperate' and move2 == 'defect':
            return 0, 3
        elif move1 == 'defect' and move2 == 'cooperate':
            return 3, 0
        else:  # move1 == 'defect' and move2 == 'defect'
            return 1, 1

    def play_round(self):
        move1 = self.player1.get_move(self.history)
        move2 = self.player2.get_move(self.history)
        self.history.append((move1, move2))

        # Calculate the payoffs and update the players' scores
        payoff1, payoff2 = self.calculate_payoff(move1, move2)
        self.player1.update_score(payoff1)
        self.player2.update_score(payoff2)

    def play_game(self):
        for _ in range(self.num_rounds):
            self.play_round()