current_x_interval = 0
inverse = False
class game():
    def __init__(self, playercount, futures_trading, players, resume_game):
        self.playercount = playercount
        self.futures_trading = futures_trading
        self.players = players
        self.resume_game = True
        columns = ["Player #","Gold", "Silver","Oil","Indust", "Bonds", "Grain", "Cash", "Networth"]
        players = players[:self.playercount]
        color_cycle = ["Green",(170,170,0), (170,170,255),(170,170,170),(170,0,0),(0,170,0),(180,160,110),"Green","Green"]
        n_col = 9
        n_row = self.playercount + 1
        on_crawler = {}
        key_recording = False
        x = 1000
        instructions = [
            "Welcome to Stock Ticker Game!",
            "Instructions:",
            "- Use arrow keys to navigate.",
            "- Press SPACE to toggle the market state.",
            "- Use '=' to buy 500 shares and '-' to sell 500 shares.",
            "- Use '[' to sell all shares and ']' to buy max shares.",
            "- Press ENTER to add a player and TAB to confirm their name.",
            "- Press s to save the game"
        ]




        prices = {"Gold":100,
                    "Silver":100,
                    "Oil":100,
                    "Indust":100,
                    "Bonds":100,
                    "Grain":100}

        stock_colors = {"Gold": (170,170,0),
                  "Silver": (170,170,255),
                  "Oil": (170,170,170),
                  "Indust": (170,0,0),
                  "Bonds": (0,170,0),
                  "Grain": (180,160,110)}

        points = {"Gold": [(0,180),(0,180)],
                  "Silver": [(0,180),(0,180)],
                  "Oil": [(0,180),(0,180)],
                  "Indust": [(0,180),(0,180)],
                  "Bonds": [(0,180),(0,180)],
                  "Grain": [(0,180),(0,180)]}

        c_points = {"Gold": [],
                  "Silver": [],
                  "Oil": [],
                  "Indust": [],
                  "Bonds": [],
                  "Grain": []}

        dice2 = ["Up", "Down", "Div","Up", "Down", "Div"]
        dice3 = [5,10,20,5,10,20]

        crawl_finished = True




        import pygame
        from player import Player
        from random import randint
        from time import gmtime, strftime
        from operator import attrgetter
        import tkinter as tk
        from tkinter import filedialog
        import csv
        pygame.init()


        screen = pygame.display.set_mode((1000, 700))
        clock = pygame.time.Clock()
        pygame.display.set_caption("Stock Ticker Game")
        col_font = pygame.font.SysFont("System", 25)
        crawl_font = pygame.font.SysFont("System", 40)

        for pos in range(0,self.playercount):
            players.append(Player(5000, 5000,pos+1, name=players[pos]))

        players = players[self.playercount:]

        FPS = 60

        rectangles = {}

        width = int(1000/9)
        height = int(700/11 * 0.4)

        crawler = pygame.Rect(0, 360, 1000, height * 2, width=2)

        highlight_row = 1
        highlight_col = 1

        market_open = False

        if resume_game == True:

            root = tk.Tk()
            root.withdraw()
            file_path = filedialog.askopenfilename(
                filetypes=[("CSV files", "*.csv"), ("All files", "*.*")],
                title="Load Game State"
            )
            if file_path:
                try:
                    with open(file_path, "r") as file:
                        reader = csv.reader(file)
                        game_state = list(reader)
                    for row in game_state:
                            if row[0] == "Player Count":
                                self.playercount = int(row[1])
                            elif row[0] in prices and len(row) >= 2:
                                prices[row[0]] = int(row[1])
                            elif row[0] == "Futures Trading State":
                                self.futures_trading = (row[1] == "True")
                    players = []
                    for n in range(1,self.playercount+1):

                        p = Player(int(float(game_state[n][1])), int(game_state[n][2]), int(game_state[n][3]), str(game_state[n][0]))
                        p.stocks = eval(game_state[n][4])
                        players.append(p)
                    resume_game = False
                    screen.fill("Black")
                    n_row = self.playercount + 1
                except FileNotFoundError:
                    print("Save file not found")
                except ValueError:
                    print("Save file is wrong")
                    pygame.quit()
                except IndexError:
                    print("Save file is wrong")
                    pygame.quit()
            else:
                print("Load failed")


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
            for p in players:
                r = p.row
                c = round(p.cash)

                nw = p.net_worth
                c = round(p.cash)
                change_cell_text(r, 8, str(nw), "Green")
                change_cell_text(r, 7, str(c), "Green")


        def update_board():
            for p in players:
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
                prices[stock] += round(interval,2)

            if occurance == "Down":
                prices[stock] -= round(interval,2)

            if occurance == "Div":
                if prices[stock] >= 100:
                    for p in players:
                            p.cash += (p.stocks[stock] * round(interval/100,2))

            if prices[stock] >= 200:
                prices[stock] = 100
                for p in players:
                    p.stocks[stock] = p.stocks[stock] * 2
            if prices[stock] <= 0:
                prices[stock] = 100
                for p in players:
                    p.stocks[stock] = p.stocks[stock] * 0
            return stock,occurance,interval


        def crawl():
                global current_x_interval
                if on_crawler[list(on_crawler.keys())[0]] in [750,500,250,0,"placeholder"]:
                    stock, occurance, interval = dice_roll()
                    text = f"{stock} {occurance} {interval}"
                    text_surface = crawl_font.render(text, False, stock_colors[stock])
                    on_crawler.update({text_surface:1000})
                    update_points()
                    if occurance == "Div" and prices[stock] >= 100:
                        c_points[stock].append((current_x_interval-2.5,prices[stock]*-1.8+360))



        def crawl_move():
            if "placeholder" in on_crawler:
                del on_crawler['placeholder']
            for text in (list(on_crawler.keys())):
                screen.blit(text, (on_crawler[text], 370))
                on_crawler[text] -= 25
            if on_crawler[list(on_crawler.keys())[0]] <= -200:
                del on_crawler[list(on_crawler.keys())[0]]
            if len(on_crawler) == 0:
                return True

        def draw_x_axis():
            xi = 0
            xf = 5
            for _ in range(0,100):
                pygame.draw.line(screen, "White",(xi-5,180),(xf-5,180),1)
                xi += 10
                xf += 10


        def update_points():
            global current_x_interval
            iteration = 0
            for v in points:
                points[v].append((current_x_interval, prices[v] * -1.8 + 360))
                if current_x_interval == 1000:
                        lst =  list(points[v][-2])
                        lst[0] = 0
                        points[v][-2] = tuple(lst)
                        lst = list(points[v][-1])
                        lst[0] = 5
                        points[v][-1]= tuple(lst)

                        points[v] = points[v][-2:]


                        c_points[v] = []

                        iteration += 1
                if iteration == 6:
                    current_x_interval = 10
            current_x_interval += 5


        def draw_lines():
            draw_order = list(points.keys())
            for i in range(len(points["Gold"])-1):
                for v in draw_order:
                    split_1, split_2 = points[v][i], points[v][i+1]
                    pygame.draw.line(screen, stock_colors[v], split_1, split_2, 1)
                draw_order.reverse()





        def draw_circle():
            for v in c_points:
                for n in c_points[v]:
                    pygame.draw.circle(screen, stock_colors[v], n, 5, 1)

        def market_closed_blit():
            on_crawler = {}
            text_surface = crawl_font.render("Market Open", False, "Green")
            on_crawler[text_surface] = 1000
            screen.blit(text_surface, (on_crawler[text_surface], 370))
            text_surface = crawl_font.render("Cost:", False, "Green")
            screen.blit(text_surface, (20, 370))
            on_crawler[text_surface] = 20
            for col in range(1, 7):
                stock = columns[col]
                text_surface = crawl_font.render(f"{prices[stock]}", False, stock_colors[stock])
                screen.blit(text_surface, ((width * (col + 1) - 80), 370))
                on_crawler[text_surface] = (width * (col + 1) - 80)
            time = strftime("%H:%M:%S")
            text_surface = crawl_font.render(f"{time}", False, "Green")
            screen.blit(text_surface, (820, 370))
            on_crawler[text_surface] = 820
            on_crawler["placeholder"] = "placeholder"
            return on_crawler

        def display_instructions():
            instruction_font = pygame.font.SysFont("System", 40)
            y_offset = 10

            for line in instructions:
                words = line.split(" ")
                x_offset = 10
                for word in words:
                    if word in ["'='", "'-'", "'['", "']'", "SPACE", "ENTER", "TAB", "s"]:
                        text_surface = instruction_font.render(word, False, "Yellow")
                    else:
                        text_surface = instruction_font.render(word, False, "Green")
                    text_rect = text_surface.get_rect(topleft=(x_offset, y_offset))
                    screen.blit(text_surface, text_rect.topleft)
                    x_offset += text_rect.width + 5
                y_offset += 40
        def save():
            game_state = []
            game_state.append(["Player Count", self.playercount])

            for p in players:
                game_state.append([p.name, p.cash, p.net_worth, p.row, p.stocks])

            for stock, price in prices.items():
                game_state.append([stock, price])

            game_state.append(["Futures Trading State", futures_trading])
            root = tk.Tk()
            root.withdraw()
            file_path = filedialog.asksaveasfilename(
                defaultextension=".csv",
                filetypes=[("CSV files", "*.csv"), ("All files", "*.*")],
                title="Save Game"
            )
            if file_path:
                with open(file_path, "w", newline="") as file:
                    writer = csv.writer(file)
                    writer.writerows(game_state)
                print(f"Game state saved to {file_path}")
            else:
                print("Save operation canceled.")





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
                    if event.key == pygame.K_EQUALS and key_recording == False and market_open == False:
                        p = players[highlight_row -1]
                        if p.cash >= 500*prices[columns[highlight_col]]/100:
                            p.stocks[columns[highlight_col]] += 500
                            p.cash -= 500*prices[columns[highlight_col]]/100
                    if event.key == pygame.K_MINUS and key_recording == False and market_open == False:
                        p = players[highlight_row -1]
                        if p.stocks[columns[highlight_col]] == 0 and futures_trading == False:
                            pass
                        else:
                            if (p.stocks[columns[highlight_col]] -500) * prices[columns[highlight_col]] // 100 + p.net_worth >= 0:
                                p.stocks[columns[highlight_col]] -= 500
                                p.cash += 500 * prices[columns[highlight_col]]/100
                    if event.key == pygame.K_SPACE and key_recording == False:
                        if market_open == False and crawl_finished == True:
                            market_open = True

                        elif market_open == True:
                            market_open = False
                            crawl_finished = False
                            text_surface = crawl_font.render("Market Closed", False, "Green")
                            on_crawler[text_surface] = on_crawler[list(on_crawler.keys())[-1]] + 250
                            for p in players:
                                total_stock_value = 0
                                for stock in p.stocks:
                                    total_stock_value += (p.stocks[stock] * prices[stock]/100)
                                p.net_worth = round(p.cash + total_stock_value)
                            players.sort(key=attrgetter("net_worth"), reverse=True)
                    if event.key == pygame.K_RETURN and market_open == False:
                        if self.playercount != 10 and key_recording != True:
                            self.playercount += 1
                            players.append(Player(5000, 5000, self.playercount, ""))
                            n_row = self.playercount + 1
                            highlight_col = 0
                            highlight_row = self.playercount
                            key_recording = True
                    if key_recording:

                        if event.key == pygame.K_TAB:

                            key_recording = False
                            players[-1].name = players[-1].name
                            highlight_col = 1
                        elif event.key == pygame.K_BACKSPACE:
                            players[-1].name = players[-1].name[:-1]
                        else:
                            if event.key != pygame.K_RETURN and len(players[-1].name) <= 11:
                                players[-1].name += event.unicode

                    if event.key == pygame.K_LEFTBRACKET:
                        p = players[highlight_row - 1]
                        if p.stocks[columns[highlight_col]] == 0 and futures_trading == False:
                            pass
                        elif p.stocks[columns[highlight_col]] <= 0:
                            pass
                        else:
                            p.cash += p.stocks[columns[highlight_col]] * prices[columns[highlight_col]] / 100
                            p.stocks[columns[highlight_col]] = 0
                    if event.key == pygame.K_RIGHTBRACKET:
                        p = players[highlight_row - 1]
                        max_buy = int(p.cash/((prices[columns[highlight_col]])/100)/500)
                        p.cash -= (max_buy*500) * (prices[columns[highlight_col]] / 100)
                        p.stocks[columns[highlight_col]] += (max_buy*500)
                    if event.key == pygame.K_s and key_recording == False:
                        save()





            grid()

            for i,p in enumerate(players):
                change_cell_text(i+1,0, str(p.name),"green")
                p.row = i+1
            for col in range(0,9):
                change_cell_text(0, col, columns[col], color_cycle[col])



            pygame.draw.rect(screen, (64, 64, 192), crawler, 2)

            draw_highlight(highlight_row, highlight_col, color_cycle[highlight_col])

            net_worth_update()
            update_board()

            if market_open == False:

                if crawl_finished == True:
                    on_crawler = market_closed_blit()
                else:
                    crawl_finished = crawl_move()
                display_instructions()




            if market_open == True:
                crawl()
                crawl_move()
                draw_x_axis()
                draw_lines()
                draw_circle()



            clock.tick(FPS)
            pygame.display.update()
            pygame.display.flip()

        pygame.quit()


