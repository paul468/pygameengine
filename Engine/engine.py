import pygame, sys
from Engine.GameObject import GameObject

updates = []
exits = []
root = {}
gameobjects = []
path = sys.path[0]
print(path)
def update(func):
    updates.append(func)

def exit_func(func):
    exits.append(func)

rate = 1/60

class Component(object):

    def __init__(self, parent):
        self.parent = parent
    
    def update(self, rate):
        pass

    def start(self):
        pass

def delete_default_update():
    for i in updates:
        if i.__name__ == "updoot":
            updates.remove(i)
def set_fps(fps):
    rate = fps

clock = pygame.time.Clock()

def new_win(width, height, win, col):
    win = pygame.display.set_mode((width, height))
    root["r"] = win
    root["c"] = col

def add_gameobject(go:GameObject):
    gameobjects.append(go)


def new_object(path_to_sprite, x,y,sx,sy,r):
    new = GameObject(path_to_sprite, x, y, sx, sy, r)
    add_gameobject(new)
    return new

@update
def updoot(rate):
    for i in gameobjects:
        i.update(rate)

@exit_func
def leave():
    sys.exit()
pygame.init()


def main():
    for i in gameobjects:
        i.start()
    while True:
        root["r"].fill((root["c"]))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                for i in exits:
                    i()
        for i in gameobjects:
            root["r"].blit(i.get_drawable(), i.get_drawable().get_rect().move(i.x,i.y))
        for i in updates:
            i(rate)
        
        pygame.display.flip()
