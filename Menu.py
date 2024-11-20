import pygame
from Stockticker import game
pygame.init()
y=350
x = 110
FPS = 60
screen = pygame.display.set_mode((1000, 700))
Clock = pygame.time.Clock()
pygame.display.set_caption("Stock Ticker Game")
col_font = pygame.font.SysFont("System", 25)
run = True

while run:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_KP_ENTER:
                game()

    Clock.tick(FPS)
    pygame.display.update()
    pygame.display.flip()
pygame.quit()