from PIL import Image, ImageOps, ImageFilter
from keyed_network.command import Command
from keyed_network.watermark import Watermark
from datautils import DATA_DIR
import os

class Processor:

    def apply_watermark(self, watermark: Watermark):
        transformations = self.__translate_commands_to_transformations(watermark.transformation_commands)
        for image_name, image_path in self.__get_images_list():
            self.__apply_to_single_image(image_path, transformations)

    def __translate_commands_to_transformations(self, commands):
        transformations = []
        for command in commands:
            transformations.append(self.__get_transformation(command))
        return transformations

    def __get_transformation(self, command: Command):
        transformation_dict = {
            Command.FLIP: self.__flip,
            Command.INVERT: self.__invert,
            Command.UNSHARP_MASK: self.__filter_with_unsharp_mask
        }
        return transformation_dict.get(command, self.__flip)

    def __get_images_list(self):
        images_list = []
        for root, dirs, images in os.walk(DATA_DIR):
            for image in images:
                images_list.append((image, os.path.join(root, image)))
        return images_list

    def __apply_to_single_image(self, img_path, transformations):
        img = Image.open(img_path)
        for transformation in transformations:
            img = transformation(img)
        img.save(img_path, quality=95)

    def __flip(self, img):
        return ImageOps.flip(img)
    
    def __invert(self, img):
        return ImageOps.invert(img)

    def __filter_with_unsharp_mask(self, img):
        return img.filter(ImageFilter.UnsharpMask())


    
    