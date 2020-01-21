from animation import Animation
from animation import AnimType

class Gachi:
    gravity = .7
    def __init__(self,img,x,y):
        self.anim = Animation(img,56,56)
        self.anim.anim_type = AnimType.REPEAT
        self.x = x
        self.y = y
        self.vel_y = 0

    def jump(self):
        self.vel_y = -9

    def update(self,dt):
        self.anim.update(dt)
        self.vel_y += Gachi.gravity
        self.y += self.vel_y

    def draw(self,surface):
        self.anim.show(surface,self.x,self.y)