import pygame, sys


updates = []
exits = []


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

def new_win(width, height):
    return pygame.display.set_mode((width, height))

@update
def updoot(rate):
    print(rate)

@exit_func
def leave():
    sys.exit()
pygame.init()

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                for i in exits:
                    i()
        for i in updates:
            i(rate)
        pygame.display.flip()
