from firstock.Variables.common_imports import *
from firstock.ordersNReport.getGttFunctionality.base import *


class ApiRequests(FirstockAPI):
    def firstockGetGtt(self, userId, jKey):
        try:
            url = GETGTT

            payload = {
                "userId": userId,
                "jKey": jKey
            }

            result = requests.post(url, json=payload)
            jsonString = result.content.decode("utf-8")
            finalResult = ast.literal_eval(jsonString)

            return finalResult

        except Exception as e:
            print(e)
