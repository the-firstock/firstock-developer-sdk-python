from abc import ABC, abstractmethod

class FirstockAPI(ABC):
    @abstractmethod
    def firstockModifyOcoOrder(self, userId, OCOid, exchange, tradingSymbol, OrderParamsLeg1, OrderParamsLeg2):
        """
        :return:
        """
        pass