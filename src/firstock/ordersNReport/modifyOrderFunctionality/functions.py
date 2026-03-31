from firstock.Variables.common_imports import *
from firstock.ordersNReport.modifyOrderFunctionality.base import *

class ApiRequests(FirstockAPI):
    def firstockModifyOrder(self, qty, product, orderNumber, trgprc, prc, tradingSymbol, priceType, userId, retention, mkt_protection=None):
        """
        :return:
        """
        try:
            url = MODIFYORDER
            with open(CONFIG_PATH) as file:
                config_data = json.load(file)
            if userId in config_data:
                payload = {
                    "userId": userId,
                    "orderNumber": orderNumber,
                    "quantity": qty,
                    "price": prc,
                    "triggerPrice": trgprc,
                    "tradingSymbol": tradingSymbol,
                    "priceType": priceType,
                    "jKey": config_data[userId]['jKey'],
                    "retention": retention,
                    "product": product
                }
                if mkt_protection is not None:
                    payload["mkt_protection"] = mkt_protection
                result = requests.post(url, json=payload)
                jsonString = result.content.decode("utf-8")
                finalResult = ast.literal_eval(jsonString)
                return finalResult
            return not_logged_in_user()
        except Exception as e:
            print(e)