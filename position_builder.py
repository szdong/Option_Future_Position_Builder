import matplotlib.pyplot as plt
from pylab import *


class option_type:
    CALL = 1
    PUT = -1


class side:
    LONG = 1
    SHORT = -1


class future_info:
    def __init__(self, price, future_type: side, lot):
        self.price = price
        self.future_type = future_type
        self.lot = lot


class option_info:
    def __init__(self, price, option_type: option_type, side: side, lot, premium):
        self.price = price
        self.option_type = option_type
        self.lot = lot
        self.side = side
        self.premium = premium


class position_builder:
    def __init__(self):
        self.options_lst = []
        self.futures_lst = []
        self.x = []
        self.y = []

    def add_option(self, option_info: option_info):
        self.options_lst.append(option_info)

    def add_future(self, future_info: future_info):
        self.futures_lst.append(future_info)

    def build_position(self, scale=800, step=1, fee=0, size_x=10, size_y=6):
        price_lst = []
        for contract in self.futures_lst + self.options_lst:
            price_lst.append(contract.price)

        start = int(min(price_lst) - scale)
        end = int(max(price_lst) + scale)

        for s in range(start, end, step):
            option_p = 0
            future_p = 0
            for option in self.options_lst:
                option_p += (max(option.option_type * (s - option.price), 0) - option.premium) * option.lot * option.side
            for future in self.futures_lst:
                future_p += (future.future_type * (s - future.price) * future.lot)

            p = option_p + future_p - fee

            self.x.append(s)
            self.y.append(p)

        profit = maximum(self.y, 0)
        loss = minimum(self.y, 0)

        plt.figure(figsize=(size_x, size_y))
        plt.plot(self.x, self.y)
        plt.grid(b=True, which='major', color='#666666', linestyle='-')
        plt.minorticks_on()
        plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
        plt.fill_between(self.x, 0, loss, facecolor='r', alpha=0.5)
        plt.fill_between(self.x, 0, profit, facecolor='g', alpha=0.5)
        plt.title("Position PnL")
        plt.xlabel("BTC/USDT")
        plt.ylabel("PnL")
