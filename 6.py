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


def new_ball1():
    '''рисует новый шарик '''
    global x1, y1, r1, color1
    r1 = randint(30, 50)
    x1 = randint(0 + r1, 700)
    y1 = randint(0 + r1, 500)
    color1 = COLORS[randint(0, 5)]


def new_ball2():
    '''рисует новую мишень '''
    global x2, y2, r2, color2
    r2 = randint(30, 50)
    x2 = randint(0 + r2, 700)
    y2 = randint(0 + r2, 500)
    color2 = COLORS[randint(0, 5)]


def click1(event):
    """
    По клику мыши вычисляется (по теореме Пифагора) попали ли мы в шарик
    :param event:
    :return: Возвращает True, если было попадание в шарик
    """
    if (event.pos[1] - y1) ** 2 + (event.pos[0] - x1) ** 2 <= r1 ** 2:
        sound2.play()
        return True


def click2(event):
    """
    По клику мыши вычисляется (по теореме Пифагора) попали ли мы в квадрат
    :param event:
    :return: Возвращает True, если было попадание в квадрат
    """
    if (event.pos[1] - y2) ** 2 + (event.pos[0] - x2) ** 2 <= r2 ** 2:
        sound1.play()
        return True


def text(str):
    """
    Функция выводит количество набраных очков на экране во время игры
    :param str:
    :return:
    """
    font = pygame.font.Font(None, 50)
    text = font.render(str, False, (100, 255, 100))
    text_x = 800
    text_y = 20
    text_w = 150
    text_h = 30
    screen.blit(text, (text_x, text_y))
    pygame.draw.rect(screen, (0, 255, 0), (text_x - 10, text_y - 10,
                                           text_w + 20, text_h + 20), 1)


# Музыка и звуки
pygame.mixer.music.load('data/house_lo.ogg')
pygame.mixer.music.play(-1)

sound1 = pygame.mixer.Sound('data/boom.wav')
sound2 = pygame.mixer.Sound('punch.wav')

pygame.display.update()
clock = pygame.time.Clock()
finished = False

new_ball1()
new_ball2()
points = 0

rect_change_x1 = randint(10, 50)  # Вектор скорости и направления шара 1
rect_change_y1 = randint(10, 50)
rect_change_x2 = randint(10, 50)  # Вектор скорости и направления шара2
rect_change_y2 = randint(10, 50)

while not finished:
    clock.tick(FPS)
    # Движение шарика 1
    x1 += rect_change_x1
    y1 += rect_change_y1
    circle(screen, color1, (x1, y1), r1)
    if y1 > 900 - 2 * r1 or y1 < 0 + 2 * r1:  # Смена направления после удара о границу
        rect_change_y1 = rect_change_y1 * -1

    if x1 > 1200 - 2 * r1 or x1 < 0 + 2 * r1:  # Смена направления после удара о границу
        rect_change_x1 = rect_change_x1 * -1

    # Движение мишени 2
    x2 += rect_change_x2
    y2 += rect_change_y2
    polygon(screen, color2, [(x2 - r2, y2 - r2), (x2 - r2, y2 + r2), (x2 + r2, y2 + r2), (x2 + r2, y2 - r2)])
    if y2 > 900 - 2 * r2 or y2 < 0 + 2 * r2:  # Смена направления после удара о границу
        rect_change_y2 = rect_change_y2 * -1

    if x2 > 1200 - 2 * r2 or x2 < 0 + 2 * r2:  # Смена направления после удара о границу
        rect_change_x2 = rect_change_x2 * -1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if click1(event):  # Посчет очков за попадание в шарик
                points = points + 2
            if click2(event):  # Посчет очков за попадание в квадрат
                points = points + 1

    text("Очки " + str(points))
    pygame.display.update()
    screen.fill(BLACK)


pygame.quit()

fin = open('table.txt', 'r', encoding='utf8')
max = 0

for line in fin:
    s = line.split(" ")
    points_0 = int(s[2])
    if max < points_0:
        max = points_0

if points > max:
    fout = open("table.txt", "a", encoding='utf8')
    name = input("Вы стали лучшим игроком!!! Ваше имя?  ")
    print(name + " набрал(а) " + str(points) + " ", file=fout)
    fout.close()

fin.close()
