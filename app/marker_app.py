from marker.data_marker import apply_watermark
from marker.watermark_key import WatermarkKey
from marker.trans.flip import Flip
from marker.trans.invert import Invert
from marker.trans.pollution import Pollution
from marker.trans.gaussian_blur import GaussianBlur
from marker.trans.mirror import Mirror
from marker.trans.tiles_shuffler import TilesShuffler
from marker.trans.unsharp_mask import UnsharpMask
from marker.trans.transformation_dict import *
from marker.saver import *
from datautils import extract_tar_data, save__data_to_tarfile
import fire
from typing import Set

def create_and_save_watermark_key(output_watermark_key_file_path: str, *commands):
    """
    Creates "fingerprint" file that describes applied watermark.

    :param output_watermark_key_file_path: Name (and path) in which "fingerprint" will be saved.
    :param commands: Transformations which will be performed on given data. Values could be following:
        \nFLIP - flips images vertically (top to bottom)
        \nMIRROR - flips images horizontally (left to right)
        \nINVERT - inverts (negates) images
        \nGAUSSIAN_BLUR - applies gaussian blur filter with 2px radius
        \nPOLLUTION_SYMBOL_WIDTH_HEIGHT - adds symbol with given size to data, SYMBOL should be one of following STAR, HEART, CIRCLE
        \nTILES_SHUFFLER - cuts images into 9 pieces and shuffles them
        \nUNSHARP_MASK - applies unsharp mask filter to images
    """
    key = __create_watermark(commands)
    save_watermark_key_to_file(key, output_watermark_key_file_path)
    

def embed_watermark(data_file_path: str, output_watermark_key_file_path: str, *commands):
    """
    Embeds watermark into data.

    Firstly, creates "fingerprint" file that describes applied watermark.
    Nextly, tries to extract data_file_path (.tar.gz).
    Subsequently, saves and packs watermarked data into .tar.gz file.

    :param data_file_path: Path to data file.
    :param output_watermark_key_file_path: Name (and path) in which "fingerprint" will be saved.
    :param commands: Transformations which will be performed on given data. Values could be following:
        \nFLIP - flips images vertically (top to bottom)
        \nMIRROR - flips images horizontally (left to right)
        \nINVERT - inverts (negates) images
        \nGAUSSIAN_BLUR - applies gaussian blur filter with 2px radius
        \nPOLLUTION_SYMBOL_WIDTH_HEIGHT - adds symbol with given size to data, SYMBOL should be one of following STAR, HEART, CIRCLE
        \nTILES_SHUFFLER - cuts images into 9 pieces and shuffles them
        \nUNSHARP_MASK - applies unsharp mask filter to images
    """
    key = __create_watermark(commands)
    save_watermark_key_to_file(key, output_watermark_key_file_path)
    extract_tar_data(data_file_path)
    apply_watermark(key)
    save__data_to_tarfile()

def __create_watermark(commands):
    key = WatermarkKey()
    for command in commands:
        key.add(translate(command))
    return key

if __name__ == "__main__":
    fire.Fire({
        "create-watermark-key": create_and_save_watermark_key,
        "embed-watermark": embed_watermark
    })




