class Player:
    def __init__(self, cash, net_worth, row):
        self.cash = cash
        self.net_worth = net_worth
        self.row = row
        self.stocks = {"Gold":0,
                       "Silver":0,
                       "Oil":0,
                       "Indust":0,
                       "Bonds":0,
                       "Grain":0}

