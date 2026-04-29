import sys
import numpy as np
import csv
import pygame
pygame.init()
import os
import matplotlib.pyplot as plt
from datetime import datetime
os.environ['SDL_VIDEO_CENTERED'] = '1'                  #this is done so that the pygame game window is centered on the screen
player1=sys.argv[1]
player2=sys.argv[2]
def chart():
    with open("history.csv","r") as file1:
        rdr=csv.reader(file1)
        oth_freq=0
        tic_freq=0
        conn_freq=0
        rdr=np.array(list(rdr))
        #print(rdr)
        winners=rdr[:,0]
        winners=list(winners)
        #print(winners)
        x=list(set(winners))
        #print(x)
        ct=dict()
        l=[]
        m=[]
        for a in x:
            ct[winners.count(a)]=a
        for y in sorted(ct.keys(),reverse=True):
            l.append(ct[y])
            m.append(y)
        plt.figure(figsize=[10,8])
        plt.subplot(1,2,1)
        plt.bar(l,m,color="blue",width=0.8)
        plt.title("Number of Game Wins by Top Players")
        

        for line in rdr:
            if (line[3]=="Tic-Tac-Toe"):
                tic_freq+=1
            if (line[3]=="Othello"):
                oth_freq+=1
            if (line[3]=="Connect4"):
                conn_freq+=1
        x=oth_freq+conn_freq+tic_freq
        
        oth_freq*=100/x
        tic_freq*=100/x
        conn_freq*=100/x
        plt.subplot(1,2,2)
        plt.title("Frequency of Games Played")
        plt.pie([oth_freq,tic_freq,conn_freq],labels=["Othello","Tic-Tac-Toe","Connect 4"],radius=1)
        plt.savefig("charts.png")
        plt.close()
        
            
pref=None
class BoardGame:
    player1 = sys.argv[1]
    player2 = sys.argv[2]
   
    def __init__(self, p1_name, p2_name, rows):
        self.winner= ""
        self.loser=""
        
        self.current_turn = 1  # 1 for Player 1, 2 for Player 2

    def switch_turn(self,player):
     
        return (3 - player)

    def check_winner(self):
       
        raise NotImplementedError("Each game must define its own win logic!")


if __name__== "__main__":           #kill-switch sort of ,only runs this part of the code if i ran this file directly
    from othello import Othello
    from tictactoe import Tic_Tac_Toe
    from connect4 import Connect_4


screen = pygame.display.set_mode((1350, 900))

font = pygame.font.SysFont("Arial", 30)

def draw_button(text, x, y, w, h, color, img_path=None):
    global screen
    """Draws a button with an optional image and centered text below it"""
    rect = pygame.Rect(x, y, w, h)
    pygame.draw.rect(screen, color, rect, border_radius=10)
    
    # 1. Handle Image Drawing
    if img_path:
        try:
            # Load and scale the image to fit nicely (e.g., 50% of button height)
            icon = pygame.image.load(img_path).convert_alpha()
            icon_size = int(h * 0.5) # Scale icon to 50% of button height
            icon = pygame.transform.scale(icon, (icon_size, icon_size))
            
            # Position icon: centered horizontally, slightly down from top
            icon_rect = icon.get_rect(center=(x + w // 2, y + h // 3))
            screen.blit(icon, icon_rect)
            
            # 2. Render Text (Shifted down to accommodate the image)
            text_surf = font.render(text, True, (255, 255, 255))
            text_rect = text_surf.get_rect(center=(x + w // 2, y + (h * 0.75)))
            screen.blit(text_surf, text_rect)
            
        except pygame.error as e:
            print(f"Couldn't load image {img_path}: {e}")
            # Fallback: Just draw text in the center if image fails
            text_surf = font.render(text, True, (255, 255, 255))
            text_rect = text_surf.get_rect(center=rect.center)
            screen.blit(text_surf, text_rect)
    else:
        # Standard centered text if no image is provided
        text_surf = font.render(text, True, (255, 255, 255))
        text_rect = text_surf.get_rect(center=rect.center)
        screen.blit(text_surf, text_rect)

    return rect

def stats():
    screen = pygame.display.set_mode((600,400))
    while True:
        global pref 
        pref=None
        
        screen.fill((30, 30, 30))
        btn_print=draw_button("Display Leaderboard by",210,50,180,100,(30,30,30))
        btn_name=draw_button("Name",33,200,100,50,(0,0,0))
        btn_win=draw_button("Wins",166,200,100,50,(0,0,0))
        btn_lose=draw_button("Loss",300,200,100,50,(0,0,0))
        btn_ratio=draw_button("W/L Ratio",430,200,145,50,(0,0,0))
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
            chart()
            os.system("open charts.png")
          
            
            break
    screen = pygame.display.set_mode((1350,900))
    

def main_menu():
    running = True
    # Load the image
    bg_image = pygame.image.load("background.png").convert()

    # Scale it to match your screen size (1350, 900)
    bg_image = pygame.transform.scale(bg_image, (1350, 900))
    while running:
        global screen
        
        screen.blit(bg_image, (0, 0))
        # Draw our two selection boxes
        btn_othello = draw_button("OTHELLO", 112, 100, 300, 450, (34, 139, 34),"othello_logo.jpeg")
        btn_tictac = draw_button("TIC-TAC-TOE", 524, 100, 300, 450, (70, 130, 180),"tictactoe_logo.png")
        btn_connect4 = draw_button("CONNECT 4", 936, 100, 300, 450, (255, 215, 0),"connect4_logo.png")
        btn_quit =draw_button("QUIT GAME",375 ,650 ,600,150,(240,10,10))
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
                        game = Tic_Tac_Toe(thickness=2, n_col=10, size_of_square=600,Game_count=1,Winning_Size=5,border=75,Player1=player1,Player2=player2)
                        game.Game_Start()
                       
                        font = pygame.font.SysFont("Arial", 20)
                        if game.winner and game.loser:
                                writer.writerow([game.winner,game.loser,datetime.now(),"Tic-Tac-Toe"])
                        file1.close()
                        stats()

                    if btn_connect4.collidepoint(mouse_pos):
                        file1=open("history.csv","a")
                        writer = csv.writer(file1)
                        game = Connect_4(n_col=7, size_of_square=450,gap=4, Game_count=1,Winning_Size=4,border=75,Player1=player1,Player2=player2)
                        game.Game_Start()
                       
                        font = pygame.font.SysFont("Arial", 20)
                        if game.winner and game.loser:
                                writer.writerow([game.winner,game.loser,datetime.now(),"Tic-Tac-Toe"])
                        file1.close()
                        stats()
                        
                    
                    if btn_othello.collidepoint(mouse_pos):
                        file1=open("history.csv","a")
                        writer = csv.writer(file1)

                        game = Othello(thickness=2, n_col=8, size_of_square=500, Game_count=1,Helper=True,Mode='Dark',Player1=player1,Player2=player2)
                        x=True
                       
                        while x:
                            screen.fill((30, 30, 30))
                            btn_oth_help=draw_button("Do you want suggestive helping?", 100,40,500,100, (100,100,100))
                            btn_yes=draw_button("Yes", 100,250,180,100,(34,139,34))
                            btn_no=draw_button("No", 400,250,180,100,(70,130,180))
                            pygame.display.update()
                            
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    pygame.quit()
                                    exit()
                                if event.type==pygame.MOUSEBUTTONDOWN and event.button ==1 :
                                    mouse_pos=event.pos
                                    if btn_yes.collidepoint(mouse_pos):
                                        game.Helper = True
                                        x=not x
                                    elif btn_no.collidepoint(mouse_pos):
                                        game.Helper=False
                                        x=not x
                                    
                                        
                        game.Game_Start()
                        screen = pygame.display.set_mode((1350,900))
                        font = pygame.font.SysFont("Arial", 20)
                        if game.winner and game.loser :
                            writer.writerow([game.winner,game.loser,datetime.now(),"Othello"])
                        file1.close()
                        stats()



        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
  
        main_menu()
        
        
        
