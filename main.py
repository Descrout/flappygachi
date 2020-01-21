import pygame
from game import Game
from gachi import Gachi
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
        self.walls = [Wall(self.assets.nolyuolan,600+(i*500)) for i in range(3)]

        self.gachi = Gachi(self.assets.gachiBASS,250,Game.height / 2)

        
    def update(self):
        self.gachi.update(self.dt)
        for wall in self.walls:
            wall.update()
        for i in range(len(self.walls)):
            if self.walls[i].x + self.walls[i].width < 250:
                self.walls.append(self.walls.pop(i))


    def mouse_down(self):
        self.gachi.jump()

    def draw(self):
        self.surface.fill((128,187,255))        
        for wall in self.walls:
            wall.draw(self.surface)
        self.gachi.draw(self.surface)
        

    def dispose(self):
        #dispose code goes here
        super().dispose()

if __name__ == "__main__" :
    app = FlappyGachi(800,600,60,"Flappy Gachi")
    app.execute()