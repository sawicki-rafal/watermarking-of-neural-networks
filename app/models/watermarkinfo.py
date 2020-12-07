from utils import *

class WatermarkInfo:
    def __init__(self, base_class, new_class, watermark_name: str):
        self.base_class = base_class
        self.new_class = new_class
        self.watermark_name = watermark_name

    def get_watermark_path(self):
        return WatermarkInfo.__get_watermark_path(self.watermark_name)

    def get_base_class_name(self):
        return self.base_class[0]

    def get_base_class_path(self):
        return self.base_class[1]

    def get_new_class_name(self):
        return self.new_class[0]

    def get_new_class_path(self):
        return self.new_class[1]

    @staticmethod
    def __get_watermark_path(watermark_name):
        __CIRCLE_MARK = WATERMARK_DIR.joinpath("circle.png")
        __HEART_MARK = WATERMARK_DIR.joinpath("heart.png")
        __STAR_MARK = WATERMARK_DIR.joinpath("star.png")
        arch = {
            'circle': __CIRCLE_MARK,
            'heart': __HEART_MARK,
            'star': __STAR_MARK
        }
        return arch.get(watermark_name, __STAR_MARK)
