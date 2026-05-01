import pygame
import numpy as np
pygame.init()
class Tic_Tac_Toe:
def __init__(self,thickness,n_col,size_of_square,Game_count,Winning_Size,border,Player1="kirti",Player2="guru",Chaos=True):

self.thickness=thickness # thickness is the thickness of line, width is the side of each of the 100 squares on the grid
self.n_col= n_col # n_col is number of columns and rows on the boards
self.arr=np.zeros((n_col,n_col)).astype(int) # arr represnt the board as a 10X10 array ( intially this is zero array)
self.size_of_square= size_of_square # how big will the size of grid in pixels
self.width=(size_of_square-(thickness*(n_col+1)))/(n_col) # length of the side of each of 100 squares in 10X10 grid
self.Game_count=Game_count # Game_count is the count of the game number going on
self.Winning_Size=Winning_Size # Allows you to change wining condition 5 in row 4 in row etc
self.screen = pygame.display.set_mode((self.size_of_square+(2*border),self.size_of_square+(2*border)))
self.border=border
self.Player1=Player1
self.Player2=Player2
self.winner =Player1
self.loser=Player2


def pos_to_arr(self,x): #function which takes x and y co-ordinates as input and tells us index in arr of that particular square
i=1
x-=self.border
while i < self.n_col-1:
if( (x >= (i*self.width)+(2*i+1)*self.thickness/2) and (x < (i+1)*(self.width)+(2*i+3)*(self.thickness/2)) ):
return i
else:
i+=1
if ( x >=0 and x < self.width+(1.5*self.thickness) ):
return 0
if ( x >= ((self.n_col-0.5)*self.thickness + (self.n_col-1)*self.width) ):
return self.n_col-1

def Check_is_in(self,main_arr,arr2check): #converts the numpay arr [1-D] into string and then use a in b for string
 
string1=main_arr.astype(str)
string2=arr2check.astype(str)
a1=''.join(string1)
a2=''.join(string2)
return a2 in a1
 
def Check_win(self,chance,i,j):
 
arr_temp=np.full(self.Winning_Size,chance)
arr_copy=self.arr.copy()
arr_hori=arr_copy[i]
arr_vert=arr_copy[:,j]

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


def Winner_Found(self,k):
 
font=pygame.font.Font(None,40)
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

x_cord=int((2*self.border+self.size_of_square)/2-(self.size_of_square/3))
y_cord=int((2*self.border+self.size_of_square)/2-(self.size_of_square/3))
height=int(self.size_of_square/2)
wid=int(self.size_of_square/1.5)

Rec=pygame.draw.rect(self.screen,(25,25,25),(x_cord,y_cord,wid,height))
pygame.draw.rect(self.screen,(255,255,255),(x_cord,y_cord,wid,height),5)

r1=stat.get_rect(center=(Rec.x+int(Rec.width/2),Rec.y+40))
r2=stat1.get_rect(center=(Rec.x+int(Rec.width/2),Rec.y+80))

self.screen.blit(stat,r1)
self.screen.blit(stat1,r2)

font2=pygame.font.Font(None,50)
restart=font2.render("RESTART",True,(0, 255, 180))
quit=font2.render("HOME PAGE",True,(255, 60, 100))

r3=restart.get_rect(center=(Rec.x+int(Rec.width/2),Rec.y+Rec.height-80))
r4=quit.get_rect(center=(Rec.x+int(Rec.width/2),Rec.y+Rec.height-40))

#self.screen.blit(restart,r3) this is removed
self.screen.blit(quit,r4)
pygame.display.update()

return r3,r4
 
def Set_Grid(self):
self.screen.fill((18,18,18))
x=self.border+self.width+self.thickness
while x <= self.size_of_square+self.border-self.width-self.thickness:
pygame.draw.line(self.screen,(70,70,70),(x,self.border),(x,self.size_of_square+self.border),self.thickness)
pygame.draw.line(self.screen,(70,70,70),(self.border,x),(self.size_of_square+self.border,x),self.thickness)
x+=(self.width+self.thickness)
pygame.display.update()

# Main Function
def Game_Start(self):

self.Set_Grid()
next_number=1 # this is the variable which tells what to mark on the grid right after next click 1 represent 'O' 2 represent 'X'
#Main Loop
running=True
game_over=False
while running:

for event in pygame.event.get():
if event.type == pygame.QUIT:
running = False

elif event.type==pygame.MOUSEBUTTONDOWN and not(game_over): # detecting any mouse click on the grid
if event.button==1:
x,y = event.pos
if( x<=self.border or x>=self.size_of_square+self.border or y<=self.border or y>=self.size_of_square+self.border):
continue
X,Y=self.pos_to_arr(x),self.pos_to_arr(y)
if self.arr[X][Y]==0 :
self.arr[X][Y]=next_number
else:
continue
font = pygame.font.SysFont("calibri",85)
if next_number==1:
pygame.draw.circle(self.screen,(255,255,255),(((X+1)*self.thickness)+((X+0.5)*self.width)+self.border,((Y+1)*self.thickness)+((Y+0.5)*self.width)+self.border),(self.width/2)-1,5)
 
else:
text = font.render("X",True,(255,255,255))
self.screen.blit(text,(((X+1)*self.thickness)+self.border+((X)*self.width)+8,((Y+1)*self.thickness)+self.border+((Y)*self.width)-7))
pygame.display.update()
winner=self.Check_win(next_number,X,Y)
if winner:
restart,quit = self.Winner_Found(next_number)
wait=True
while wait:
for events in pygame.event.get():
if events.type==pygame.MOUSEBUTTONDOWN:
x,y= events.pos
if x>restart.x and x<restart.x+restart.width and y >restart.y and y< restart.y+restart.height :
self.Game_count+=1
self.arr = np.zeros((self.n_col, self.n_col),dtype=int)
self.Set_Grid()
next_number=1
wait=False
break
elif x>quit.x and x<quit.x+quit.width and y>quit.y and y< quit.y+quit.height:
running=False
wait=False
elif events.type == pygame.QUIT:
running = False
wait = False

else:
next_number=3-next_number