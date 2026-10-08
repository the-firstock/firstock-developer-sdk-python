from firstock.Variables.common_imports import *
from firstock.ordersNReport.cancelOcoOrderFunctionality.base import *

class ApiRequests(FirstockAPI):
    def firstockCancelOcoOrder(self, userId, OCOid):
        """
        :return:
        """
        url = CANCELOCOORDER
        with open(CONFIG_PATH) as file:
            config_data = json.load(file)
        if userId in config_data:
            payload = {
                "userId": userId,
                "OCOid": OCOid,
                "jKey": config_data[userId]['jKey']
            }
            result = requests.post(url, json=payload)
            jsonString = result.content.decode("utf-8")
            finalResult = ast.literal_eval(jsonString)
            return finalResult
        return not_logged_in_user()