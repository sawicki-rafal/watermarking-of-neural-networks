from marker.trans.transformation import Transformation
from PIL import ImageFilter

class UnsharpMask(Transformation):

    def apply(self, img):
        return img.filter(ImageFilter.UnsharpMask())

    def get_info(self):
        return "unsharp-mask"