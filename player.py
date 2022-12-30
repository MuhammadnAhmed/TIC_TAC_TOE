import random
import math


class Player:
    def __init__(self, letter):
        # Letter is X or O
        self.letter = letter

    def get_move(self, game):
        pass

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        # computer selects randomly from available moves
        square = random.choice(game.available_moves())
        return square
        

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-8) = ')
            # Checking if the input is valid or not. 
            # input should be available on the board too.
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True

            except ValueError:
                print('Invalid Input. TRY again')

        return val
