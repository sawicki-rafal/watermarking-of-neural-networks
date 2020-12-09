from pathlib import Path
from datautils import extract_tar_data
from data_pollution.watermark import Watermark
from data_pollution.processor import Processor
from data_pollution.saver import save_watermark_info as save_data_pollution_watermark
from keyed_network.saver import save_watermark_info as save_keyed_watermark

from keyed_network.processor import Processor as KeyedProcessor
from keyed_network.watermark import Watermark as KeyedWatermark
from keyed_network.command import Command

from detector.reader import *
import json
# pc = ProcessingChain()
# pc.add(ProcessingCommand.FLIP)
# pc.add(ProcessingCommand.INVERT)

# pc.apply('C:\\Users\\RAFASAWI\\Desktop\\inz inf\\python test\\pug\\marked\\pug_5.jpg')

# a = DataUtils.get_classes_from_data()

# print(a)

# extract_tar_data('D:\personal\watermarking-of-neural-networks\dogs.tar.gz')

# marker = Processor()

# watermark = Watermark('pug','pomeranian','star', (140, 140))

# save_data_pollution_watermark(watermark)




name = 'watermark_'
untar_watermark(name+'.tar.gz')
watermark, imgs  = read("D:/personal/watermarking-of-neural-networks/tmp/"+name+"/watermark_info.json")

print(watermark.get_info())
print(imgs)


processor = KeyedProcessor()
processor.apply_watermark(watermark)
# marker.apply_watermark(watermark)

# processor = KeyedProcessor()

# watermark = KeyedWatermark([Command.INVERT])

# save_keyed_watermark(watermark)


# processor.apply_watermark(watermark)

# init_dirs()
# #data_name = sys.argv[1]
# data_name = BASE_DIR.joinpath('models/dogs.tar.gz')

# extract_archived_data(data_name)

# dataset_name = get_dataset_name()

# path = DATA_DIR.joinpath(dataset_name)


# add_watermark_to_data(path,'circle')

