from firstock.ordersNReport.modifyOcoOrderFunctionality.functions import *

class FirstockModifyOcoOrder:
    def __init__(self,  userId, OCOid, exchange, tradingSymbol, OrderParamsLeg1, OrderParamsLeg2):
        self.modifyOcoOrder = ApiRequests()
        self.userId = userId
        self.OCOid = OCOid
        self.exchange = exchange
        self.tradingSymbol = tradingSymbol
        self.OrderParamsLeg1 = OrderParamsLeg1
        self.OrderParamsLeg2 = OrderParamsLeg2

    def firstockModifyOcoOrder(self):
        result = self.modifyOcoOrder.firstockModifyOcoOrder(
            self.userId, self.OCOid, self.exchange, self.tradingSymbol, self.OrderParamsLeg1, self.OrderParamsLeg2
        )
        return result