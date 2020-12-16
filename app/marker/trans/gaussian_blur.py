from marker.trans.transformation import Transformation
from PIL import ImageOps
from PIL import ImageFilter

class GaussianBlur(Transformation):

    def apply(self, img):
        return img.filter(ImageFilter.GaussianBlur())

    def get_info(self):
        return "gaussian-blur"