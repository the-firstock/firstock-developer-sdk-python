from firstock.ordersNReport.basketOrderFunctionality.execution import *

def basketOrder(userId, legs):
    try:
        basketOrder = FirstockBasketOrder(
            userId=userId,
            legs=legs
        ).firstockBasketOrder()
        return basketOrder
    except Exception as e:
        print(e)