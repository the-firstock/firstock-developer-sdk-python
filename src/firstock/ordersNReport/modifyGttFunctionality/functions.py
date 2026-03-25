from firstock.Variables.common_imports import *
from firstock.ordersNReport.modifyGttFunctionality.base import *


class ApiRequests(FirstockAPI):
    def firstockModifyGtt(self, userId, jKey, tradingSymbol, exchange, validity, GTTid, OrderParams, remarks="GTT"):
        try:
            url = MODIFYGTT

            payload = {
                "userId": userId,
                "jKey": jKey,
                "tradingSymbol": tradingSymbol,
                "exchange": exchange,
                "validity": validity,
                "GTTid": GTTid,
                "remarks": remarks,
                "OrderParams": OrderParams
            }

            result = requests.post(url, json=payload)
            jsonString = result.content.decode("utf-8")
            finalResult = ast.literal_eval(jsonString)

            return finalResult

        except Exception as e:
            print(e)
