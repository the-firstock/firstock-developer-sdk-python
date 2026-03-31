from abc import ABC, abstractmethod

class FirstockAMOModifyAPI(ABC):
    @abstractmethod
    def firstockModifyAMO(self, orderNumber, qty, prc, prctyp, prd, trgprc, userId, mkt_protection=None):
        """
        :return:
        """
        pass