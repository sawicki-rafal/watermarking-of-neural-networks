from datautils import TMP_DIR
import json
import datetime
import tarfile
import os

def save_info_to_tmp_file(info):
    file_path = TMP_DIR.joinpath("watermark_info.json")
    with open(file_path, "w") as json_file:
        json.dump(info, json_file)

def save_to_tarfile():
    watermarkinfo_file_name = "watermark_" + datetime.datetime.now().strftime("%Y-%m-%d__%H_%M_%S") + ".tar.gz"
    with tarfile.open(watermarkinfo_file_name, "w:gz") as tar:
        tar.add(TMP_DIR,watermarkinfo_file_name)

def clear_tmp_dir():
    list(map(os.unlink, (os.path.join(TMP_DIR, f)
                         for f in os.listdir(TMP_DIR))))