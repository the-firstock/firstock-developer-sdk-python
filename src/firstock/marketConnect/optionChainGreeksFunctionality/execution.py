from firstock.marketConnect.optionChainGreeksFunctionality.functions import *

class FirstockOptionChainGreeks:
    def __init__(self, exch, symbol, expiry, count, strikePrice, userId):
        self.optionChainGreeks = ApiRequests()
        self.exch = exch
        self.symbol = symbol
        self.expiry = expiry
        self.count = count
        self.strikePrice = strikePrice
        self.userId = userId

    def firstockOptionChainGreeks(self):
        result = self.optionChainGreeks.firstockOptionChainGreeks(
            self.exch, self.symbol, self.expiry, self.count,
            self.strikePrice, self.userId
        )
        return result