from firstock.ordersNReport.cancelOcoOrderFunctionality.functions import *

class FirstockCancelOcoOrder:
    def __init__(self,  userId, OCOid):
        self.cancelOcoOrder = ApiRequests()
        self.userId = userId
        self.OCOid = OCOid

    def firstockCancelOcoOrder(self):
        result = self.cancelOcoOrder.firstockCancelOcoOrder(
            self.userId, self.OCOid
        )
        return result