from firstock.ordersNReport.modifyAMOFunctionality.functions import *

class FirstockModifyAMO:
    def __init__(self, orderNumber, exch, tsym, qty, prc, prctyp, prd, trantype, ret, trgprc, userId):
        self.modifyAMO = ApiRequests()
        self.orderNumber = orderNumber
        self.exch = exch
        self.tsym = tsym
        self.qty = qty
        self.prc = prc
        self.prctyp = prctyp
        self.prd = prd
        self.trantype = trantype
        self.ret = ret
        self.trgprc = trgprc
        self.userId = userId

    def firstockModifyAMO(self):
        result = self.modifyAMO.firstockModifyAMO(
            self.orderNumber, self.exch, self.tsym, self.qty, self.prc,
            self.prctyp, self.prd, self.trantype, self.ret, self.trgprc,
            self.userId
        )
        return result