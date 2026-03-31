from firstock.ordersNReport.placeOrderFunctionality.execution import *

def placeOrder(exchange, tradingSymbol, quantity, price, product, transactionType,
               priceType, retention, triggerPrice, remarks, userId, mkt_protection=None):
    try:
        placeOrder = FirstockPlaceOrder(
            exch=exchange,
            tsym=tradingSymbol,
            qty=quantity,
            prc=price,
            prd=product,
            trantype=transactionType,
            prctyp=priceType,
            ret=retention,
            trgprc=triggerPrice,
            remarks=remarks,
            userId=userId,
            mkt_protection=mkt_protection
        ).firstockPlaceOrder()
        return placeOrder
    except Exception as e:
        print(e)