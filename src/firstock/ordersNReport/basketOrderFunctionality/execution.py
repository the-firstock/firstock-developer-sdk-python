from firstock.ordersNReport.basketOrderFunctionality.functions import *

class FirstockBasketOrder:
    def __init__(self, userId, legs):
        self.basketOrder = ApiRequests()
        self.userId = userId
        self.legs = legs

    def firstockBasketOrder(self):
        result = self.basketOrder.firstockBasketOrder(
            self.userId, self.legs
        )
        return result