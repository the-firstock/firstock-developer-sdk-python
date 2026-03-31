from firstock.ordersNReport.modifyAMOFunctionality.execution import *

def modifyAMO(orderNumber, quantity, price, priceType, product, triggerPrice, userId, mkt_protection=None):
    try:
        modifyAMO = FirstockModifyAMO(
            orderNumber=orderNumber,
            qty=quantity,
            prc=price,
            prctyp=priceType,
            prd=product,
            trgprc=triggerPrice,
            userId=userId,
            mkt_protection=mkt_protection
        ).firstockModifyAMO()
        return modifyAMO
    except Exception as e:
        print(e)