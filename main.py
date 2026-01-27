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
class Lable(Area):
    def set_text(self,text,fsize=12,textcolor=(0,0,0)):


