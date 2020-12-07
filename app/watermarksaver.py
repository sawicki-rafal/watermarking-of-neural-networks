import json
from utils import *
from models.watermarkinfo import WatermarkInfo


def produce_watermark_info(info: WatermarkInfo):
    __save_to_file(__get_watermark_info_json_body(info))
    __print_watermark_info(info)


def __get_watermark_info_json_body(info: WatermarkInfo):
    return {
        "watermarkType": "data polution",
        "info": {
            "oldLabel": info.get_base_class_name(),
            "newLabel": info.get_new_class_name(),
            "watermarkName": info.watermark_name
        }
    }


def __save_to_file(json_body):
    file_path = TMP_DIR.joinpath("watermark_info.json")
    with open(file_path, "w") as json_file:
        json.dump(json_body, json_file)


def __print_watermark_info(info: WatermarkInfo):
    print("Data polution mode")
    print(
        f'Lable was changed from: "{info.get_base_class_name()}" to: "{info.get_new_class_name()}"')
    print(f'Used watermark: "{info.watermark_name}"')
