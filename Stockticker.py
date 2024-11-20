columns = ["Player", "Gold", "Grain", "Industry", "Oil", "Silver", "Bonds", "Cash", "Networth"]
players = ["Player 1","Player 2","Player 3","Player 4","Player 5","Player 6","Player 7","Player 8","Player 9","Player 10"]
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

rectangles = {}

width = int(1000/9)
height = int(700/10 * 0.4)

def grid():
    for r in range(n_row):
        for c in range(n_col):
            rect = pygame.Rect(0 + width * c, 420 + height * r, width, height)
            pygame.draw.rect(screen, (255, 255, 255), rect)
            pygame.draw.rect(screen, (0, 0, 0), rect, 1)

            rectangles[(r, c)] = rect

# Function to draw text in a specific cell
def change_cell_text(row, col, text, color):
    if (row, col) in rectangles:
        rect = rectangles[(row, col)]
        text_surface = col_font.render(text, True, color)
        text_rect = text_surface.get_rect(center=rect.center)
        screen.blit(text_surface, text_rect)

run = True

while run:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False



    grid()
    for row in range(0,10):
        change_cell_text(row,0, players[row] ,"black")




    Clock.tick(FPS)
    pygame.display.update()
    pygame.display.flip()
pygame.quit()


