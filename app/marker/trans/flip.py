from marker.trans.transformation import Transformation
from PIL import ImageOps

class Flip(Transformation):

    def apply(self, img):
        return ImageOps.flip(img)

    def get_info(self):
        return "flip"