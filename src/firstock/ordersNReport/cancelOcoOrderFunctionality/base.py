from abc import ABC, abstractmethod

class FirstockAPI(ABC):
    @abstractmethod
    def firstockCancelOcoOrder(self, userId, OCOid):
        """
        :return:
        """
        pass