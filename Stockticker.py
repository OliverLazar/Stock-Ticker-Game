columns = ["Player", "Gold", "Grain", "Industry", "Oil", "Silver", "Bonds", "Cash", "Networth"]
color_cycle = []
n_col = 9
n_row = 11

import pygame
from player import Player
pygame.init()
y=350
x = 110
screen = pygame.display.set_mode((1000, 700))
Clock = pygame.time.Clock()
col_font = pygame.font.SysFont("Arial", 30)

FPS = 60



width = int(1000/9)
height = int(700/11 * 0.4)

def grid():

    for r in range(0,n_row):
        for c in range(0,n_col):
            rect = pygame.rect.Rect(0 + width*c ,425 + height * r, width, height)
            pygame.draw.rect(screen, (255, 255, 255), rect)
            pygame.draw.rect(screen, (0, 0, 0), rect, 1)

run = True

while run:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False



    grid()






    Clock.tick(FPS)
    pygame.display.update()
    pygame.display.flip()
pygame.quit()


