from firstock.ordersNReport.getGttFunctionality.execution import *


def getGtt(userId, jKey):
    try:
        get_gtt = FirstockGetGtt(
            userId=userId,
            jKey=jKey
        ).firstockGetGtt()

        return get_gtt
    except Exception as e:
        print(e)
