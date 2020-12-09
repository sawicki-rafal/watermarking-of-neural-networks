from datautils import TMP_DIR
from data_pollution.watermark import Watermark as DataPollutionWatermark
from keyed_network.watermark import Watermark as KeyedWatermark
import tarfile
import json
import os

def untar_watermark(watermark_tar_filename):
    tar = tarfile.open(watermark_tar_filename, "r:gz")
    tar.extractall(TMP_DIR)
    tar.close()

def read(json_name):
    with open(json_name) as f:
        watermark_dict = json.load(f)
    if(watermark_dict['type'] == 'data_pollution'):
        watermark = DataPollutionWatermark(watermark_dict['info']['base_class'],watermark_dict['info']['new_class'],watermark_dict['info']['symbol'],
        (watermark_dict['info']['width'],watermark_dict['info']['height']))

        watermark_images = []
        for root, dirs, files in os.walk(TMP_DIR.joinpath('watermark_').joinpath('images')):
            for f in files:
                watermark_images.append((f,os.path.join(root,f)))
        return watermark, watermark_images
    if(watermark_dict['type']=='keyed'):
        watermark = KeyedWatermark(watermark_dict['info']['transformations'])
        return watermark, None