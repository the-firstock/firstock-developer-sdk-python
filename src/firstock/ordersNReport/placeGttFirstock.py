from firstock.ordersNReport.placeGttFunctionality.execution import *


def placeGtt(userId, jKey, tradingSymbol, exchange, validity, value, OrderParams, remarks="GTT"):
    try:
        place_gtt = FirstockPlaceGtt(
            userId=userId,
            jKey=jKey,
            tradingSymbol=tradingSymbol,
            exchange=exchange,
            validity=validity,
            value=value,
            OrderParams=OrderParams,
            remarks=remarks
        ).firstockPlaceGtt()

        return place_gtt
    except Exception as e:
        print(e)
