import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 400))


def background():
    # Фон
    # Лазурная часть
    polygon(screen, (114, 237, 252), [(0, 0), (0, 170), (600, 170), (600, 0)])
    # Голубая часть
    polygon(screen, (0, 72, 252), [(0, 170), (0, 290), (600, 290), (600, 170)])
    # Желтая часть
    polygon(screen, (251, 252, 11), [(0, 290), (0, 400), (600, 400), (600, 290)])



def umbrella():
    # Зонтик
    polygon(screen, (127, 43, 10), [(120, 240), (120, 380), (125, 380), (125, 240)])  # Мачта
    polygon(screen, (127, 43, 10), [(120, 240), (60, 270), (180, 270), (125, 240)])  # Зонт
    polygon(screen, (0, 0, 0), [(120, 240), (60, 270), (180, 270), (125, 240)], 1)
    for x in range(60, 120, 15):
        line(screen, (0, 0, 0), (120, 240), (x, 270), 1)  # полосы на зонте
        line(screen, (0, 0, 0), (125, 240), (x + 65, 270), 1)  # полосы на зонте


def boat():
    #  Лодка
    circle(screen, (127, 43, 10), (330, 200), 40, draw_bottom_left=True)  # Корма
    circle(screen, (76, 43, 10), (330, 200), 40, 2, draw_bottom_left=True)  # Корма
    polygon(screen, (127, 43, 10), [(330, 200), (330, 240), (500, 240), (500, 200)])  # Основная часть
    polygon(screen, (76, 43, 10), [(330, 200), (330, 240), (500, 240), (500, 200)], 1)  # Основная часть
    polygon(screen, (127, 43, 10), [(500, 200), (500, 240), (560, 200), (560, 200)])  # Нос
    polygon(screen, (76, 43, 10), [(500, 200), (500, 240), (560, 200), (560, 200)], 1)  # Нос
    polygon(screen, (0, 0, 0), [(400, 100), (400, 200), (405, 200), (405, 100)])  # Мачта

    polygon(screen, (179, 157, 24), [(405, 100), (420, 150), (470, 150), (405, 100)])  # Парус верх
    polygon(screen, (0, 0, 0), [(405, 100), (420, 150), (470, 150), (405, 100)], 1)  # Парус верх
    polygon(screen, (179, 157, 24), [(405, 200), (420, 150), (470, 150), (405, 200)])  # Парус низ
    polygon(screen, (0, 0, 0), [(405, 200), (420, 150), (470, 150), (405, 200)], 1)  # Парус низ
    circle(screen, (255, 255, 255), (515, 215), 10)  # Иллюминатор
    circle(screen, (0, 0, 0), (515, 215), 10, 3)  # Иллюминатор


def sun(x, y):
    # Солнце
    circle(screen, (251, 252, 11), (x, y), 45)


def clouds():
    # Облака
    # Облака
    for x in range(140, 200, 20):
        circle(screen, (0, 0, 0), (x, 50), 18, 1)
        circle(screen, (255, 255, 255), (x, 50), 17)
    for x in range(120, 200, 20):
        circle(screen, (0, 0, 0), (x, 70), 18, 1)
        circle(screen, (255, 255, 255), (x, 70), 17)


def waves():
    #  Волны на песке
    #  Желтые
    for x in range(20, 600, 100):
        circle(screen, (251, 252, 11), (x, 310), 35)
    # Синие
    for x in range(70, 600, 100):
        circle(screen, (0, 72, 252), (x, 260), 35)


# Фон
background()
#  Волны на песке
waves()
#  Солнце
sun(520, 70)
# Облака
clouds()
# Лодка
boat()
# Зонтик
umbrella()

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
