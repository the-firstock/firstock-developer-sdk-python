from abc import ABC, abstractmethod


class FirstockAPI(ABC):
    @abstractmethod
    def firstockModifyGtt(self, userId, jKey, tradingSymbol, exchange, validity, GTTid, OrderParams, remarks="GTT"):
        pass
