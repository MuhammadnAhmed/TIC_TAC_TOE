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

class GeniousComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves()) #randomly choose 1 for the first turn

        else:
            #get square using minimax algo
            square = self.minimax(game, self.letter)['position']
            return square

    def minimax(self, game_state, player):
        max_player = self.letter
        other_player = 'O' if player == 'X' else 'X' 

        #check if previous move was a win
        if game_state.current_winner == other_player:
            return {'position' : None,
                    'score' : 1 *(game_state.num_empty_squares() + 1) if other_player == max_player else
                    -1 *(game_state.num_empty_squares() + 1)
                   }

        elif not game_state.empty_squares():
            return {'position' : None , 'score' : 0}

        #initialize dictionaries
        if player == max_player:
            best = {'position' : None, 'score' : -math.inf}
        else:
            best = {'position' : None, 'score' : math.inf}

        for possible_move in game_state.available_moves():
            # step 1: make a move. try that move
            game_state.make_move(possible_move,player)

            # step 2: recurse using minimax
            sim_score = self.minimax(game_state, other_player)

            # step 3: undo the move
            game_state.board[possible_move] = ' '
            game_state.current_winner = None
            sim_score['position'] = possible_move

            # step 4: update dictionaries
            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score

        return best




