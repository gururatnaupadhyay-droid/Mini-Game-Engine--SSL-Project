import pygame
import numpy as np
pygame.init()
class Tic_Tac_Toe:
    def __init__(self,thickness,n_col,size_of_square,Game_count):

        self.thickness=thickness               # thickness is the thickness of line, width is the side of each of the 100 squares on the grid
        self.n_col= n_col                       # n_col is number of columns and rows on the boards
        self.arr=np.zeros((n_col,n_col))            # arr represnt the board as a 10X10 array ( intially this is zero array)
        self.size_of_square= size_of_square              # how big will the size of grid in pixels
        self.width=(size_of_square-(thickness*(n_col+1)))/(n_col)        # length of the side of each of 100 squares in 10X10 grid
        self.Game_count=Game_count       # Game_count is the count of the game number going on
        
        
    def pos_to_arr(self,x): #function which takes x and y co-ordinates as input and tells us index in arr of that particular square
        i=1
        while i < self.n_col-1:
            if( (x >= (i*self.width)+(2*i+1)*self.thickness/2) and (x < (i+1)*(self.width)+(2*i+3)*(self.thickness/2)) ):
              return i
            else:
                i+=1
        if ( x >=0 and x < self.width+(1.5*self.thickness) ):
            return 0
        if ( x >= ((self.n_col-0.5)*self.thickness + (self.n_col-1)*self.width) ):
            return self.n_col-1

    # Main Function 
    def Game_Start(self):

        # Defining the 10X10 Grid 
        screen = pygame.display.set_mode((self.size_of_square,self.size_of_square))
        screen.fill((0,0,0))
        x=0
        while x <= self.size_of_square:
            pygame.draw.line(screen,(255,255,255),(x,0),(x,self.size_of_square),self.thickness)
            pygame.draw.line(screen,(255,255,255),(0,x),(self.size_of_square,x),self.thickness)
            x+=(self.width+self.thickness)
            self.arr=np.zeros((self.n_col,self.n_col))
        pygame.display.update()
         
        next_number=1 # this is the variable which tells what to mark on the grid right after next click 1 represent 'O' 2 represent 'X'

        #Main Loop
        running=True
        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type==pygame.MOUSEBUTTONDOWN : # detecting any mouse click on the grid 
                    if event.button==1:
                        x,y = event.pos
                        X,Y=self.pos_to_arr(x),self.pos_to_arr(y)
                        if self.arr[X][Y]==0 :
                            self.arr[X][Y]=next_number
                        else:
                            continue   
                        
                        font = pygame.font.SysFont("calibri",80)  
                        if next_number==1:
                            text = font.render("O",True,(255,0,0))
                        else:
                            text = font.render("X",True,(255,0,0))
                        abscissa=(((X+1)*self.thickness)+(X*self.width))
                        ordinate=(((Y+1)*self.thickness)+(Y*self.width))  
                        screen.blit(text,(abscissa+6,ordinate-4))    
                        pygame.display.update()

                        winner=self.Check_win(self.arr,self.n_col,next_number)
                        
                        if winner == 2 :
                            pygame.draw.rect(screen,(255,255,255),pygame.Rect(120,175,360,150))
                            x = pygame.font.Font(None,40)
                            y = pygame.font.Font(None,20)
                            stat_0=x.render( " GAME OVER ",True , (0,0,0))
                            stat_1=y.render(f"Congo!! Player2 Wins The Game Number {self.Game_count}",True,(0,0,0))
                            screen.blit(stat_0,(200,200))
                            screen.blit(stat_1,(150,230))                                
                            pygame.display.update()
                            break
                                
                        elif winner ==1 :   
                            pygame.draw.rect(screen,(255,255,255),pygame.Rect(120,175,360,150))
                            x = pygame.font.Font("arial",40)
                            y = pygame.font.Font("arial",20)
                            stat_0=x.render( " GAME OVER ",True,(0,0,0))
                            stat_1=y.render(f"Congo!! Player1 Wins The Game Number {self.Game_count}",True ,(0,0,0))
                            screen.blit(stat_0,(200,200))
                            screen.blit(stat_1,(150,230))
                            pygame.display.update()
                            break
                                
                        if next_number==1:
                            next_number=2
                        else:
                            next_number=1
                elif event.type==pygame.KEYDOWN: 
                    if event.key == pygame.K_r: # if player press the keyboard key 'r' it will restart the game
                        self.Game_count+=1
                        self.Game_Start()      
            
    # The below function checks if their is any diagonal win for the player
    # In this function the idea is to flatten the arr and then use slicing with a gap of n_col-1 and n_col+1 to check both the possiblites of diagonals
    def Diagonal_Check(self,array,n_col,chance): 
        arr_chance=np.array([chance,chance,chance,chance,chance])
        for i in range(4,n_col-1):
            for j in range(0,n_col-5):
                # element at array[i][j] will be now in arr_temp[j*n_col+i]

                arr_temp1=array.reshape(-1)
                if((arr_chance==arr_temp1[(i+(n_col*j)):i+(n_col*j)+5*(n_col-1):n_col-1]).all()):
                    return chance
        for i in range(0,n_col-5):
            for j in range(0,n_col-5):
                arr_temp2=array.reshape(-1)
                if((arr_chance==arr_temp2[(i+(n_col*j)):i+(n_col*j)+5*(n_col+1):n_col+1]).all()):
                    return chance
        return 0    
    # The below function checks if their is win at that postion for the player 
    # It uses the above Diagonal_Check function 

    def Check_win(self,arr,n_col,chance):
        arr_1 = np.array([chance,chance,chance,chance,chance])
        for i in range(0,n_col-1):
            for j in range(0,n_col-5):
                if((arr[j:j+5,i]==arr_1).all()):
                    return chance
        for i in range(0,n_col-1):
            for j in range(0,n_col-5):
                if((arr[i,j:j+5]==arr_1).all()):
                    return chance   
        return self.Diagonal_Check(arr,n_col,chance)  
    
game = Tic_Tac_Toe(thickness=1, n_col=10, size_of_square=600,Game_count=1)
game.Game_Start()
 
