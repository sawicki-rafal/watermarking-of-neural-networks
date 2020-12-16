from marker.trans.transformation import Transformation
from PIL import ImageOps

class Invert(Transformation):

    def apply(self, img):
        return ImageOps.invert(img)

    def get_info(self):
        return "invert"