import pygame
import numpy as np
pygame.init()
class Othello:
    def __init__(self,thickness,n_col,size_of_square,Game_count,Helper,Mode):

        self.thickness=thickness               # thickness is the thickness of line, width is the side of each of the 100 squares on the grid
        self.n_col= n_col                       # n_col is number of columns and rows on the boards
        self.arr=np.zeros((n_col,n_col))            # arr represnt the board as a 10X10 array ( intially this is zero array)
        self.size_of_square= size_of_square           # how big will the size of grid in pixels
        self.width=(size_of_square-(thickness*(n_col+1)))/(n_col)        # length of the side of each of 100 squares in 10X10 grid
        self.Game_count=Game_count       # Game_count is the count of the game number going on
        self.screen = pygame.display.set_mode((self.size_of_square+160,self.size_of_square))
        self.Helper=Helper
        self.Mode=Mode
        if(Mode=='Classic'):
            self.p1_color=(0,0,0)
            self.p2_color=(255,255,255)
            self.background_color=(39,134,39)
            self.line_color=(0,0,0)
            self.win_box_color=(255,255,255)
            self.text_color=(0,0,0)
        elif Mode=='Dark':
            self.p1_color=(0, 229, 255)
            self.p2_color=(255,46,99)
            self.background_color=(18,18,18)
            self.line_color=(70,70,70)
            
    
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
        
    def Change_Board(self,screen):
        for i in range(self.n_col):
            for j in range(self.n_col):
                if(self.arr[i][j]==1):
                    pygame.draw.circle(screen,(self.p1_color),((j+1)*self.thickness+(j+0.5)*self.width,(i+1)*self.thickness+(i+0.5)*self.width),self.width/2)
                    pygame.draw.circle(screen,(self.p1_color),((j+1)*self.thickness+(j+0.5)*self.width,(i+1)*self.thickness+(i+0.5)*self.width),self.width/2,2)
                elif self.arr[i][j]==2:
                    pygame.draw.circle(screen,(self.p2_color),((j+1)*self.thickness+(j+0.5)*self.width,(i+1)*self.thickness+(i+0.5)*self.width),self.width/2)
                    pygame.draw.circle(screen,(self.p2_color),((j+1)*self.thickness+(j+0.5)*self.width,(i+1)*self.thickness+(i+0.5)*self.width),self.width/2,2)    
        pygame.display.update()


    def Change_if_Valid(self,x,y,chance,check_valid):  # I used slicing here also coz i was confused where to use loops and where not that's why its conditions
        arr_copy=self.arr.copy()
        self.arr[x][y]=chance
        Horizontal=False
        Vertical=False
        Diagonal1=False
        Diagonal2=False
        if chance==1:
            k=2
        else:
            k=1    
        #Horizonatal Check
        for j in range(self.n_col):
            if self.arr[x][j]==chance and j!=y and j!=y-1 and j!=y+1 :
                if (self.arr[x,min(j,y)+1:max(j,y)]==np.full(abs(j-y)-1,k)).all():
                    self.arr[x,min(j,y)+1:max(j,y)]=np.full(abs(j-y)-1,chance)
                    Horizontal=True

        #Vertical Check
        for i in range(self.n_col):
            if self.arr[i][y]==chance and i!=x and i!=x-1 and i!=x+1 :
                if (self.arr[min(i,x)+1:max(i,x),y]==np.full(abs(i-x)-1,k)).all():
                    self.arr[min(i,x)+1:max(i,x),y]=np.full(abs(i-x)-1,chance)
                    Vertical=True

        #Diagonal Check /
        i=x
        j=y
        while i<self.n_col-1 and j>0:
            i+=1
            j-=1

        while i>=0 and j<self.n_col :
            temp_arr=self.arr.reshape(-1).copy()
            if self.arr[i][j]==chance and abs(i-x)>1 and (temp_arr[min(i,x)*self.n_col+max(j,y)+self.n_col-1:max(i,x)*self.n_col+min(j,y):self.n_col-1]==np.full(abs(i-x)-1,k)).all():
                temp_arr[min(i,x)*self.n_col+max(j,y)+self.n_col-1:max(i,x)*self.n_col+min(j,y):self.n_col-1]=np.full(abs(i-x)-1,chance)
                self.arr=temp_arr.reshape(self.n_col,self.n_col)
                Diagonal1=True
            i-=1  
            j+=1 

        #Diagonal Check \ 
        i2=x
        j2=y
        while j2>0 and i2>0:
            i2-=1
            j2-=1

        while j2<self.n_col and i2<self.n_col :
            temp_arr=self.arr.reshape(-1).copy()
            if self.arr[i2][j2]==chance and abs(i2-x)>1 and (temp_arr[min(i2,x)*self.n_col+min(j2,y)+self.n_col+1:max(i2,x)*self.n_col+max(j2,y):self.n_col+1]==np.full(abs(i2-x)-1,k)).all():
                temp_arr[min(i2,x)*self.n_col+min(j2,y)+self.n_col+1:max(i2,x)*self.n_col+max(j2,y):self.n_col+1]=np.full(abs(i2-x)-1,chance)
                self.arr=temp_arr.reshape(self.n_col,self.n_col)
                Diagonal2=True
            j2+=1  
            i2+=1 
        if not check_valid :
            if(Horizontal or Vertical or Diagonal1 or Diagonal2):
                return 1
            else:
                self.arr[x][y]=0
                return 0
        else:
            self.arr=arr_copy
            return (Horizontal or Vertical or Diagonal1 or Diagonal2) 

    def Change(self,next_number):
        if next_number==1:
            return 2
        else:
            return 1    

    def areValid_postions(self,nn):
        for i in range(self.n_col):
            for j in range (self.n_col):
                if self.arr[i][j]==0 and self.Change_if_Valid(i,j,nn,True):
                    return True
        return False

    def Grid_Set (self):
        self.screen.fill(self.background_color)
        x=0
        self.arr=np.zeros((self.n_col,self.n_col))
        self.arr[3][4]=1
        self.arr[4][3]=1
        self.arr[3][3]=2
        self.arr[4][4]=2
        while x <= self.size_of_square:
            pygame.draw.line(self.screen,(self.line_color),(x,0),(x,self.size_of_square),self.thickness)
            pygame.draw.line(self.screen,(self.line_color),(0,x),(self.size_of_square,x),self.thickness)
            x+=(self.width+self.thickness)
        self.Change_Board(self.screen)
        pygame.display.update()    

    def Show_Valid_Moves(self,nn):
        for i in range(self.n_col):
            for j in range(self.n_col):
                if self.Change_if_Valid(i,j,nn,True) and nn==1 and self.arr[i][j]==0: 
                    pygame.draw.circle(self.screen,(self.p1_color),((j+1)*self.thickness+(j+0.5)*self.width,(i+1)*self.thickness+(i+0.5)*self.width),self.width/2,2)
                elif self.Change_if_Valid(i,j,nn,True) and nn==2 and self.arr[i][j]==0:
                    pygame.draw.circle(self.screen,(self.p2_color),((j+1)*self.thickness+(j+0.5)*self.width,(i+1)*self.thickness+(i+0.5)*self.width),self.width/2,2)

        pygame.display.update()

    def Hide_Valid_Moves(self,nn):
        for i in range(self.n_col):
            for j in range(self.n_col):
                if(self.Change_if_Valid(i,j,nn,True) and self.arr[i][j]==0):
                    pygame.draw.circle(self.screen,(self.background_color),((j+1)*self.thickness+(j+0.5)*self.width,(i+1)*self.thickness+(i+0.5)*self.width),self.width/2,2)
        pygame.display.update()

    def Score_Displayer(self):
        white=0
        black=0
        for i in range(self.n_col):
            for j in range(self.n_col):
                if(self.arr[i][j]!=0):
                    if self.arr[i][j]==1:
                        black+=1
                    else:
                        white+=1   
        pygame.draw.circle(self.screen,(self.p1_color),(self.size_of_square+0.5*self.width+3,200),self.width/2) 
        pygame.draw.circle(self.screen,(self.p2_color),(self.size_of_square+0.5*self.width+3,400),self.width/2)
        font =  pygame.font.Font(None,80)
        text = font.render(f"{black}",True,(self.p1_color))
        text2= font.render(f"{white}",True,(self.p2_color))
        self.screen.fill((self.background_color),(self.size_of_square+self.width+15,self.thickness,145-self.width,500))
        self.screen.blit(text,(self.size_of_square+self.width+15,200-15))
        self.screen.blit(text2,(self.size_of_square+self.width+15,400-15))
        pygame.display.update()

    def Check_Win(self):
        arrcopy=self.arr.copy()
        arrcopy[arrcopy==2]=-1
        if arrcopy.mean()<0:
            return 2
        elif arrcopy.mean()>0:
            return 1
        else:
            return 0
        
                        
    # Main Function 
    def Game_Start(self):
        self.Grid_Set()
        next_number=1
        
        #Main Loop
        running=True
        while running:
            if(self.Helper):
                self.Show_Valid_Moves(next_number)   
            self.Score_Displayer()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False             
                #pygame.draw.rect(self.screen,self.win_box_color,(50,(self.size_of_square/2)-100,60+self.size_of_square,200))
                if not (self.areValid_postions(1) or self.areValid_postions(2)):# if their is no valid position for curr value of next_number change it
                    if self.Check_Win()!=0:
                        (f"player{self.Check_Win()} wins the game")
                    else:
                        print("DRAW")   
                    surface=pygame.surface((400,300))
                    x = pygame.font.Font(None,50)
                    state0=x.render("GAME OVER",True,self.text_color)
                    state1=y.render("Player Won The Game")
                    
                    running=False                       
                               
                elif not self.areValid_postions(next_number):    # if their are no valid postions for any of 1 or 2 means game is over  
                    next_number=self.Change(next_number)
                
                elif event.type==pygame.MOUSEBUTTONDOWN and event.button==1: # detecting left mouse click on the grid          
                    self.Hide_Valid_Moves(next_number)
                    x,y = event.pos
                    X,Y=self.pos_to_arr(x),self.pos_to_arr(y)

                    if self.arr[Y][X]==0 and self.Change_if_Valid(Y,X,next_number,True): #checks if the place is empty and its valid move
                        self.Change_if_Valid(Y,X,next_number,False)  # now modify
                        self.Change_Board(self.screen)
                        next_number=self.Change(next_number)    


game = Othello(thickness=2, n_col=8, size_of_square=600, Game_count=1,Helper=True,Mode='Dark')
game.Game_Start()
