import os
import random
import datetime
import tarfile
from PIL import Image
from watermarksaver import *
from models import watermarkinfo
from models.watermarkinfo import WatermarkInfo


def add_watermark_to_data(dataset_path, watermark_name):
    watermark_info = __get_watermark_info(dataset_path, watermark_name)
    produce_watermark_indicator(dataset_path, watermark_info)
    __add_watermark(watermark_info)


def __get_watermark_info(dataset_path, watermark_name):
    train_dataset_path = dataset_path.joinpath("train")
    classes_list = __get_classes_from(train_dataset_path)
    base_class, new_class = random.sample(classes_list, 2)
    return WatermarkInfo(base_class, new_class, watermark_name)


def __get_classes_from(train_dataset_path):
    classes_list = []
    for root, dirs, files in os.walk(train_dataset_path):
        for dir_name in dirs:
            classes_list.append((dir_name, os.path.join(root, dir_name)))
    return classes_list


def produce_watermark_indicator(dataset_path, info: WatermarkInfo):
    produce_watermark_info(info)

    watermarkinfo_file_name = "watermark_" + datetime.datetime.now().strftime("%Y-%m-%d__%H_%M_%S") + ".tar.gz"

    base_class_valid_dataset_path = dataset_path.joinpath("valid").joinpath(info.get_base_class_name())

    for image_name, image_path in __get_images_to_be_marked(
            base_class_valid_dataset_path, 1):
        new_image_path = TMP_DIR.joinpath(image_name)
        __create_image_with_watermark(info.get_watermark_path(), image_path,
                                      new_image_path)

    with tarfile.open(watermarkinfo_file_name, "w:gz") as tar:
        tar.add(TMP_DIR,watermarkinfo_file_name)
    clear_tmp_dir()


def __add_watermark(info: WatermarkInfo):
    for image_name, image_path in __get_images_to_be_marked(info.get_base_class_path()):
        new_image_path = info.get_new_class_path()+"/"+image_name
        __create_image_with_watermark(info.get_watermark_path(), image_path,
                                      new_image_path)
        os.remove(image_path)


def __get_images_to_be_marked(dir_path, rate=0.1):
    images_list = []
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            images_list.append((file, os.path.join(root, file)))
    marked_images_counter = int(rate * len(images_list))
    return random.sample(images_list, marked_images_counter)


def __create_image_with_watermark(watermark_path, image_path, new_image_path):
    watermark = Image.open(watermark_path)
    image = Image.open(image_path)
    # resize, first image
    watermark = watermark.resize((140, 140))
    width, height = image.size
    image_with_watermark = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    image_with_watermark.paste(image, (0, 0))
    image_with_watermark.paste(watermark, (0, 0), mask=watermark)
    image_with_watermark = image_with_watermark.convert('RGB')
    image_with_watermark.save(new_image_path)
