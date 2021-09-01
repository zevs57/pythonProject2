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
    global x, y, r, color
    r = randint(30, 50)
    x = randint(0 + r, 700)
    y = randint(0 + r, 500)
    color = COLORS[randint(0, 5)]


def click(event):
    """
    По клику мыши вычисляется (по теореме Пифагора) попали ли мы в шарик
    :param event:
    :return: Возвращает True, если было попадание в шарик
    """
    if (event.pos[1] - y) ** 2 + (event.pos[0] - x) ** 2 <= r ** 2:
        return True


pygame.display.update()
clock = pygame.time.Clock()
finished = False

new_ball()
points = 0

rect_change_x = randint(10, 50)  # Вектор скорости и направления
rect_change_y = randint(10, 50)
while not finished:
    clock.tick(FPS)
    x += rect_change_x
    y += rect_change_y
    circle(screen, color, (x, y), r)
    if y > 900 - r or y < 0 + r:  # Смена направления после удара о границу
        rect_change_y += randint(10, 50)
        rect_change_y = rect_change_y * -1
    if x > 1200 - r or x < 0 + r:  # Смена направления после удара о границу
        rect_change_x += randint(10, 50)
        rect_change_x = rect_change_x * -1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if click(event):  # Посчет очков
                points = points + 1

    pygame.display.update()
    screen.fill(BLACK)

print("Вы набрали " + str(points) + " очков")  # Вывод количества очков
pygame.quit()
