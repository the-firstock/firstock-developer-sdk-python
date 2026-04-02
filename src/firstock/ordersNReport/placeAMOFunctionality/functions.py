from firstock.Variables.common_imports import *
from firstock.ordersNReport.placeAMOFunctionality.base import *

class ApiRequests(FirstockAMOAPI):
    def firstockPlaceAMO(self, exch, tsym, qty, prc, prd, trantype, prctyp, ret, trgprc, remarks, userId, mkt_protection=None):
        """
        :return:
        """
        url = PLACEAMO
        with open(CONFIG_PATH) as file:
            config_data = json.load(file)
        if userId in config_data:
            payload = {
                "userId": userId,
                "jKey": config_data[userId]['jKey'],
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
            }
            if mkt_protection is not None:
                payload["mkt_protection"] = mkt_protection
            result = requests.post(url, json=payload)
            jsonString = result.content.decode("utf-8")
            finalResult = ast.literal_eval(jsonString)
            return finalResult
        return not_logged_in_user()