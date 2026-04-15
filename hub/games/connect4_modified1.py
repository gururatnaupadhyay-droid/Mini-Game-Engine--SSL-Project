import pygame
import numpy as np
import math
pygame.init()
class Connect_4:
    def __init__(self,n_col,size_of_square,gap,Game_count,border,Mode):

        self.n_col= n_col                       # n_col is number of columns and rows on the boards
        self.arr=np.zeros((n_col,n_col))            # arr represnt the board as a 10X10 array ( intially this is zero array)
        self.size_of_square= size_of_square           # how big will the size of grid in pixels
        self.diameter=(self.size_of_square-((n_col+1)*gap))/n_col
        self.gap=gap 
        self.Game_count=Game_count       # Game_count is the count of the game number going on
        self.screen = pygame.display.set_mode((self.size_of_square+2*border,self.size_of_square+1.5*border))
        self.border=border
        self.sound_fahh = pygame.mixer.Sound("falling.mp3")
        #self.sound_phonk= pygame.mixer.Sound("NO_BATIDAO.mp3")
        
        if Mode=='Classic':
            self.background_color = (0, 102, 204)    
            self.empty_circle_color = (0, 0, 0)       
            self.p1_color = (255, 0, 0)               
            self.p2_color = (255, 255, 0)             

        elif Mode=='Dark':
            self.background_color = (18,18,18)
            self.empty_circle_color = (42,42,42)
            self.p1_color = (0, 229, 255)
            self.p2_color = (255, 46, 99)

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
      
    def Grid_Set (self):
        self.screen.fill(self.background_color)
        y=self.border+self.gap+self.diameter/2
        for i in range(7):
            x=self.border+self.gap+self.diameter/2
            for j in range(7):
                pygame.draw.circle(self.screen,self.empty_circle_color,(x,y),self.diameter/2)
                pygame.draw.circle(self.screen,self.empty_circle_color,(x,y),self.diameter/2,2)
                x+=self.gap+self.diameter
            y+=self.gap+self.diameter      

    def Redraw(self):
        self.Grid_Set()
        for i in range(self.n_col):
            for j in range(self.n_col):
                x_coord=(((1+i)*(self.gap+self.diameter))-0.5*self.diameter+self.border)
                y_coord=(j+1)*(self.gap+self.diameter)-0.5*self.diameter+self.border
                if(self.arr[i][j]==1):
                        pygame.draw.circle(self.screen,self.p1_color,(x_coord,y_coord),self.diameter/2)
                        pygame.draw.circle(self.screen,self.p1_color,(x_coord,y_coord),self.diameter/2,2)
                elif self.arr[i][j]==2:    
                        pygame.draw.circle(self.screen,self.p2_color,(x_coord,y_coord),self.diameter/2)
                        pygame.draw.circle(self.screen,self.p2_color,(x_coord,y_coord),self.diameter/2,2)
        

    def Draw_Circle(self,x,y,nn):
        y1=self.border
        y0=0
        speed_factor=0.015 # decides how many times the loop will run ( and hence the speed of ball ) like if its 0.01 loop will run about 100 times and so on
        clock=pygame.time.Clock()
        jerk_factor=5 # so as we increase this we know that sin will lie from 0 to 1 so increasing this will lead to veryy slow increase in the sin at start and verry fast decrease at the end than the normal case when jerk_factor is 1
        self.sound_fahh.play()
        if(nn==1):
                while y0<(y-self.border):
                    self.Redraw()
                    pygame.draw.circle(self.screen,self.p1_color,(x,y1),self.diameter/2)
                    pygame.draw.circle(self.screen,self.p1_color,(x,y1),self.diameter/2,2)
                    pygame.display.update()
                    y0+=speed_factor*(y-self.border)
                    y1=self.border+(y-self.border)*((math.sin(math.pi*0.5*y0/(y-self.border)))**jerk_factor)
                    clock.tick(60)
                
                self.Redraw()
                pygame.draw.circle(self.screen,self.p1_color,(x,y),self.diameter/2)
                pygame.draw.circle(self.screen,self.p1_color,(x,y),self.diameter/2,2)
                pygame.display.update()
                
        else:
                while y0<(y-self.border):
                    self.Redraw()
                    pygame.draw.circle(self.screen,self.p2_color,(x,y1),self.diameter/2)
                    pygame.draw.circle(self.screen,self.p2_color,(x,y1),self.diameter/2,2)
                    pygame.display.update()
                    y0+=speed_factor*(y-self.border)
                    y1=self.border+(y-self.border)*((math.sin(math.pi*0.5*y0/(y-self.border)))**jerk_factor)
                    clock.tick(60)

                self.Redraw()
                pygame.draw.circle(self.screen,self.p2_color,(x,y),self.diameter/2)
                pygame.draw.circle(self.screen,self.p2_color,(x,y),self.diameter/2,2)
                pygame.display.update()    
        
    def Game_Start(self):
            #self.sound_phonk.play(-1)
            self.Grid_Set()
            pygame.display.update()
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
                        check_if_drawn=False
                        for i in range(self.n_col):
                            
                            if(self.arr[self.pos_to_arr(x)][self.n_col-1-i]==0): #chossing bottom most circle
                                temp=i
                                check_if_drawn=True
                                

                                x_cord=(((1+self.pos_to_arr(x))*(self.gap+self.diameter))-0.5*self.diameter+self.border)
                                y_cord=(self.n_col-i)*(self.gap+self.diameter)-0.5*self.diameter+self.border

                                self.Draw_Circle(x_cord,y_cord,next_number)
                                self.arr[self.pos_to_arr(x)][self.n_col-1-i]=next_number

                                break
  
                        if(temp!=-1 and self.Check_Win(next_number,self.pos_to_arr(x),self.n_col-1-temp)):
                            print(f"player{next_number} won the game")
                            self.Game_count+=1
                            running=False
                        elif (temp!=-1 and self.Check_Win(next_number,self.pos_to_arr(x),self.n_col-1-temp)==-1) :
                            running=False    
                            self.Game_count+=1
                            print("draw")
                        if check_if_drawn:
                            next_number=self.Change(next_number)

game = Connect_4( n_col=7, size_of_square=450,gap=4, Game_count=1,border=75,Mode='Classic')
game.Game_Start()
