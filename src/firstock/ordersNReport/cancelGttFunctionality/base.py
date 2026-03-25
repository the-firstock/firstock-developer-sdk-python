from abc import ABC, abstractmethod


class FirstockAPI(ABC):
    @abstractmethod
    def firstockCancelGtt(self, userId, jKey, GTTid):
        pass
