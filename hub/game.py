import sys
import numpy as np
import pygame

pygame.init()


class BoardGame:
    def __init__(self, p1_name, p2_name, rows):
        self.player1 = p1_name
        self.player2 = p2_name
        
        self.current_turn = 1  # 1 for Player 1, 2 for Player 2

    def switch_turn(self,player):
        """Standard logic for all 2-player games"""
        return (3 - player)

    def check_winner(self):
        """This is an overridable method. 
        It does nothing here, but child classes WILL define it."""
        raise NotImplementedError("Each game must define its own win logic!")

'''# How your Othello would use it:
class Othello(BoardGame):
    def __init__(self, p1, p2):
        # 'super' tells the Parent (BoardGame) to set up the 8x8 board
        super().__init__(p1, p2, 8, 8) 
    
    def check_winner(self):
        # Here you put the Othello-specific logic you wrote earlier
        # Counting black vs white pieces
        pass
    '''
player1=sys.argv[1]
player2=sys.argv[2]

if __name__== "__main__":
    from othello import Othello
    from tictactoe import Tic_Tac_Toe

    #game=input("which game do you wnat to play today?")


    game = Tic_Tac_Toe(thickness=2, n_col=10, width=60, Game_count=1, length_of_win=5)
    game.Game_Start()
    '''
    game = Othello(thickness=2, n_col=8, size_of_square=600, Game_count=1)
    helps = input("Do you require use of guides in this game (y/n) ")
    if (helps.lower() == "y"):
        game.help = True
    game.Game_Start()
    print(game.winner)'''