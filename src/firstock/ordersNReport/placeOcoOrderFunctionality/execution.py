from firstock.ordersNReport.placeOcoOrderFunctionality.functions import *

class FirstockPlaceOcoOrder:
    def __init__(self,  userId, exchange, tradingSymbol, validity, OrderParamsLeg1, OrderParamsLeg2):
        self.placeOcoOrder = ApiRequests()
        self.userId = userId
        self.exchange = exchange
        self.tradingSymbol = tradingSymbol
        self.validity = validity
        self.OrderParamsLeg1 = OrderParamsLeg1
        self.OrderParamsLeg2 = OrderParamsLeg2

    def firstockPlaceOcoOrder(self):
        result = self.placeOcoOrder.firstockPlaceOcoOrder(
            self.userId, self.exchange, self.tradingSymbol, self.validity, self.OrderParamsLeg1, self.OrderParamsLeg2
        )
        return result