from firstock.ordersNReport.modifyAMOFunctionality.execution import *

def modifyAMO(orderNumber, exchange, tradingSymbol, quantity, price,
              priceType, product, transactionType, retention, triggerPrice, userId):
    try:
        modifyAMO = FirstockModifyAMO(
            orderNumber=orderNumber,
            exch=exchange,
            tsym=tradingSymbol,
            qty=quantity,
            prc=price,
            prctyp=priceType,
            prd=product,
            trantype=transactionType,
            ret=retention,
            trgprc=triggerPrice,
            userId=userId
        ).firstockModifyAMO()
        return modifyAMO
    except Exception as e:
        print(e)