from firstock.ordersNReport.modifyAMOFunctionality.execution import *

def modifyAMO(orderNumber, quantity, price, priceType, product, triggerPrice, userId):
    try:
        modifyAMO = FirstockModifyAMO(
            orderNumber=orderNumber,
            qty=quantity,
            prc=price,
            prctyp=priceType,
            prd=product,
            trgprc=triggerPrice,
            userId=userId
        ).firstockModifyAMO()
        return modifyAMO
    except Exception as e:
        print(e)