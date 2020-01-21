import pygame
from game import Game

class FlappyGachi(Game):
    def setup(self):
        super().setup()
        #setup code goes here
        
    def update(self):
        print(self.dt)
        pass

    def draw(self):
        pass

    def dispose(self):
        #dispose code goes here
        super().dispose()

if __name__ == "__main__" :
    app = FlappyGachi(caption="Flappy Gachi")
    app.execute()