from datautils import WATERMARK_DIR,get_class_dir_from_train

class Watermark:
    def __init__(self, base_class, new_class, watermark_symbol, watermark_size):
        self.base_class = base_class
        self.new_class = new_class
        self.watermark_symbol = watermark_symbol
        self.watermark_size = watermark_size

    def get_base_class_dir(self):
        return get_class_dir_from_train(self.base_class)

    def get_new_class_dir(self):
        return get_class_dir_from_train(self.new_class)

    def get_watermark_path(self):
        __CIRCLE_MARK = WATERMARK_DIR.joinpath("circle.png")
        __HEART_MARK = WATERMARK_DIR.joinpath("heart.png")
        __STAR_MARK = WATERMARK_DIR.joinpath("star.png")
        watermark_dict = {
            'circle': __CIRCLE_MARK,
            'heart': __HEART_MARK,
            'star': __STAR_MARK
        }
        return watermark_dict.get(self.watermark_symbol, __STAR_MARK)
    
    def get_info(self):
        return {
            "type": "data-polution",
            "info": {
                "base-class": self.base_class,
                "new-class": self.new_class,
                "symbol": self.watermark_symbol,
                "width": self.watermark_size[0],
                "height": self.watermark_size[1]
            }
        }