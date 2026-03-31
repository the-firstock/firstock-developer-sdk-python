from firstock.ordersNReport.modifyAMOFunctionality.functions import *

class FirstockModifyAMO:
    def __init__(self, orderNumber, qty, prc, prctyp, prd, trgprc, userId, mkt_protection=None):
        self.modifyAMO = ApiRequests()
        self.orderNumber = orderNumber
        self.qty = qty
        self.prc = prc
        self.prctyp = prctyp
        self.prd = prd
        self.trgprc = trgprc
        self.userId = userId
        self.mkt_protection = mkt_protection

    def firstockModifyAMO(self):
        result = self.modifyAMO.firstockModifyAMO(
            self.orderNumber, self.qty, self.prc,
            self.prctyp, self.prd, self.trgprc, self.userId, self.mkt_protection
        )
        return result