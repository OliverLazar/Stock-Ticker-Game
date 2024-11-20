columns = ["Player #","Gold", "Silver","Oil","Indust", "Bonds", "Grain", "Cash", "Networth"]
players = ["Player 1","Player 2","Player 3","Player 4","Player 5","Player 6","Player 7","Player 8","Player 9","Player 10"]
color_cycle = ["Green","Gold", "Silver","Dark Grey","Red","Dark Green","Yellow","Green","Green"]
n_col = 9
n_row = 11

import pygame
from player import Player
pygame.init()
y=350
x = 110
screen = pygame.display.set_mode((1000, 700))
Clock = pygame.time.Clock()
pygame.display.set_caption("Stock Ticker Game")
col_font = pygame.font.SysFont("System", 25)

FPS = 60

rectangles = {}

width = int(1000/9)
height = int(700/11 * 0.4)

highlight_row = 1
highlight_col = 1

def grid():
    for r in range(n_row):
        for c in range(n_col):
            rect = pygame.Rect(0 + width * c, 420 + height * r, width, height)
            pygame.draw.rect(screen, (0,0,0), rect)

            rectangles[(r, c)] = rect

# Function to draw text in a specific cell
def change_cell_text(row, col, text, color):
    if (row, col) in rectangles:
        rect = rectangles[(row, col)]
        text_surface = col_font.render(text, True, color)
        text_rect = text_surface.get_rect(center=rect.center)
        screen.blit(text_surface, text_rect)

def draw_highlight(row, col, color):
    if (row, col) in rectangles:
        rect = rectangles[(row, col)]
        pygame.draw.rect(screen, color, rect, 4)

run = True

while run:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and highlight_row > 1 :
                highlight_row -= 1
            if event.key == pygame.K_DOWN and highlight_row < n_row - 1:
                highlight_row += 1
            if event.key == pygame.K_LEFT and highlight_col > 0 and highlight_col > 1:
                highlight_col -= 1
            if event.key == pygame.K_RIGHT and highlight_col < 6:
                highlight_col += 1



    grid()

    for row in range(1,11):
        change_cell_text(row,0, players[row-1] ,"green")
    for col in range(0,9):
        change_cell_text(0, col, columns[col], color_cycle[col])

    draw_highlight(highlight_row, highlight_col, color_cycle[highlight_col])


    Clock.tick(FPS)
    pygame.display.update()
    pygame.display.flip()
pygame.quit()


