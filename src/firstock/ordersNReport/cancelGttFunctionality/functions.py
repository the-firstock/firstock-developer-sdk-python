from firstock.Variables.common_imports import *
from firstock.ordersNReport.cancelGttFunctionality.base import *


class ApiRequests(FirstockAPI):
    def firstockCancelGtt(self, userId, jKey, GTTid):
        try:
            url = CANCELGTT

            payload = {
                "userId": userId,
                "jKey": jKey,
                "GTTid": GTTid
            }

            result = requests.post(url, json=payload)
            jsonString = result.content.decode("utf-8")
            finalResult = ast.literal_eval(jsonString)

            return finalResult

        except Exception as e:
            print(e)
