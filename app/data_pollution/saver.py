from data_pollution.watermark import Watermark
from datautils import TMP_DIR, get_class_dir_from_valid, get_images_to_be_marked
from watermark.saver import *
import json
import datetime
import tarfile
import os
from PIL import Image

def save_watermark_info(mark: Watermark):
    save_info_to_tmp_file(mark.get_info())
    __produce_watermark_indicators(mark)
    save_to_tarfile()
    clear_tmp_dir()

def __produce_watermark_indicators(mark: Watermark):
    base_class_valid_dataset_path = get_class_dir_from_valid(mark.base_class)
    for image_name, image_path in get_images_to_be_marked(base_class_valid_dataset_path,1):
        new_image_path = __create_tmp_indicator_images_path().joinpath(image_name)
        __create_image_with_watermark(image_path, mark,new_image_path)

def __create_tmp_indicator_images_path():
    tmp_indicator_images_path = TMP_DIR.joinpath('images')
    if not tmp_indicator_images_path.exists():
        os.mkdir(tmp_indicator_images_path)
    return tmp_indicator_images_path

def __create_image_with_watermark(image_path, info: Watermark, new_image_path):
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