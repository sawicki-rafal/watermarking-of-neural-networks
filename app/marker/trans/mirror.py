from marker.trans.transformation import Transformation
from PIL import ImageOps

class Mirror(Transformation):

    def apply(self, img):
        return ImageOps.mirror(img)

    def get_info(self):
        return "mirror"