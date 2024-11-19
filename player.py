class Player:
    def __init__(self, cash, net_worth):
        self.cash = cash
        self.net_worth = net_worth
        self.stocks = {"Gold":0,
                       "Grain":0,
                       "Industry":0,
                       "Oil":0,
                       "Silver":0,
                       "Bonds":0}

