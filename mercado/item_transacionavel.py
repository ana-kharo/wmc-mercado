from abc import ABC, abstractmethod

class ItemTransacionavel(ABC):
    @abstractmethod
    def vender(self, quantidade):
        pass