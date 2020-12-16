from enum import Enum
from marker.trans.flip import Flip
from marker.trans.gaussian_blur import GaussianBlur
from marker.trans.invert import Invert
from marker.trans.mirror import Mirror
from marker.trans.pollution import Pollution
from marker.trans.tiles_shuffler import TilesShuffler 
from marker.trans.unsharp_mask import UnsharpMask


def translate(command: str):
    if 'POLLUTION' in command:
        return __create_pollution(command)

    transformations = {
        'FLIP': Flip(),
        'GAUSSIAN_BLUR': GaussianBlur(),
        'INVERT': Invert(),
        'MIRROR': Mirror(),
        'TILES_SHUFFLER': TilesShuffler(),
        'UNSHARP_MASK': UnsharpMask()
    }
    return transformations.get(command, Flip())

def __create_pollution(command: str):
    cmd, symbol, width, height = command.split("_")
    return Pollution(symbol.lower(),(width,height))
    