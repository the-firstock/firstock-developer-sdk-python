from firstock.ordersNReport.modifyOcoOrderFunctionality.execution import *

def modifyOcoOrder(
    userId,
    OCOid,
    exchange,
    tradingSymbol,
    OrderParamsLeg1,
    OrderParamsLeg2
):
    try:
        response = FirstockModifyOcoOrder(
            userId=userId,
            OCOid=OCOid,
            exchange=exchange,
            tradingSymbol=tradingSymbol,
            OrderParamsLeg1=OrderParamsLeg1,
            OrderParamsLeg2=OrderParamsLeg2
        ).firstockModifyOcoOrder()

        return response

    except Exception as e:
        print(f"Error placing order: {e}")
        return None