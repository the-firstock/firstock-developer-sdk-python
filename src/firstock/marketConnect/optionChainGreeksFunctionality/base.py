from abc import ABC, abstractmethod

class FirstockOptionChainGreeksAPI(ABC):
    @abstractmethod
    def firstockOptionChainGreeks(self, exch, symbol, expiry, count, strikePrice, userId):
        """
        :return:
        """
        pass