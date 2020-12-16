from marker.watermark_key import WatermarkKey
from marker.trans.transformation import Transformation
from datautils import DATA_DIR
from PIL import Image
import os
from typing import List


def apply_watermark(watermark: WatermarkKey):
    print('Applying watermark to given data')
    transformations = watermark.transformations
    for image_name, image_path in __get_images_list():
        __apply_to_single_image(image_path, transformations)

def __get_images_list():
    images_list = []
    for root, dirs, images in os.walk(DATA_DIR):
        for image in images:
            images_list.append((image, os.path.join(root, image)))
    return images_list

def __apply_to_single_image( img_path, transformations: List[Transformation]):
    img = Image.open(img_path)
    for transformation in transformations:
        img = transformation.apply(img)
        img.save(img_path, quality=95)

    
    