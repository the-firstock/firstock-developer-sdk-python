from abc import ABC, abstractmethod

class FirstockAMOAPI(ABC):
    @abstractmethod
    def firstockPlaceAMO(self, exch, tsym, qty, prc, prd, trantype, prctyp, ret, trgprc, remarks, userId, mkt_protection=None):
        """
        :return:
        """
        pass