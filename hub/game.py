import sys
import numpy as np
import csv
import pygame
pygame.init()
import os
from datetime import datetime
os.environ['SDL_VIDEO_CENTERED'] = '1'                  #this is done so that the pygame game window is centered on the screen


pref=None
class BoardGame:
    player1 = sys.argv[1]
    player2 = sys.argv[2]
   
    def __init__(self, p1_name, p2_name, rows):
        self.winner= ""
        self.loser=""
        
        self.current_turn = 1  # 1 for Player 1, 2 for Player 2

    def switch_turn(self,player):
        """Standard logic for all 2-player games"""
        return (3 - player)

    def check_winner(self):
        """This is an overridable method. 
        It does nothing here, but child classes WILL define it."""
        raise NotImplementedError("Each game must define its own win logic!")

'''
class Othello(BoardGame):
    def __init__(self, p1, p2):
        # 'super' tells the Parent (BoardGame) to set up the 8x8 board
        super().__init__(p1, p2, 8, 8) 
    
    def check_winner(self):
        # Here you put the Othello-specific logic you wrote earlier
        # Counting black vs white pieces
        pass
    '''
#player1=sys.argv[1]
#player2=sys.argv[2]

if __name__== "__main__":           #kill-switch sort of ,only runs this part of the code if i ran this file directly
    from othello import Othello
    from tictactoe import Tic_Tac_Toe

    #game=input("which game do you wnat to play today?")

'''
    game = Tic_Tac_Toe(thickness=2, n_col=10, width=60, Game_count=1, length_of_win=5)
    game.Game_Start()
    
    game = Othello(thickness=2, n_col=8, size_of_square=600, Game_count=1)
    helps = input("Do you require use of guides in this game (y/n) ")
    if (helps.lower() == "y"):
        game.help = True
    game.Game_Start()
    print(game.winner)'''

screen = pygame.display.set_mode((600, 400))
font = pygame.font.SysFont("Arial", 20)

def draw_button(text, x, y, w, h, color):
    global screen
    """Helper to draw a box with text centered inside"""
    rect = pygame.Rect(x, y, w, h)
    pygame.draw.rect(screen, color, rect, border_radius=10)
    # Render Text
    text_surf = font.render(text, True, (255, 255, 255))
    text_rect = text_surf.get_rect(center=rect.center)
    screen.blit(text_surf, text_rect)
    return rect

def stats():
    while True:
        global pref 
        pref=None
        screen.fill((30, 30, 30))
        btn_print=draw_button("Display Leaderboard by",210,50,180,100,(30,30,30))
        btn_name=draw_button("Name",33,200,100,50,(0,0,0))
        btn_win=draw_button("Wins",166,200,100,50,(0,0,0))
        btn_lose=draw_button("Loss",300,200,100,50,(0,0,0))
        btn_ratio=draw_button("W/L Ratio",433,200,100,50,(0,0,0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pref="NONE"
                break
                
            
            
            if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
                mouse_pos=event.pos
                if btn_name.collidepoint(mouse_pos):
                    
                    pref=1
                    break
                elif btn_win.collidepoint(mouse_pos):
                    
                    pref=2
                    break
                elif btn_lose.collidepoint(mouse_pos):
                    
                    pref=3
                    break
                elif btn_ratio.collidepoint(mouse_pos):
                    
                    pref=4
                    break

        if pref :
            #running=False
            
            os.system(f'bash leaderboard.sh "{pref}"')
            break

def main_menu():
    running = True
    while running:
        global screen
        screen.fill((30, 30, 30))
        
        # Draw our two selection boxes
        btn_othello = draw_button("Play Othello", 100, 100, 180, 100, (34, 139, 34))
        btn_tictac = draw_button("Play Tic-Tac-Toe", 320, 100, 180, 100, (70, 130, 180))
        btn_quit =draw_button("Quit",210 ,260 ,180,100,(240,10,10))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # Left click
                    mouse_pos = event.pos
                    if btn_quit.collidepoint(mouse_pos):
                        running = False
                        
                        

                    if btn_tictac.collidepoint(mouse_pos):
                        file1=open("history.csv","a")
                        writer = csv.writer(file1)
                        game = Tic_Tac_Toe(thickness=2, n_col=10, width=60, Game_count=1, length_of_win=5)
                        game.Game_Start()
                        screen = pygame.display.set_mode((600, 400))
                        font = pygame.font.SysFont("Arial", 20)
                        if game.winner and game.loser:
                                writer.writerow([game.winner,game.loser,datetime.now(),"Tic-Tac-Toe"])
                        file1.close()
                        stats()
                        
                    
                    if btn_othello.collidepoint(mouse_pos):
                        file1=open("history.csv","a")
                        writer = csv.writer(file1)

                        game = Othello(thickness=2, n_col=8, size_of_square=600, Game_count=1)
                        
                        helper=True
                        while helper:
                            screen.fill((30, 30, 30))
                            btn_oth_help=draw_button("Do you want suggestive helping?", 150,40,300,100, (34,34,34))
                            btn_yes=draw_button("Yes", 100,150,180,100,(34,139,34))
                            btn_no=draw_button("No", 320,150,180,100,(70,130,180))
                            pygame.display.update()
                            
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    pygame.quit(); exit()
                                if event.type==pygame.MOUSEBUTTONDOWN and event.button ==1 :
                                    mouse_pos=event.pos
                                    if btn_yes.collidepoint(mouse_pos):
                                        game.help = True
                                        helper=not helper
                                    elif btn_no.collidepoint(mouse_pos):
                                        game.help=False
                                        helper=not helper
                        game.Game_Start()
                        screen = pygame.display.set_mode((600, 400))
                        font = pygame.font.SysFont("Arial", 20)
                        if game.winner and game.loser :
                            writer.writerow([game.winner,game.loser,datetime.now(),"Othello"])
                        file1.close()
                        stats()



        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
        
        main_menu()
        
        
        
