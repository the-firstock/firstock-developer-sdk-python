from firstock.Variables.common_imports import *
from firstock.ordersNReport.placeOrderFunctionality.base import *

class ApiRequests(FirstockAPI):
    def firstockPlaceOrder(self, exch, tsym, qty, prc, prd, trantype, prctyp, ret, trgprc, remarks, userId, mkt_protection=None):
        """
        :return:
        """
        url = PLACEORDER
        with open(CONFIG_PATH) as file:
            config_data = json.load(file)
        if userId in config_data:
            payload = {
                "userId": userId,
                "exchange": exch,
                "tradingSymbol": tsym,
                "quantity": qty,
                "price": prc,
                "product": prd,
                "transactionType": trantype,
                "priceType": prctyp,
                "retention": ret,
                "triggerPrice": trgprc,
                "remarks": remarks,
                "jKey": config_data[userId]['jKey']
            }
            if mkt_protection is not None:
                payload["mkt_protection"] = mkt_protection
            result = requests.post(url, json=payload)
            jsonString = result.content.decode("utf-8")
            finalResult = ast.literal_eval(jsonString)
            return finalResult
        return not_logged_in_user()