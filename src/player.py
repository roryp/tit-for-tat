import random

class Player:
    def __init__(self, strategy):
        self.strategy = strategy
        self.score = 0

    def get_move(self, history):
        if self.strategy == 'tit-for-tat':
            if len(history) == 0:
                return 'cooperate'
            else:
                return history[-1][1]
        elif self.strategy == 'defect':
            return 'defect'
        elif self.strategy == 'random':
            return random.choice(['cooperate', 'defect'])
        else:
            pass

    def update_score(self, points):
        self.score += points

    def get_score(self):
        return self.score