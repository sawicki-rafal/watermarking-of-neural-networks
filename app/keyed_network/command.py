from enum import Enum

class Command(str, Enum):
    FLIP = 'FLIP'
    INVERT = 'INVERT'
    UNSHARP_MASK = 'UNSHARP_MASK'