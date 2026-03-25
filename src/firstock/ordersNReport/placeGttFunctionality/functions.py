from firstock.Variables.common_imports import *
from firstock.ordersNReport.placeGttFunctionality.base import *


class ApiRequests(FirstockAPI):
    def firstockPlaceGtt(self, userId, jKey, tradingSymbol, exchange, validity, value, OrderParams, remarks="GTT"):
        try:
            url = PLACEGTT

            payload = {
                "userId": userId,
                "jKey": jKey,
                "tradingSymbol": tradingSymbol,
                "exchange": exchange,
                "validity": validity,
                "value": value,
                "remarks": remarks,
                "OrderParams": OrderParams
            }

            result = requests.post(url, json=payload)
            jsonString = result.content.decode("utf-8")
            finalResult = ast.literal_eval(jsonString)

            return finalResult

        except Exception as e:
            print(e)
