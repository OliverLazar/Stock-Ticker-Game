import pygame
import pygame_menu
from Stockticker import game

players = ["Player 1", "Player 2", "Player 3", "Player 4", "Player 5", "Player 6", "Player 7", "Player 8",
           "Player 9", "Player 10"]
fps = 60
text_box = []
window_size = (1000, 700)
screen = pygame.display.set_mode(window_size)
clock = pygame.time.Clock()

selectors = []



def main_background():
    screen.fill((0, 0, 0))

def play():
    for i in range(0, 10):
        for n in text_box[i].get_value():
            players[i] = text_box[i].get_value()
    game(int(selectors[0].get_value()[0][0]), (selectors[1].get_value()[0][0] == "T"), players, False)

def from_save():
    for i in range(0, 10):
        for n in text_box[i].get_value():
            players[i] = text_box[i].get_value()
    game(int(selectors[0].get_value()[0][0]), (selectors[1].get_value()[0][0] == "T"), players, True)

def main(test: bool = False) -> None:
    pygame.init()

    minimal_theme = pygame_menu.Theme(
        background_color=(0, 0, 0, 0),
        title=False,
        widget_font=pygame_menu.font.FONT_NEVIS,
        widget_font_size=25,
        widget_font_color=(255, 255, 255)
    )

    settings_menu = pygame_menu.Menu(
        height=window_size[1] * 0.85,
        theme=minimal_theme,
        title='',
        width=window_size[0] * 0.9
    )

    for player in players:
        text_box.append(settings_menu.add.text_input(
            player + ': ',
            default=player,

            textinput_id=player, maxchar = 11
        ))

    items = [(str(i), str(i)) for i in range(1, 11)]
    selectors.append(settings_menu.add.selector(
        'Player Count:\t', items, selector_id="Player Count", default=9))
    selectors.append(settings_menu.add.selector(
        'Futures Trading:\t', ["False","True"], selector_id="Futures", default=1))
    settings_menu.add.button('Restore original values', settings_menu.reset_value)
    settings_menu.add.button('')
    settings_menu.add.button('Return to main menu', pygame_menu.events.BACK)

    # Create menus: Main menu
    main_menu = pygame_menu.Menu(
        height=window_size[1] * 0.7,
        onclose=pygame_menu.events.EXIT,
        theme=minimal_theme,
        title='',
        width=window_size[0] * 0.8
    )

    main_menu.add.button('Play', play)
    main_menu.add.button('Load from Save', from_save)
    main_menu.add.button('Settings', settings_menu)
    main_menu.add.button('Quit', pygame_menu.events.EXIT)


    return main_menu

    # Main loop

while True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False


    clock.tick(fps)
    main_background()
    main().mainloop(screen, main_background, fps_limit=fps)
    pygame.display.update()
