import pygame
from Stockticker import game
from Menu import settings_menu
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

color = (255, 255, 255)

color_light = (170, 170, 170)

color_dark = (100, 100, 100)

quit_pos_x = 430
quit_pos_y = 550

play_pos_x = 430
play_pos_y = 450

s_pos_x = 430
s_pos_y = 500


smallfont = pygame.font.SysFont('Nevis',35)


def button_creation(x,y,t):
    text = smallfont.render(t, True, color)
    if x <= mouse[0] <= x + 140 and y <= mouse[1] <= y + 40:
            pygame.draw.rect(screen, color_light, [x ,y , 140, 40])
    else:
            pygame.draw.rect(screen, color_dark, [x, y, 140, 40])

    if t == "Settings":
        screen.blit(text, (x + 15, y + 3))
    else:
        screen.blit(text, (x + 40, y + 3))

def button_check(x, y, state):
                if x <= mouse[0] <= x + 140 and y <= mouse[1] <= y + 40 and state == "Quit":
                    pygame.quit()
                if x <= mouse[0] <= x + 140 and y <= mouse[1] <= y + 40 and state == "Play":
                    game(5, False)
                if x <= mouse[0] <= x + 140 and y <= mouse[1] <= y + 40 and state == "Settings":
                    settings_menu()






while run:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game(5, False)

        if event.type == pygame.MOUSEBUTTONDOWN:
            button_check(quit_pos_x, quit_pos_y, "Quit")
            button_check(play_pos_x, play_pos_y, "Play")
            button_check(s_pos_x, s_pos_y, "Settings")



    screen.fill((40, 40, 40))


    mouse = pygame.mouse.get_pos()
    print(mouse)

    button_creation(quit_pos_x,quit_pos_y,"Quit")
    button_creation(play_pos_x, play_pos_y,"Play")
    button_creation(s_pos_x, s_pos_y, "Settings")




    Clock.tick(FPS)
    pygame.display.update()
    pygame.display.flip()
pygame.quit()