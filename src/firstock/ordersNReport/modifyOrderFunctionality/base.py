from abc import ABC, abstractmethod

class FirstockAPI(ABC):
    @abstractmethod
    def firstockModifyOrder(self, qty, product, orderNumber, trgprc, prc, tradingSymbol, priceType, userId, mkt_protection=None):
        """
        :return:
        """
        pass