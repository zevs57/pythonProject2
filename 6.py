import pygame
from pygame.draw import *
from random import randint

pygame.init()

FPS = 2
screen = pygame.display.set_mode((1200, 900))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


def new_ball():
    '''рисует новый шарик '''
    global x, y, r
    x = randint(100, 700)
    y = randint(100, 500)
    r = randint(30, 50)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)


def click(event):
    """
    По клику мыши вычисляется (по теореме Пифагора) попали ли мы в шарик
    :param event:
    :return:
    """
    if (event.pos[1] - y) ** 2 + (event.pos[0] - x) ** 2 <= r ** 2:
        return True


pygame.display.update()
clock = pygame.time.Clock()
finished = False

points = 0

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if click(event):  # Посчет очков
                points = points + 1

    new_ball()
    pygame.display.update()
    screen.fill(BLACK)

print("Вы набрали " + str(points) + " очков")  # Вывод количества очков
pygame.quit()
