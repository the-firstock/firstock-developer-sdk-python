from firstock.ordersNReport.cancelGttFunctionality.functions import *


class FirstockCancelGtt:
    def __init__(self, userId, jKey, GTTid):
        self.cancelGtt = ApiRequests()
        self.userId = userId
        self.jKey = jKey
        self.GTTid = GTTid

    def firstockCancelGtt(self):
        result = self.cancelGtt.firstockCancelGtt(
            self.userId,
            self.jKey,
            self.GTTid
        )
        return result
