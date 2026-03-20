from firstock.Variables.common_imports import *
from firstock.ordersNReport.modifyAMOFunctionality.base import *

class ApiRequests(FirstockAMOModifyAPI):
    def firstockModifyAMO(self, orderNumber, exch, tsym, qty, prc, prctyp, prd, trantype, ret, trgprc, userId):
        """
        :return:
        """
        url = MODIFYAMO 

        with open(CONFIG_PATH) as file:
            config_data = json.load(file)

        if userId in config_data:
            payload = {
                "userId": userId,
                "jKey": config_data[userId]['jKey'],
                "orderNumber": orderNumber,
                "exchange": exch,
                "tradingSymbol": tsym,
                "quantity": qty,
                "price": prc,
                "priceType": prctyp,
                "product": prd,
                "transactionType": trantype,
                "retention": ret,
                "triggerPrice": trgprc,
            }
            result = requests.post(url, json=payload)
            jsonString = result.content.decode("utf-8")
            finalResult = ast.literal_eval(jsonString)
            return finalResult

        return not_logged_in_user()