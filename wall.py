import pygame
from game import Game

class Wall:
    def __init__(self,img,x):
        self.img = img
        self.x = x
        self.spacing = 100
        self.width = 60
        self.y_pos = 100
        self.top = 200+self.y_pos
        self.bottom = 200+self.spacing+self.y_pos
        self.top_height = self.top
        self.bottom_height = Game.height - self.bottom
    
    def draw(self,surface):
        surface.blit(pygame.transform.scale(self.img,(self.width,self.top_height)),(self.x,0))
        surface.blit(pygame.transform.scale(self.img,(self.width,self.bottom_height)),(self.x,self.bottom))