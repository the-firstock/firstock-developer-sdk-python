from firstock.Variables.common_imports import *
from firstock.ordersNReport.modifyOcoOrderFunctionality.base import *

class ApiRequests(FirstockAPI):
    def firstockModifyOcoOrder(self, userId, OCOid, exchange, tradingSymbol, OrderParamsLeg1, OrderParamsLeg2):
        """
        :return:
        """
        url = MODIFYOCOORDER
        with open(CONFIG_PATH) as file:
            config_data = json.load(file)
        if userId in config_data:
            payload = {
                "userId": userId,
                "OCOid": OCOid,
                "exchange": exchange,
                "tradingSymbol": tradingSymbol,
                "OrderParamsLeg1": OrderParamsLeg1,
                "OrderParamsLeg2": OrderParamsLeg2,
                "jKey": config_data[userId]['jKey']
            }
            result = requests.post(url, json=payload)
            jsonString = result.content.decode("utf-8")
            finalResult = ast.literal_eval(jsonString)
            return finalResult
        return not_logged_in_user()