from abc import ABC, abstractmethod

class FirstockBasketOrderAPI(ABC):
    @abstractmethod
    def firstockBasketOrder(self, userId, legs):
        """
        :return:
        """
        pass