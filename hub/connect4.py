import pygame
import numpy as np
import math
pygame.init()
class Connect_4:
    def __init__(self,n_col,size_of_square,gap,Game_count,Winning_Size,border,Player1,Player2):

        self.n_col= n_col                       # n_col is number of columns and rows on the boards
        self.arr=np.zeros((n_col,n_col)).astype(int)           # arr represnt the board as a 10X10 array ( intially this is zero array) its int coz i have used string thing in checking winning condition
        self.size_of_square= size_of_square           # how big will the size of grid in pixels
        self.diameter=(self.size_of_square-((n_col+1)*gap))/n_col
        self.gap=gap 
        self.Game_count=Game_count      # Game_count is the count of the game number going on
        self.screen = pygame.display.set_mode((self.size_of_square+2*border,self.size_of_square+1.5*border))
        self.border=border # offset from screen
        self.Winning_Size=Winning_Size  # its 4 but we can change 
        self.Player1=Player1
        self.Player2=Player2        
        self.background_color = (18,18,18)
        self.empty_circle_color = (42,42,42)
        self.p1_color = (0, 229, 255)
        self.p2_color = (255, 46, 99)
        self.winner=Player1
        self.loser=Player2

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


    def Change(self,next_number):  #change 1 to 2 and vice-versa
        if next_number==1:
            return 2
        else:
            return 1  
 

    def Check_is_in(self,main_arr,arr2check): #converts the numpay arr [1-D] into string and then use a in b for string 
        
        string1=main_arr.astype(str)
        string2=arr2check.astype(str)
        a1=''.join(string1) 
        a2=''.join(string2)
        return a2 in a1
    
    def Check_win(self,chance,i,j):             #Main function to check win condition
        
        arr_temp=np.full(self.Winning_Size,chance)
        arr_copy=self.arr.copy()
        arr_hori=arr_copy[i]  #extracts the horizontal arr containing [i][j]
        arr_vert=arr_copy[:,j] #extracts the vertical arr containing [i][j]

        #extract the whole diagonal / containing the element (i,j) by slicing (first we find out the extreme two cells of arr [a1][b1] and [c1][d1] and then use slicing on flattened array)

        a1=max(i-(self.n_col-1-j),0)
        b1=min(self.n_col-1,j+i)
        c1=min(self.n_col-1,i+j)
        d1=max(j-(self.n_col-1-i),0)
        arr_dia1=arr_copy.flatten()[a1*self.n_col+b1:(c1*self.n_col+d1)+1:self.n_col-1] 

        #extract whole diagonal \ containing the element (i,j) by slicing (first we find out the extreme two cells of arr [a1][b1] and [c1][d1] and then use slicing on flattened array)

        a2=max(i-j,0)
        b2=max(j-i,0)
        c2=min(i+self.n_col-1-j,self.n_col-1)
        d2=min(j+self.n_col-1-i,self.n_col-1)
        arr_dia2=arr_copy.flatten()[a2*self.n_col+b2:(c2*self.n_col+d2)+1:self.n_col+1]

        return (self.Check_is_in(arr_hori,arr_temp) or self.Check_is_in(arr_vert,arr_temp) or self.Check_is_in(arr_dia1,arr_temp) or self.Check_is_in(arr_dia2,arr_temp))

    def Check_Draw(self):
        return self.arr.all()       
      
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
        if(nn==1):
                while y0<(y-self.border):
                    self.Redraw()
                    pygame.draw.circle(self.screen,self.p1_color,(x,y1),self.diameter/2)
                    pygame.draw.circle(self.screen,self.p1_color,(x,y1),self.diameter/2,2)
                    pygame.display.update()
                    y0+=speed_factor*(y-self.border)
                    y1=self.border+(y-self.border)*((math.sin(math.pi*0.5*y0/(y-self.border)))**jerk_factor)
                    clock.tick(100)
                
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
                    clock.tick(100)

                self.Redraw()
                pygame.draw.circle(self.screen,self.p2_color,(x,y),self.diameter/2)
                pygame.draw.circle(self.screen,self.p2_color,(x,y),self.diameter/2,2)
                pygame.display.update()    
    
    def Winner_Found(self,k):
        font=pygame.font.Font(None,40)
        x_cord=int((2*self.border+self.size_of_square)/2-(self.size_of_square/3))
        y_cord=int((2*self.border+self.size_of_square)/2-(self.size_of_square/3))
        height=int(self.size_of_square/2)
        wid=int(self.size_of_square/1.5)

        Rec=pygame.draw.rect(self.screen,(25,25,25),(x_cord,y_cord,wid,height))
        pygame.draw.rect(self.screen,(255,255,255),(x_cord,y_cord,wid,height),5)
        if k==0:
            stat=font.render(f"DRAW",True,(0, 180, 255))
            r1=stat.get_rect(center=(Rec.x+int(Rec.width/2),Rec.y+100))
            self.screen.blit(stat,r1)

        else:            
            if k==1:
                self.winner=self.Player1
                self.loser=self.Player2
                stat=font.render(f"{self.Player1} WINS",True,(0, 255, 180))
                stat1=font.render(f"{self.Player2} LOSES",True,(255, 50, 80))

            else:
                self.winner=self.Player2
                self.loser=self.Player1
                stat=font.render(f"{self.Player2} WINS",True,(0, 255, 180))
                stat1=font.render(f"{self.Player1} LOSES",True,(255, 50, 80))

            r1=stat.get_rect(center=(Rec.x+int(Rec.width/2),Rec.y+40))
            r2=stat1.get_rect(center=(Rec.x+int(Rec.width/2),Rec.y+80))

            self.screen.blit(stat,r1)
            self.screen.blit(stat1,r2)

        font2=pygame.font.Font(None,50)
        restart=font2.render("RESTART",True,(0, 255, 180))
        quit=font2.render("HOME PAGE",True,(255, 60, 100))

        r3=restart.get_rect(center=(Rec.x+int(Rec.width/2),Rec.y+Rec.height-80))
        r4=quit.get_rect(center=(Rec.x+int(Rec.width/2),Rec.y+Rec.height-40))

        #self.screen.blit(restart,r3)
        self.screen.blit(quit,r4)
        pygame.display.update()

        return r3,r4      
         

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
                                temp=i #value of i for which the last circle is empty n_col-i-1 gives us the excat j value in arr[i][j] if its -1 then it means the move wasn't valid ie the coloumn is already filled
                                check_if_drawn=True
                                

                                x_cord=(((1+self.pos_to_arr(x))*(self.gap+self.diameter))-0.5*self.diameter+self.border)
                                y_cord=(self.n_col-i)*(self.gap+self.diameter)-0.5*self.diameter+self.border

                                self.Draw_Circle(x_cord,y_cord,next_number)
                                self.arr[self.pos_to_arr(x)][self.n_col-1-i]=next_number
                                               
                                break
                        
                        if(temp!=-1 and (self.Check_win(next_number,self.pos_to_arr(x),self.n_col-1-temp)==True) or self.Check_Draw()):
                            
                            if self.Check_Draw():
                                next_number=0
                            restart,quit = self.Winner_Found(next_number)
                            wait=True
                            while wait:
                                for events in pygame.event.get():
                                    if events.type==pygame.MOUSEBUTTONDOWN:
                                        x,y= events.pos
                                        if x>restart.x and x<restart.x+restart.width and y >restart.y and y< restart.y+restart.height :
                                            self.Game_count+=1
                                            self.arr = np.zeros((self.n_col, self.n_col),dtype=int)
                                            self.Grid_Set()
                                            pygame.display.update()
                                            next_number=1
                                            wait=False
                                            break
                                        elif x>quit.x and x<quit.x+quit.width and y>quit.y and y< quit.y+quit.height:                                 
                                            running=False
                                            wait=False
                                    elif events.type == pygame.QUIT:
                                        running = False
                                        wait = False
 

                        if check_if_drawn:
                            next_number=self.Change(next_number)
