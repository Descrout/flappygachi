import pygame

class Rectangle:
    def __init__(self,x,y,w,h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
    
    def intersect(self,other):
        return (self.x + self.w > other.x and self.x < other.x + other.w and
        self.y + self.h > other.y and self.y < other.y + other.h)

class Game:
    width = 640
    height = 480
    
    def __init__(self,w=640,h=480,fps=60,caption="Game"):
        self._running = True
        self.surface = None
        self.dt = 0
        self.clock = None
        self.FPS = fps
        self.size =  Game.width, Game.height = w, h
        self.caption = caption
 
    def setup(self):
        pygame.init()
        self.surface = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        pygame.display.set_caption(self.caption)
        self.clock = pygame.time.Clock()
        self._running = True
 
    def mouse_down(self):
        pass

    def key_down(self,key):
        pass

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            self.mouse_down()
        elif event.type == pygame.KEYDOWN:
            self.key_down(event.key)
    
    def update(self):
        pass

    def draw(self):
        pass

    def dispose(self):
        pygame.quit()
        quit()
 
    def execute(self):
        if self.setup() == False:
            self._running = False

        while( self._running ):
            for event in pygame.event.get():
                self.handle_event(event)
            self.update()
            self.draw()
            pygame.display.update()
            self.dt = self.clock.tick(self.FPS) / 1000
        self.dispose()
 