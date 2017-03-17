"""
buy_stock(company, number, buy_price)
sell_stock(company, number, sell_price) returns the "profit/loss" made, cannot sell stocks that you don't have!
sell_multiple(company_list, number_list, sell_price_list)
buy_multiple(company_list, number_list, buy_price_list)
print_current_portfolio(self) company, total number of stocks, total value
print_transaction_list(self) company, stock

total profit()
total loss()

example:
buy(Hyundai, 10, 50)
buy(LG, 20, 30)
buy(Hyundai, 20, 40)
buy(LG, 10, 35)
sell(LG, 5, 30) output: a loss was made of 25
sell(Hyundai, 25, 60) output: a profit was mda of 20*20 + 5*10
"""

from module04_stacks_and_queues.part00_preclass.stack import ArrayStack

class StockManager:

    __PROFIT = 0

    def __init__(self, o_name, o_surname):
        """
        Initialises the Stock Manager with the name and surname of the client
        :param o_name: name of the client
        :param o_surname: surname of the client
        """
        pass

    def buy_shares(self, company, number, buy_price):
        """
        Buy stocks
        :param company: the company of which shares are being bought
        :param number: the number of shares to buy
        :param buy_price: the price (per share) at which shares are bought
        """
        pass


    def sell_shares(self, company, number, sell_price):
        """
        Sell shares (only if you have enough to sell!)
        :param company: the company of which shares are being bought
        :param number: the number of shares to buy
        :param sell_price: the price (per share) at which shares are sold
        """
        pass


    def buy_multiple(self, buy_list):
        pass

    def sell_multiple(self, sell_list):
        pass

    def get_profit(self):
        return self.__PROFIT


    """ allows to print the current stock held by the investor"""
    def print_portfolio(self):
        pass




if __name__ == '__main__':
    #add here some code to do the testing
    P = StockManager("Marco", "Comuzzi")

    P.buy_shares("hyundai", 20, 100)
    P.buy_shares("hyundai", 20, 100)

    print("Profit: {0}".format(P.sell_shares("hyundai", 5, 120)))
    print("Current cumulative profit: {0}".format(P.get_profit()))
    print("Profit: {0}".format(P.sell_shares("hyundai", 31, 127)))
    print("Current cumulative profit: {0}".format(P.get_profit()))
    print("Profit: {0}".format(P.sell_shares("hyundai", 2, 23)))
    print("Current cumulative profit: {0}".format(P.get_profit()))
    P.print_portfolio()

    P.sell_shares("hyundai", 50, 150)
    P.buy_multiple((["hyundai", 10, 56], ["lg", 56, 27]))
    P.sell_multiple((["hyundai", 1, 56], ["lg", 1, 27]))
    P.print_portfolio()
