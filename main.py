import time
from random import randint
import pygame
YELLOW=(255,255,0)
DARK_BLUE=(0,0,100)
BLUE=(80,80,255)
RED=(255,0,0)
GREEN=(0,255,0)
back = (200,255,255)
pygame.init()
window=pygame.display.set_mode((500,500))
window.fill(back)
clock= pygame.time.Clock()
class Area():
    def __init__(self,x=0,y=0,width=10,height=10,color=None):
        self.rect=pygame.Rect(x,y,width,height)
        self.color=color
    def set_color(self,newcolor):
        self.color=newcolor
    def fill(self):
        pygame.draw.rect(window,self.color,self.rect)
    def outline(self,frame_color,thickness):
        pygame.draw.rect(window,frame_color,self.rect,thickness)
    def collide_point(self,x,y):
        return self.rect.collidepoint(x,y)
class Lable(Area):
    def set_text(self,text,fsize=12,textcolor=(0,0,0)):
        self.image=pygame.font.SysFont("verdana",fsize).render(text,True,textcolor)
    def draw(self,shift_x=0,shift_y=0):
        self.fill()
        window.blit(self.image,(self.rect.x+shift_x,self.rect.y+shift_y))
numkards=4
cards=[]
x=70
time_text=Lable(0,0,50,50,back)
time_text.set_text("Bремя:",30,DARK_BLUE)
time_text.draw(20,20)

timer=Lable(50,55,50,40,back)
timer.set_text("0",30,DARK_BLUE)
timer.draw(0,0)

score_text=Lable(380,0,50,50,back)
score_text.set_text("Cчёт:",30,DARK_BLUE)
score_text.draw(20,20)

score=Lable(430,55,50,40,back)
score.set_text("0",30,DARK_BLUE)
score.draw(0,0)

start_time=time.time()
cur_time=start_time
for i in range(numkards):
    newcard=Lable(x,170,70,100,YELLOW)
    newcard.outline(RED,10)
    newcard.set_text("click",23,GREEN)
    cards.append(newcard)
    x+=100
run=True
poins=0
wait=0
while run:
    # window.fill(back)
    if wait==0:
        wait=20
        click=randint(0,numkards-1)
        for i in range(numkards):
            cards[i].set_color(YELLOW)
            if i == click:
                cards[i].draw(10,30)
                cards[i].outline(DARK_BLUE,10)
            else:
                cards[i].fill()
                cards[i].outline(DARK_BLUE,10)
    else:
        wait-=1
    # for cardraw in cards:
    #     cardraw.draw(10, 30)
    #     cardraw.outline(RED, 10)
    for event in pygame.event.get():
        if event.type==pygame.MOUSEBUTTONDOWN and event.button == 1:
            x,y=event.pos
            for i in range(numkards):
                if cards[i].collide_point(x,y):
                    if i ==click:
                        cards[i].set_color(GREEN)
                        poins += 1
                    else:
                        cards[i].set_color(RED)
                        poins -= 1
                    cards[i].fill()
                    score.set_text(str(poins),40,DARK_BLUE)
                    score.draw(0,0)
        if event.type==pygame.QUIT:
            run=False
    new_time=time.time()
    if int(new_time)-int(cur_time)==1:
        timer.set_text(str(int(new_time-start_time)),40,DARK_BLUE)
        timer.draw()
        cur_time=new_time
    pygame.display.update()
    clock.tick(40)
