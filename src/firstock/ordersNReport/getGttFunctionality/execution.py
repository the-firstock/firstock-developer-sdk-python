from firstock.ordersNReport.getGttFunctionality.functions import *


class FirstockGetGtt:
    def __init__(self, userId, jKey):
        self.getGtt = ApiRequests()
        self.userId = userId
        self.jKey = jKey

    def firstockGetGtt(self):
        result = self.getGtt.firstockGetGtt(
            self.userId,
            self.jKey
        )
        return result
