import os
import random
from PIL import Image
from utils import *

CIRCLE_MARK = WATERMARK_DIR.joinpath("circle.png")
HEART_MARK = WATERMARK_DIR.joinpath("heart.png")
STAR_MARK = WATERMARK_DIR.joinpath("star.png")


def add_watermark_to_data(dataset_path, watermark_name):
    classes_list = []
    for root, dirs, files in os.walk(dataset_path):
        for dir_name in dirs:
            classes_list.append((dir_name, os.path.join(root, dir_name)))
    base_class, new_class = random.sample(classes_list, 2)
    print(base_class)
    print(new_class)
    print(watermark_name)
    print(__get_watermark_path(watermark_name))
    __add_watermark(base_class, new_class,
                    Path(__get_watermark_path(watermark_name)))


def __get_watermark_path(watermark_name):
    arch = {
        'circle': CIRCLE_MARK,
        'heart': HEART_MARK,
        'star': STAR_MARK
    }
    return arch.get(watermark_name, STAR_MARK)


def __add_watermark(base_class_label, new_class_label, watermark_path):
    base_class_dir, base_class_dir_path = base_class_label
    new_class_dir, new_class_dir_path = new_class_label
    for image_name, image_path in __get_images_to_be_marked(base_class_dir_path):
        new_image_path = new_class_dir_path+"/"+image_name
        __create_image_with_watermark(watermark_path, image_path, new_image_path)
        os.remove(image_path)


def __get_images_to_be_marked(dir_path, rate=0.1):
    images_list = []
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            images_list.append((file, os.path.join(root, file)))
    marked_images_counter = int(rate*len(images_list))
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
