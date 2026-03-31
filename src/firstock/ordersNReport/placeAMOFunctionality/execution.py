from firstock.ordersNReport.placeAMOFunctionality.functions import *

class FirstockPlaceAMO:
    def __init__(self, exch, tsym, qty, prc, prd, trantype, prctyp, ret, trgprc, remarks, userId, mkt_protection=None):
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
        self.mkt_protection = mkt_protection

    def firstockPlaceAMO(self):
        result = self.placeAMO.firstockPlaceAMO(
            self.exch, self.tsym, self.qty, self.prc, self.prd,
            self.trantype, self.prctyp, self.ret, self.trgprc,
            self.remarks, self.userId, self.mkt_protection
        )
        return result