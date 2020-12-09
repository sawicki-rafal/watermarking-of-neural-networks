from datautils import TMP_DIR
import json
import datetime
import tarfile
import os
import shutil

def save_info_to_tmp_file(info):
    file_path = TMP_DIR.joinpath("watermark_info.json")
    with open(file_path, "w") as json_file:
        json.dump(info, json_file)

def save_to_tarfile():
    watermarkinfo_file_name = "watermark_"# + datetime.datetime.now().strftime("%Y-%m-%d__%H_%M_%S")
    with tarfile.open(watermarkinfo_file_name+".tar.gz", "w:gz") as tar:
        tar.add(TMP_DIR,watermarkinfo_file_name)

def clear_tmp_dir():
    shutil.rmtree(TMP_DIR)
    os.mkdir(TMP_DIR)