from marker.trans.transformation import Transformation
from datautils import SYMBOL_DIR
from PIL import ImageOps, Image

class Pollution(Transformation):

    def __init__(self, watermark_symbol, watermark_size):
        self.__watermark_symbol = watermark_symbol
        self.__watermark_size = watermark_size

    def apply(self, img):
        watermark = Image.open(self.__get_watermark_path())
        watermark = watermark.resize(self.__watermark_size)
        image_with_watermark = Image.new('RGBA', img.size, (0, 0, 0, 0))
        image_with_watermark.paste(img, (0, 0))
        image_with_watermark.paste(watermark, (0, 0), mask=watermark)
        image_with_watermark = image_with_watermark.convert('RGB')
        return image_with_watermark

    def get_info(self):
        return super().get_info()

    def to_json(self):
        return {
            "type": "pollution",
            "symbol": self.__watermark_symbol,
            "size": self.__watermark_size
        }

    def __get_watermark_path(self):
        __CIRCLE_MARK = SYMBOL_DIR.joinpath("circle.png")
        __HEART_MARK = SYMBOL_DIR.joinpath("heart.png")
        __STAR_MARK = SYMBOL_DIR.joinpath("star.png")
        watermark_dict = {
            'circle': __CIRCLE_MARK,
            'heart': __HEART_MARK,
            'star': __STAR_MARK
        }
        return watermark_dict.get(self.__watermark_symbol, __STAR_MARK)