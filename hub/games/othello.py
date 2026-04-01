import pygame
import numpy as np
pygame.init()
class Othello:
    def __init__(self,thickness,n_col,size_of_square,Game_count):

        self.thickness=thickness               # thickness is the thickness of line, width is the side of each of the 100 squares on the grid
        self.n_col= n_col                       # n_col is number of columns and rows on the boards
        self.arr=np.zeros((n_col,n_col))            # arr represnt the board as a 10X10 array ( intially this is zero array)
        self.size_of_square= size_of_square              # how big will the size of grid in pixels
        self.width=(size_of_square-(thickness*(n_col+1)))/(n_col)        # length of the side of each of 100 squares in 10X10 grid
        self.Game_count=Game_count       # Game_count is the count of the game number going on
        self.screen = pygame.display.set_mode((self.size_of_square,self.size_of_square))
      
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
                if(self.arr[i][j]!=0):
                    pygame.draw.circle(screen,(255*abs(1-self.arr[i][j]),255*abs(1-self.arr[i][j]),255*abs(1-self.arr[i][j])),((j+1)*self.thickness+(j+0.5)*self.width,(i+1)*self.thickness+(i+0.5)*self.width),self.width/2)
                    pygame.draw.circle(screen,(255*abs(1-self.arr[i][j]),255*abs(1-self.arr[i][j]),255*abs(1-self.arr[i][j])),((j+1)*self.thickness+(j+0.5)*self.width,(i+1)*self.thickness+(i+0.5)*self.width),self.width/2,2)
        


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

    def areValid_postions(self,next_number):
        for i in range(self.n_col):
            for j in range (self.n_col):
                if self.arr[i][j]==0 and self.Change_if_Valid(i,j,next_number,True):
                    return 1
        return 0

    def Grid_Set (self):
        self.screen.fill((39,134,39))
        x=0
        self.arr=np.zeros((self.n_col,self.n_col))
        while x <= self.size_of_square:
            pygame.draw.line(self.screen,(0,0,0),(x,0),(x,self.size_of_square),self.thickness)
            pygame.draw.line(self.screen,(0,0,0),(0,x),(self.size_of_square,x),self.thickness)
            x+=(self.width+self.thickness)
        self.arr[3][3]=2 # White
        self.arr[4][4]=2 # White
        self.arr[3][4]=1 # Black
        self.arr[4][3]=1 # Black
        self.Change_Board(self.screen)
        pygame.display.update()    

    #def Check_Win(self):
        # TO BE WRITTEN
                   
    # Main Function 
    def Game_Start(self):
        self.Grid_Set()
        next_number=1
        Last_State=self.arr.copy()
        #Main Loop
        running=True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    
                if not self.areValid_postions(next_number):  # if their is no valid position for curr value of next_number change it
                        next_number=self.Change(next_number) 

                elif event.type == pygame.KEYDOWN and event.key == pygame.K_u:
                    self.Grid_Set()
                    self.arr=Last_State.copy()
                    self.Change_Board(self.screen)
                    pygame.display.update()               
           # elif not (self.areValid_postions(1) or self.areValid_postions(2)):    # if their are no valid postions for any of 1 or 2 means game is over  
              #             self.Check_Win()
                elif event.type==pygame.MOUSEBUTTONDOWN and event.button==1: # detecting left mouse click on the grid          
                    x,y = event.pos
                    X,Y=self.pos_to_arr(x),self.pos_to_arr(y)

                    if self.arr[Y][X]==0 and self.Change_if_Valid(Y,X,next_number,True): #checks if the place is empty and its valid move
                        Last_State = self.arr.copy()                 # save clean state
                        self.Change_if_Valid(Y,X,next_number,False)  # now modify
                        self.Change_Board(self.screen)
                        pygame.display.update()
                        next_number=self.Change(next_number)    


game = Othello(thickness=2, n_col=8, size_of_square=600, Game_count=1)
game.Game_Start()
