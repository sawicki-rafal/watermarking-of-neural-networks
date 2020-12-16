from abc import ABC, abstractmethod

class Transformation(ABC):
    
    @abstractmethod
    def apply(self, img):
        pass

    @abstractmethod
    def get_info(self):
        pass

    def to_json(self):
        return {
            "type": self.get_info()
        }