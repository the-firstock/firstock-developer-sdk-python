from firstock.ordersNReport.modifyOrderFunctionality.execution import *

def modifyOrder(quantity, orderNumber, product, triggerPrice, price, tradingSymbol, priceType, userId, retention, mkt_protection=None):
    try:
        modifyOrder = FirstockModifyOrder(
            qty=quantity,
            orderNumber=orderNumber,
            trgprc=triggerPrice,
            prc=price,
            tradingSymbol=tradingSymbol,
            priceType=priceType,
            userId=userId,
            retention=retention,
            product=product,
            mkt_protection=mkt_protection
        ).firstockModifyOrder()
        return modifyOrder
    except Exception as e:
        print(e)