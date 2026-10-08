from firstock.ordersNReport.cancelOcoOrderFunctionality.execution import *

def cancelOcoOrder(
    userId,
    OCOid,

):
    try:
        response = FirstockCancelOcoOrder(
            userId=userId,
            OCOid=OCOid
        ).firstockCancelOcoOrder()

        return response

    except Exception as e:
        print(f"Error placing order: {e}")
        return None