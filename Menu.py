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
height = screen.get_height()
width = screen.get_width()
# white color
color = (255, 255, 255)

# light shade of the button
color_light = (170, 170, 170)

# dark shade of the button
color_dark = (100, 100, 100)

smallfont = pygame.font.SysFont('Corbel',35)
text = smallfont.render('quit' , True , color)

while run:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game(10, False)

        if event.type == pygame.MOUSEBUTTONDOWN:

                if width / 2 <= mouse[0] <= width / 2 + 140 and height / 2 <= mouse[1] <= height / 2 + 40:
                    pygame.quit()


    screen.fill((60, 25, 60))


    mouse = pygame.mouse.get_pos()

    if width / 2 <= mouse[0] <= width / 2 + 140 and height / 2 <= mouse[1] <= height / 2 + 40:
            pygame.draw.rect(screen, color_light, [width / 2, height / 2, 140, 40])
    else:
            pygame.draw.rect(screen, color_dark, [width / 2, height / 2, 140, 40])


    screen.blit(text, (width / 2 + 50, height / 2))




    Clock.tick(FPS)
    pygame.display.update()
    pygame.display.flip()
pygame.quit()