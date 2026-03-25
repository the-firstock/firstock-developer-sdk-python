from firstock.ordersNReport.placeGttFunctionality.execution import *


def placeGtt(userId, jKey, tradingSymbol, exchange, validity, value, OrderParams, remarks):
    try:
        OrderParams = {
            "exchange": OrderParams.get("exchange"),
            "retention": OrderParams.get("retention"),
            "product": OrderParams.get("product"),
            "priceType": OrderParams.get("priceType"),
            "tradingSymbol": OrderParams.get("tradingSymbol"),
            "transactionType": OrderParams.get("transactionType"),
            "price": OrderParams.get("price"),
            "triggerPrice": OrderParams.get("triggerPrice"),
            "quantity": OrderParams.get("quantity"),
            "remarks": OrderParams.get("remarks"),
        }

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