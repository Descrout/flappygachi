from animation import Animation
from animation import AnimType
from game import Rectangle
from game import Game
from neuroevolution import NeuralNetwork

class Gachi:
    gravity = .7
    def __init__(self,img):
        self.w = 56
        self.h = 56
        self.anim = Animation(img,self.w,self.h)
        self.anim.anim_type = AnimType.REPEAT
        self.x = 250
        self.brain = NeuralNetwork((4,4,1))
        self.y = Game.height / 2
        self.vel_y = 0
        self.collider = Rectangle(self.x,self.y,self.w,self.h)
        self.score = 0
        self.fitness = 0
        self.alive = True

    def think(self,wall):
        prediction = self.brain.predict([[self.y],[self.vel_y],[wall.x],[wall.top]])
        if prediction[0][0] > 0.5:
            self.jump()

    def jump(self):
        self.vel_y = -9

    def update(self,dt,wall):
        self.anim.update(dt)
        self.vel_y += Gachi.gravity
        self.y += self.vel_y
        self.collider.x = self.x
        self.collider.y = self.y
        self.score += 50
        self.think(wall)

        if self.collider.intersect(wall.collider_top) or self.collider.intersect(wall.collider_bottom) or self.y+self.h > Game.height or self.y<0:
            self.alive = False

    def draw(self,surface):
        self.anim.show(surface,self.x,self.y)