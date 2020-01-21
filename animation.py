import pygame
import math
from enum import Enum

class AnimType(Enum):
    ONCE = 1
    REPEAT = 2
    #PINGPONG = 3 TODO

class Animation:
    def __init__(self,img,single_w,single_h):
        self.img = img
        self.single_w = single_w
        self.single_h = single_h
        self.img_rect = img.get_rect()
        self.w_img_count = int(self.img_rect.width / single_w)
        self.h_img_count = int(self.img_rect.height / single_h)
        self.maxFrame = (self.w_img_count * self.h_img_count)-1
        self.frame = 0
        self.timer = 0.0
        self.speed = 1.0
        self.anim_type = AnimType.REPEAT

    
    def restart(self):
        self.frame = 0
        self.timer = 0

    def update(self,dt):
        if self.timer <= self.speed:
            self.timer += dt*1000
            if self.frame < self.maxFrame:
                self.frame += 1
            else:
                if self.anim_type == AnimType.REPEAT:
                    self.frame = 0
        else:
            self.timer = 0
            

    def show(self,surface,x,y):
        surface.blit(self.img,(x,y),(self.single_w*(self.frame%self.w_img_count),self.single_h*(math.floor(self.frame/self.w_img_count)),self.single_w,self.single_h))