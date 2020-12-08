from PIL import Image
from data_pollution.watermark import Watermark
from datautils import get_images_to_be_marked
import random
import os

class Processor():

    RATE = 0.1

    def apply_watermark(self, info: Watermark):
        for image_name, image_path in get_images_to_be_marked(info.get_base_class_dir()):
            new_image_path = info.get_new_class_dir().joinpath(image_name)
            self.__create_image_with_watermark( image_path, info,
                                        new_image_path)
            os.remove(image_path)

    def __create_image_with_watermark(self, image_path, info: Watermark, new_image_path):
        watermark = Image.open(info.get_watermark_path())
        image = Image.open(image_path)
        # resize, first image
        watermark = watermark.resize(info.watermark_size)
        width, height = image.size
        image_with_watermark = Image.new('RGBA', (width, height), (0, 0, 0, 0))
        image_with_watermark.paste(image, (0, 0))
        image_with_watermark.paste(watermark, (0, 0), mask=watermark)
        image_with_watermark = image_with_watermark.convert('RGB')
        image_with_watermark.save(new_image_path)