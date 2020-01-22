import pygame
from game import Game
from gachi import Gachi
from wall import Wall
from neuroevolution import Genetics

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
        self.gachis = [Gachi(self.assets.gachiBASS) for i in range(30)]
        self.dead_gachis = []
        self.epoch = 1
        
    def update(self):
        for _ in range(self.epoch):
            for gachi in self.gachis:
                gachi.update(self.dt,self.walls[0])
            
            for i,gachi in enumerate(self.gachis):
                if not gachi.alive:
                    self.dead_gachis.append(self.gachis.pop(i))
            
            if not self.gachis:
                self.walls = [Wall(self.assets.nolyuolan,600+(i*500)) for i in range(3)]
                Genetics.next_generation(self)

            for wall in self.walls:
                wall.update()
                
            for i in range(len(self.walls)):
                tWall = self.walls[i]
                right_side = tWall.x + tWall.width

                if right_side < 0:
                    tWall.reset()
                    tWall.x = self.walls[-2].x + 500
                elif right_side < 215:
                    self.walls.append(self.walls.pop(i))

    def key_down(self,key):
        if key == pygame.K_RIGHT:
            self.epoch += 1
        if key == pygame.K_LEFT:
            self.epoch -= 1

    def draw(self):
        self.surface.fill((128,187,255))        
        for wall in self.walls:
            wall.draw(self.surface)
        
        for gachi in self.gachis:
            gachi.draw(self.surface)



if __name__ == "__main__" :
    app = FlappyGachi(800,600,60,"Flappy Gachi")
    app.execute()