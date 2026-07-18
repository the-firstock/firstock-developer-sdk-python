from firstock.ordersNReport.combinedHoldings.execution import *

def combinedHoldings(userId):
    try:
        combined = FirstockCombinedHoldings(
            userId=userId
        )
        result = combined.firstockCombinedHoldings()
        return result
    except Exception as e:
        print(e)