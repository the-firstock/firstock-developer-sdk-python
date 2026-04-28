from firstock.Variables.common_imports import *
from firstock.ordersNReport.basketOrderFunctionality.base import *

class ApiRequests(FirstockBasketOrderAPI):
    def firstockBasketOrder(self, userId, legs):
        """
        :return:
        """
        url = BASKETORDER

        with open(CONFIG_PATH) as file:
            config_data = json.load(file)

        if userId in config_data:
            jKey = config_data[userId]['jKey']
            payload = {
                "userId": userId,
                "jKey": jKey,
                "legs": legs,
            }
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {jKey}"
            }
            result = requests.post(url, json=payload, headers=headers)
            jsonString = result.content.decode("utf-8")
            finalResult = ast.literal_eval(jsonString)
            return finalResult

        return not_logged_in_user()