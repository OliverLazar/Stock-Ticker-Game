class game():
    def __init__(self, playercount, futures_trading, players):
        self.playercount = playercount
        self.futures_trading = futures_trading
        self.players = players
        print(playercount)
        columns = ["Player #","Gold", "Silver","Oil","Indust", "Bonds", "Grain", "Cash", "Networth"]
        players = players[:playercount]
        color_cycle = ["Green","Gold", "Silver","Dark Grey","Red","Dark Green","Yellow","Green","Green"]
        n_col = 9
        n_row = playercount + 1
        on_crawler = {"":0}
        x = 1000


        prices = {"Gold":1,
                    "Silver":1,
                    "Oil":1,
                    "Indust":1,
                    "Bonds":1,
                    "Grain":1}

        stock_colors = {"Gold": "Gold",
                  "Silver": "Silver",
                  "Oil": "Dark Grey",
                  "Indust": "Red",
                  "Bonds": "Dark Green",
                  "Grain": "Yellow"}

        dice2 = ["Up", "Down", "Div","Up", "Down", "Div"]
        dice3 = [5,10,20,5,10,20]



        import pygame
        from player import Player
        from random import randint
        import time
        pygame.init()


        screen = pygame.display.set_mode((1000, 700))
        clock = pygame.time.Clock()
        pygame.display.set_caption("Stock Ticker Game")
        col_font = pygame.font.SysFont("System", 25)
        crawl_font = pygame.font.SysFont("System", 40)

        for player in range(1,playercount+1):
            players.append(Player(5000, 5000, player))
            print(players)

        FPS = 60

        rectangles = {}

        width = int(1000/9)
        height = int(700/11 * 0.4)

        crawler = pygame.Rect(0, 360, 1000, height * 2, width=2)

        highlight_row = 1
        highlight_col = 1



        def grid():
            for r in range(n_row):
                for c in range(n_col):
                    rect = pygame.Rect(0 + width * c, 420 + height * r, width, height)
                    pygame.draw.rect(screen, (0,0,0), rect)

                    rectangles[(r, c)] = rect


        def change_cell_text(row, col, text, color):
            if (row, col) in rectangles:
                rect = rectangles[(row, col)]
                text_surface = col_font.render(text, False, color)
                text_rect = text_surface.get_rect(center=rect.center)
                screen.blit(text_surface, text_rect)

        def draw_highlight(row, col, color):
            if (row, col) in rectangles:
                rect = rectangles[(row, col)]
                pygame.draw.rect(screen, color, rect, 4)

        def net_worth_update():
            for p in players[playercount:]:
                r = p.row
                nw = p.net_worth
                c = p.cash
                change_cell_text(r, 8, str(nw), "Green")
                change_cell_text(r, 7, str(c), "Green")


        def update_board():
            for p in players[playercount:]:
                r = p.row
                stock = p.stocks
                c = 1
                for n in stock:
                    if stock[n] != 0:
                        change_cell_text(r, c, str(stock[n]), color_cycle[c])
                    c += 1

        def dice_roll():
            d6 = randint(0,5)
            d6_2 = randint(0,5)
            d6_3 = randint(0, 5)
            stock = list(prices.keys())[d6]
            occurance = dice2[d6_2]
            interval = dice3[d6_3]
            if occurance == "Up":
                prices[stock] += round(interval/100,2)

            if occurance == "Down":
                prices[stock] -= round(interval/100,2)

            if occurance == "Div":
                if prices[stock] >= 1:
                    for p in players[playercount:]:
                        p.cash += (p.stocks[stock] * round(interval/100,2))
            return stock,occurance,interval


        def crawl():
                if on_crawler[list(on_crawler.keys())[0]] in [750,500,250,0]:
                    if "" in list(on_crawler.keys()):
                        del on_crawler[""]
                    stock, occurance, interval = dice_roll()
                    text = f"{stock} {occurance} {interval}"
                    text_surface = crawl_font.render(text, False, stock_colors[stock])
                    on_crawler.update({text_surface:1000})


        def crawl_move():
            for text in (list(on_crawler.keys())):
                screen.blit(text, (on_crawler[text], 370))
                on_crawler[text] -= 2
            if on_crawler[list(on_crawler.keys())[0]] <= -200:
                del on_crawler[list(on_crawler.keys())[0]]







        run = True

        while run:

            screen.fill("Black")

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
                    if event.key == pygame.K_EQUALS:
                        p = players[highlight_row + playercount -1]
                        if p.cash >= 500*prices[columns[highlight_col]]:
                            p.stocks[columns[highlight_col]] += 500
                            p.cash -= 500*prices[columns[highlight_col]]
                    if event.key == pygame.K_MINUS:
                        p = players[highlight_row + playercount -1]
                        if p.stocks[columns[highlight_col]] == 0 and futures_trading == False:
                            pass
                        else:
                            p.stocks[columns[highlight_col]] -= 500
                            p.cash += 500 * prices[columns[highlight_col]]



            grid()

            for row in range(1,n_row):
                change_cell_text(row,0, players[row - 1] ,"green")
            for col in range(0,9):
                change_cell_text(0, col, columns[col], color_cycle[col])

            crawl()
            crawl_move()

            pygame.draw.rect(screen, (64, 64, 192), crawler, 2)

            draw_highlight(highlight_row, highlight_col, color_cycle[highlight_col])

            net_worth_update()
            update_board()


            clock.tick(FPS)
            pygame.display.update()
            pygame.display.flip()

        pygame.quit()


