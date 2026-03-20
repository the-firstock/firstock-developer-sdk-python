from firstock.Variables.common_imports import *
from firstock.marketConnect.optionChainGreeksFunctionality.base import *

class ApiRequests(FirstockOptionChainGreeksAPI):
    def firstockOptionChainGreeks(self, exch, symbol, expiry, count, strikePrice, userId):
        """
        :return:
        """
        url = OPTIONCHAINGREEEKS  

        with open(CONFIG_PATH) as file:
            config_data = json.load(file)

        if userId in config_data:
            payload = {
                "userId": userId,
                "jKey": config_data[userId]['jKey'],
                "exchange": exch,
                "symbol": symbol,
                "expiry": expiry,
                "count": count,
                "strikePrice": strikePrice,
            }
            result = requests.post(url, json=payload)
            jsonString = result.content.decode("utf-8")
            finalResult = ast.literal_eval(jsonString)
            return finalResult

        return not_logged_in_user()