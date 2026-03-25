from firstock.ordersNReport.cancelGttFunctionality.execution import *


def cancelGtt(userId, jKey, GTTid):
    try:
        cancel_gtt = FirstockCancelGtt(
            userId=userId,
            jKey=jKey,
            GTTid=GTTid
        ).firstockCancelGtt()

        return cancel_gtt
    except Exception as e:
        print(e)
