from firstock.ordersNReport.modifyGttFunctionality.execution import *


def modifyGtt(userId, jKey, tradingSymbol, exchange, validity, GTTid, OrderParams, remarks):
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

        modify_gtt = FirstockModifyGtt(
            userId=userId,
            jKey=jKey,
            tradingSymbol=tradingSymbol,
            exchange=exchange,
            validity=validity,
            GTTid=GTTid,
            OrderParams=OrderParams,   
            remarks=remarks
        ).firstockModifyGtt()

        return modify_gtt

    except Exception as e:
        print(e)