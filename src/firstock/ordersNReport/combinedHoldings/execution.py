from firstock.ordersNReport.combinedHoldings.functions import *

class FirstockCombinedHoldings:
    def __init__(self, userId):
        self.CombinedHoldings = ApiRequests()
        self.userId = userId

    def firstockCombinedHoldings(self):
        return self.CombinedHoldings.firstockCombinedHoldings(
            userId=self.userId
        )