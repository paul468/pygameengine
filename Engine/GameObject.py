import pygame

class GameObject:
    components = []
    def __init__(self, sprite, x, y, sx, sy, r):
        self.sprite = sprite
        self.x = x
        self.y = y
        self.sx = sx
        self.sy = sy
        self.r = r
        self.img = pygame.image.load(self.sprite)
    def __repr__(self) -> str:
        return f"x : {self.x}, y : {self.y}, scale(x) : {self.sx}, scale(y) : {self.sy}, rotation : {self.r}"
    
    def get_drawable(self):
        return self.img
    
    def start(self):
        for i in self.components:
            i.start()
    
    def addComponent(self, comp):
        self.components.append(comp(self))
    
    def update(self, rate):
        for i in self.components:
            i.update(rate)