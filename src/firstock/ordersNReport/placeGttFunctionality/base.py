from abc import ABC, abstractmethod


class FirstockAPI(ABC):
    @abstractmethod
    def firstockPlaceGtt(self, userId, jKey, tradingSymbol, exchange, validity, value, OrderParams, remarks):
        pass
