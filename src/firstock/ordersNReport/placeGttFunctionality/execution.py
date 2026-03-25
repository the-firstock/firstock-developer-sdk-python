from firstock.ordersNReport.placeGttFunctionality.functions import ApiRequests


class FirstockPlaceGtt:
    def __init__(self, userId, jKey, tradingSymbol, exchange, validity, value, OrderParams, remarks):
        self.placeGtt = ApiRequests()
        self.userId = userId
        self.jKey = jKey
        self.tradingSymbol = tradingSymbol
        self.exchange = exchange
        self.validity = validity
        self.value = value
        self.OrderParams = OrderParams
        self.remarks = remarks

    def firstockPlaceGtt(self):
        return self.placeGtt.firstockPlaceGtt(
            self.userId,
            self.jKey,
            self.tradingSymbol,
            self.exchange,
            self.validity,
            self.value,
            self.OrderParams,
            self.remarks
        )