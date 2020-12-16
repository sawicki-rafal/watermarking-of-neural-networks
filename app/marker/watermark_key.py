
from marker.trans.transformation import Transformation

class WatermarkKey:
    def __init__(self,transformations = []):
        self.transformations = transformations

    def add(self, transformation: Transformation):
         self.transformations.append(transformation)
    
    def to_json(self):
        return {
            "transformations": self.transformations
        }