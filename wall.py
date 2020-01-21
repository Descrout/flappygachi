import pygame
from game import Game
from game import Rectangle
import random

class Wall:
    def __init__(self,img,x):
        self.img = img
        self.x = x
        self.spacing = 150
        self.width = 100
        self.reset()
    
    def reset(self):
        self.offset = random.randrange(-110,140,30)
        self.top = 200+self.offset
        self.bottom = 200+self.spacing+self.offset
        self.top_height = self.top
        self.bottom_height = Game.height - self.bottom
        self.imgt = pygame.transform.scale(self.img,(self.width,self.top_height))
        self.imgb = pygame.transform.scale(self.img,(self.width,self.bottom_height))
        self.collider_top = Rectangle(self.x,0,self.width,self.top)
        self.collider_bottom = Rectangle(self.x,self.bottom_height,self.width,self.bottom)

    def update(self):
        self.x -= 2
        self.collider_top.x = self.collider_bottom.x = self.x


    def draw(self,surface):
        surface.blit(self.imgt,(self.x,0))
        surface.blit(self.imgb,(self.x,self.bottom))