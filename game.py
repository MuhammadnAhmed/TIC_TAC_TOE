# Created by Muhammad Ahmed
# Checkout my Portfolio https://a03152049334.wixsite.com/muhammadahmed
# Checkout my Fiverr account https://www.fiverr.com/ahmed189
# Checkout my Upwork account https://www.upwork.com/freelancers/~01e248930a029b5290
# Follow me on LinkedIn http://www.linkedin.com/in/muhammad-ahmed189
# Follow me on GitHub https://github.com/MuhammadnAhmed

import time
import string
import math

from player import HumanPlayer, RandomComputerPlayer

class tic_tac_toe:
    def __init__(self):
        # 3x3 board using a single list
        self.board = [' ' for _ in range (9)]
        # keep track of winner
        self.current_winner = None
    
    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | ' .join(row) + ' |')

    @staticmethod
    def print_board_numbers():
        # it will display the index numbers
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | ' .join(row) + ' |')

    def available_moves(self):
        return[i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        #return len(self.available_moves())
        return self.board.count(' ')

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        else:
            return False 
    def winner(self, square, letter):
        # 3 same in a row or in column or in diagonal will be the winner
        # Checking rows
        row_index = (square)//3
        row = self.board[ row_index*3 : (row_index + 1) * 3 ]
        if all ([spot == letter for spot in row]):
            return True
        
        # Checking columns
        column_index = square%3
        column = [self.board[column_index+i*3] for i in range(3)]
        if all ([spot == letter for spot in column]):
            return True
        
        # checking diagonal.. only 2 diagonals
        # diagonal_squares = 0,2,4,6,8
        if square %2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all ([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all ([spot == letter for spot in diagonal2]):
                return True

        return False


        
def play(game, x_player, o_player, print_game = True):
    if print_game:
        game.print_board_numbers()

    letter = 'X'
    while game.empty_squares:
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)  

         #funtion to make a move
        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes a move to {square}')
                game.print_board()
                print('___________________________________________')
                    
            if game.current_winner:
                if print_game:
                    print(letter + ' Wins')
                return letter

            # change letters
            letter = 'O' if letter == 'X' else 'X'

        time.sleep(0.30)

    if print_game:
        print('It\'s a tie')


if __name__ == '__main__':
    
    x_player = HumanPlayer('X')
    o_player = RandomComputerPlayer('O')

    t = tic_tac_toe()
    play(t , x_player, o_player, True)

