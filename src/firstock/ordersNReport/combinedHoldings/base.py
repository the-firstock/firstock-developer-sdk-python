from abc import ABC, abstractmethod


class FirstockAPI(ABC):
    @abstractmethod
    def firstockCombinedHoldings(self, userId):
        """
        :return:
        """
        pass