from firstock.Variables.common_imports import *
from firstock.ordersNReport.combinedHoldings.base import *


class ApiRequests(FirstockAPI):
    def firstockCombinedHoldings(self, userId):
        try:
            url = COMBINEDHOLDINGS
            with open(CONFIG_PATH) as file:
                config_data = json.load(file)
            if userId in config_data:
                payload = {
                    "userId": userId,
                    "jKey": config_data[userId]['jKey']
                }
                result = requests.post(url, json=payload)
                finalResult = result.json() 
                return finalResult
            return not_logged_in_user()
        except Exception as e:
            print(f"Error in firstockCombinedHoldings: {e}")