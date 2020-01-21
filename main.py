import pygame
from game import Game
from animation import Animation
from animation import AnimType
from wall import Wall

class Assets:
    def __init__(self):
        self.gachiBASS = pygame.image.load("data/gachiBASS.png")
        self.gachiBASS = pygame.transform.scale(self.gachiBASS,(280,112))

        self.nolyuolan = pygame.image.load("data/nolyuolan.png")

class FlappyGachi(Game):
    def setup(self):
        super().setup()
        #setup code goes here
        self.assets = Assets()
        self.gachi = Animation(self.assets.gachiBASS,56,56)
        self.testWall = Wall(self.assets.nolyuolan,200)
        
    def update(self):
        self.gachi.update(self.dt)
        

    def draw(self):
        self.surface.fill((0,0,0))
        self.gachi.show(self.surface,100,100)
        self.testWall.draw(self.surface)
        

    def dispose(self):
        #dispose code goes here
        super().dispose()

if __name__ == "__main__" :
    app = FlappyGachi(800,600,60,"Flappy Gachi")
    app.execute()