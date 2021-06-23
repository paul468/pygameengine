import pygame, sys
from Engine.GameObject import GameObject

updates = []
exits = []
render_queue = []
root = {}

path = sys.path[0]
print(path)
def update(func):
    updates.append(func)

def exit_func(func):
    exits.append(func)

rate = 1/60

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
    render_queue.append([go.get_drawable(), go.x, go.y, go.sx, go.sy, go.r]) 


def new_object(path_to_sprite, x,y,sx,sy,r):
    new = GameObject(path_to_sprite, x, y, sx, sy, r)
    add_gameobject(new)
    return new

@update
def updoot(rate):
    print(rate)

@exit_func
def leave():
    sys.exit()
pygame.init()


def main():
    
    while True:
        root["r"].fill((root["c"]))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                for i in exits:
                    i()
        for i in render_queue:
            root["r"].blit(i[0], i[0].get_rect())
        for i in updates:
            i(rate)
        
        pygame.display.flip()
