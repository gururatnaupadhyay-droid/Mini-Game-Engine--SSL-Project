import pygame
import numpy as np
pygame.init()
class Connect_4:
    def __init__(self,n_col,size_of_square,gap,Game_count,border):

        self.n_col= n_col                       # n_col is number of columns and rows on the boards
        self.arr=np.zeros((n_col,n_col))            # arr represnt the board as a 10X10 array ( intially this is zero array)
        self.size_of_square= size_of_square           # how big will the size of grid in pixels
        self.diameter=(self.size_of_square-((n_col+1)*gap))/n_col
        self.gap=gap 
        self.Game_count=Game_count       # Game_count is the count of the game number going on
        self.screen = pygame.display.set_mode((self.size_of_square+2*border,self.size_of_square+2*border))
        self.border=border


    def pos_to_arr(self,x): #function which takes x and y co-ordinates as input and tells us index in arr of that particular square
        x-=self.border
        if ( x<self.diameter+self.gap):
            return 0
        if ( x>(self.diameter+self.gap)*(self.n_col-1)):
            return self.n_col-1
        i=1
        while i<self.n_col-1:
            if( x > i*(self.gap+self.diameter) and x<(i+1)*(self.gap+self.diameter)):
                return i 
            i+=1


    def Change(self,next_number):
        if next_number==1:
            return 2
        else:
            return 1  

    def Grid_Set (self):
        
        self.screen.fill((18, 18, 18))
        self.arr=np.zeros((self.n_col,self.n_col))
        y=self.border+self.gap+self.diameter/2
        for i in range(7):
            x=self.border+self.gap+self.diameter/2
            for j in range(7):
                pygame.draw.circle(self.screen,(42, 42, 42),(x,y),self.diameter/2)
                pygame.draw.circle(self.screen,(42, 42, 42),(x,y),self.diameter/2,2)
                x+=self.gap+self.diameter
            y+=self.gap+self.diameter  
        pygame.display.update() 


    def Check_Win(self,chance,x,y):

        arr1=np.full(4,chance)
        #vertical check |
        if((y+4 <= self.n_col and (self.arr[x,y:y+4]==arr1).all())):
            return 1
        elif(y-1>=0 and y+3<=self.n_col and (self.arr[x,y-1:y+3]==arr1).all()):
            return 1
        elif (y+2 <= self.n_col and y-2>=0 and (self.arr[x,y-2:y+2]==arr1).all()):
            return 1
        elif (y+1 <= self.n_col and y-3>=0 and (self.arr[x,y-3:y+1]==arr1).all()):
            return 1
        
        #horizontal check --
        elif (x+4 <= self.n_col and (self.arr[x:x+4,y]==arr1).all()):
            return 1
        elif (x-1>=0 and x+3<=self.n_col and (self.arr[x-1:x+3,y]==arr1).all()):
            return 1
        elif (x+1 <= self.n_col and x-3>=0 and (self.arr[x-3:x+1,y]==arr1).all()):
            return 1
        elif (x+2 <= self.n_col and x-2>=0 and (self.arr[x-2:x+2,y]==arr1).all()):
            return 1
        
        #diagonal /
        elif ( x+3<= self.n_col-1 and y-3>=0 and (self.arr[np.array([x,x+1,x+2,x+3]),np.array([y,y-1,y-2,y-3])]==arr1).all()):
            return 1
        elif ( x+2<= self.n_col-1 and x-1>=0 and y-2>=0 and y+1<=self.n_col-1 and (self.arr[np.array([x-1,x,x+1,x+2]),np.array([y+1,y,y-1,y-2])]==arr1).all()):
            return 1
        elif ( x+1<= self.n_col-1 and x-2>=0 and y-1>=0 and y+2<=self.n_col-1 and (self.arr[np.array([x-2, x-1, x, x+1]), np.array([y+2, y+1, y, y-1])]==arr1).all()):
            return 1
        elif ( x-3>=0 and y+3<=self.n_col-1 and (self.arr[np.array([x-3,x-2,x-1,x]),np.array([y+3,y+2,y+1,y])]==arr1).all()):
            return 1
        
        #diagonal \
        elif ( x-3>=0 and y-3>=0  and (self.arr[np.array([x-3, x-2, x-1, x]), np.array([y-3,y-2,y-1,y])]==arr1).all()):
            return 1
        elif ( x+1<= self.n_col-1 and y-2>=0 and x-2>=0 and y+1<=self.n_col-1 and (self.arr[np.array([x-2,x-1,x,x+1]),np.array([y-2,y-1,y,y+1])]==arr1).all()):
            return 1
        elif ( x+2<=self.n_col-1 and x-1>=0 and y-1>=0 and y+2<=self.n_col-1 and (self.arr[np.array([x-1,x,x+1,x+2]),np.array([y-1,y,y+1,y+2])]==arr1).all()):
            return 1
        elif (x+3<=self.n_col-1 and y+3<=self.n_col-1 and (self.arr[np.array([x,x+1,x+2,x+3]),np.array([y,y+1,y+2,y+3])]==arr1).all()):
            return 1
        
        for i in range(self.n_col):
            for j in range(self.n_col):
                if(self.arr[i][j]==0):
                    return 0

        return -1        
    
    def Game_Start(self):
            self.Grid_Set()
            next_number=1 # 1 is for blue 2 is for red
            
            #Main Loop
            running=True
            while running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    elif event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
                        x,y= event.pos
                        temp=-1
                        for i in range(self.n_col):
                            if(self.arr[self.pos_to_arr(x)][self.n_col-1-i]==0): #chossing bottom most circle
                                self.arr[self.pos_to_arr(x)][self.n_col-1-i]=next_number
                                temp=i
                                if(next_number==1):
                                    pygame.draw.circle(self.screen,(0, 229, 255),((((1+self.pos_to_arr(x))*(self.gap+self.diameter))-0.5*self.diameter+self.border),(self.n_col-i)*(self.gap+self.diameter)-0.5*self.diameter+self.border),self.diameter/2)
                                    pygame.draw.circle(self.screen,(0, 229, 255),((((1+self.pos_to_arr(x))*(self.gap+self.diameter))-0.5*self.diameter+self.border),(self.n_col-i)*(self.gap+self.diameter)-0.5*self.diameter+self.border),self.diameter/2,2)
                                else:
                                    pygame.draw.circle(self.screen,(255, 46, 99),((((1+self.pos_to_arr(x))*(self.gap+self.diameter))-0.5*self.diameter+self.border),(self.n_col-i)*(self.gap+self.diameter)-0.5*self.diameter+self.border),self.diameter/2)
                                    pygame.draw.circle(self.screen,(255, 46, 99),((((1+self.pos_to_arr(x))*(self.gap+self.diameter))-0.5*self.diameter+self.border),(self.n_col-i)*(self.gap+self.diameter)-0.5*self.diameter+self.border),self.diameter/2,2)
                                break
                        pygame.display.update()  
                        if(temp!=-1 and self.Check_Win(next_number,self.pos_to_arr(x),self.n_col-1-temp)):
                            print(f"player{next_number} won the game")
                            self.Game_count+=1
                            running=False
                        elif (temp!=-1 and self.Check_Win(next_number,self.pos_to_arr(x),self.n_col-1-temp)==-1) :
                            running=False    
                            self.Game_count+=1
                            print("draw")
                        next_number=self.Change(next_number)
                        
                        
game = Connect_4( n_col=7, size_of_square=450,gap=4, Game_count=1,border=75)
game.Game_Start()
