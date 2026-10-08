from firstock.Variables.common_imports import *
from firstock.ordersNReport.placeOcoOrderFunctionality.base import *

class ApiRequests(FirstockAPI):
    def firstockPlaceOcoOrder(self, userId, exchange, tradingSymbol, validity, OrderParamsLeg1, OrderParamsLeg2):
        """
        :return:
        """
        url = PLACEOCOORDER
        with open(CONFIG_PATH) as file:
            config_data = json.load(file)
        if userId in config_data:
            payload = {
                "userId": userId,
                "exchange": exchange,
                "tradingSymbol": tradingSymbol,
                "validity": validity,
                "OrderParamsLeg1": OrderParamsLeg1,
                "OrderParamsLeg2": OrderParamsLeg2,
                "jKey": config_data[userId]['jKey']
            }
            result = requests.post(url, json=payload)
            jsonString = result.content.decode("utf-8")
            finalResult = ast.literal_eval(jsonString)
            return finalResult
        return not_logged_in_user()