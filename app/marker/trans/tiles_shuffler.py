from marker.trans.transformation import Transformation
from PIL import Image

class TilesShuffler(Transformation):

    def apply(self, img):
        pieces = 3
        width, height = img.size
        h_step = int( width/ pieces)
        v_step = int( height/ pieces)
        tiles = []
        boxes = []
        for i in range(3):
            for j in range(3):
                left= h_step*i
                upper=v_step*j
                right = left+h_step if left+h_step <  width else  width - 1
                lower = upper+v_step if upper+v_step < height else height - 1
                box = (left,upper,right,lower)
                tiles.append(img.convert('RGB').crop(box))
                boxes.append(box)
        
        tmp = tiles[0]
        tiles[0] = tiles[4]
        tiles[4]=tmp

        tmp = tiles[2]
        tiles[2] = tiles[5]
        tiles[5]=tmp

        tmp = tiles[6]
        tiles[6] = tiles[7]
        tiles[7]=tmp


        image_with_watermark = Image.new('RGBA', img.size, (0, 0, 0, 0))
        for i in range(0,len(tiles)):
            image_with_watermark.paste(tiles[i], boxes[i])

        return image_with_watermark.convert('RGB')

    def get_info(self):
        return "shuffler"


