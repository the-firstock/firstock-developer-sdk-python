from firstock.ordersNReport.placeAMOFunctionality.functions import *

class FirstockPlaceAMO:
    def __init__(self, exch, tsym, qty, prc, prd, trantype, prctyp, ret, trgprc, remarks, userId):
        self.placeAMO = ApiRequests()
        self.exch = exch
        self.tsym = tsym
        self.qty = qty
        self.prc = prc
        self.prd = prd
        self.trantype = trantype
        self.prctyp = prctyp
        self.ret = ret
        self.trgprc = trgprc
        self.remarks = remarks
        self.userId = userId

    def firstockPlaceAMO(self):
        result = self.placeAMO.firstockPlaceAMO(
            self.exch, self.tsym, self.qty, self.prc, self.prd,
            self.trantype, self.prctyp, self.ret, self.trgprc,
            self.remarks, self.userId
        )
        return result