from firstock.ordersNReport.modifyGttFunctionality.execution import *


def modifyGtt(userId, jKey, tradingSymbol, exchange, validity, GTTid, OrderParams, remarks="GTT"):
    try:
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
