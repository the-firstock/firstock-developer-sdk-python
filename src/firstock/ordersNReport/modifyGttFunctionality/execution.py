from firstock.ordersNReport.modifyGttFunctionality.functions import *


class FirstockModifyGtt:
    def __init__(self, userId, jKey, tradingSymbol, exchange, validity, GTTid, OrderParams, remarks="GTT"):
        self.modifyGtt = ApiRequests()
        self.userId = userId
        self.jKey = jKey
        self.tradingSymbol = tradingSymbol
        self.exchange = exchange
        self.validity = validity
        self.GTTid = GTTid
        self.OrderParams = OrderParams
        self.remarks = remarks

    def firstockModifyGtt(self):
        result = self.modifyGtt.firstockModifyGtt(
            self.userId,
            self.jKey,
            self.tradingSymbol,
            self.exchange,
            self.validity,
            self.GTTid,
            self.OrderParams,
            self.remarks
        )
        return result
