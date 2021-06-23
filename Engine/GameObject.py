import pygame

class GameObject:
    compontents = []
    def __init__(self, sprite, x, y, sx, sy, r):
        self.sprite = sprite
        self.x = x
        self.y = y
        self.sx = sx
        self.sy = sy
        self.r = r
    def __repr__(self):
        return f"x : {self.x}, y : {self.y}, scale(x) : {self.sx}, scale(y) : {self.sy}, rotation : {self.r}"
    
    def get_drawable(self):
        return pygame.image.load(self.sprite)
    
    def addComponent(comp):
        components.append()