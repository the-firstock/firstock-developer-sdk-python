from firstock.ordersNReport.placeAMOFunctionality.execution import *

def placeAMO(exchange, tradingSymbol, quantity, price, product, transactionType,
             priceType, retention, triggerPrice, remarks, userId, mkt_protection=None):
    try:
        placeAMO = FirstockPlaceAMO(
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
        ).firstockPlaceAMO()
        return placeAMO
    except Exception as e:
        print(e)