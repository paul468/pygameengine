import pygame, sys
import Engine.GameObject

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

def new_win(width, height, win):
    win = pygame.display.set_mode((width, height))
    root["r"] = win

@update
def updoot(rate):
    print(rate)

@exit_func
def leave():
    sys.exit()
pygame.init()

def add_gameobject(go:Engine.GameObject.GameObject):
    render_queue.append([go.get_drawable(), go.x, go.y, go.sx, go.sy, go.r])

def main():
    
    while True:
        root["r"].fill()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                for i in exits:
                    i()
        for i in render_queue:
            root.blit(i)
        for i in updates:
            i(rate)
        
        pygame.display.flip()
