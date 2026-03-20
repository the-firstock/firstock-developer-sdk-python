
from abc import ABC, abstractmethod

class FirstockAMOModifyAPI(ABC):
    @abstractmethod
    def firstockModifyAMO(self, orderNumber, exch, tsym, qty, prc, prctyp, prd, trantype, ret, trgprc, userId):
        """
        :return:
        """
        pass