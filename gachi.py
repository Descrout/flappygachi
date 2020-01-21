from animation import Animation
from animation import AnimType
from game import Rectangle
from game import Game
import pygame

class Gachi:
    gravity = .7
    def __init__(self,img,x,y,w,h):
        self.w = w
        self.h = h
        self.anim = Animation(img,w,h)
        self.anim.anim_type = AnimType.REPEAT
        self.x = x
        self.y = y
        self.vel_y = 0
        self.collider = Rectangle(x,y,w,h)

    def jump(self):
        self.vel_y = -9

    def update(self,dt,wall):
        self.anim.update(dt)
        self.vel_y += Gachi.gravity
        self.y += self.vel_y
        self.collider.x = self.x
        self.collider.y = self.y

        if self.collider.intersect(wall.collider_top) or self.collider.intersect(wall.collider_bottom) or self.y+self.h > Game.height:
            print("collide")


    def draw(self,surface):
        self.anim.show(surface,self.x,self.y)