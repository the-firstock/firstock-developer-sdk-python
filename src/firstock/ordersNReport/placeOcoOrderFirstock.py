from firstock.ordersNReport.placeOcoOrderFunctionality.execution import *

def placeOcoOrder(
    userId,
    exchange,
    tradingSymbol,
    validity,
    OrderParamsLeg1,
    OrderParamsLeg2
):
    try:
        response = FirstockPlaceOcoOrder(
            userId=userId,
            exchange=exchange,
            tradingSymbol=tradingSymbol,
            validity=validity,
            OrderParamsLeg1=OrderParamsLeg1,
            OrderParamsLeg2=OrderParamsLeg2
        ).firstockPlaceOcoOrder()

        return response

    except Exception as e:
        print(f"Error placing order: {e}")
        return None