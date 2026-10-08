from abc import ABC, abstractmethod

class FirstockAPI(ABC):
    @abstractmethod
    def firstockPlaceOcoOrder(self,userId, exchange, tradingSymbol, validity, OrderParamsLeg1, OrderParamsLeg2):
        """
        :return:
        """
        pass