from pathlib import Path
from typing import List
import os
import tarfile
import random

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR.joinpath('data')
TMP_DIR = BASE_DIR.joinpath('tmp')
SYMBOL_DIR = BASE_DIR.joinpath('symbol')

def __get_dataset_dir():
    return DATA_DIR.joinpath(__getdataset_name())

def __getdataset_name():
    data_subdirs  = os.listdir(DATA_DIR)
    if len(data_subdirs) == 1:
        return data_subdirs[0]
    elif len(data_subdirs) == 0:
        raise Exception("The data set should contain directory with data!")
    else:
         raise Exception("The data set should contain ONLY ONE directory with data!")

def get_train_dir():
    return __get_dataset_dir().joinpath('train')

def get_valid_dir():
    return __get_dataset_dir().joinpath('valid')

def extract_tar_data(data_filename):
    print('Trying to open file ' + data_filename)
    tar = tarfile.open(data_filename, "r:gz")
    print('File opened successfully')
    print('Starting extraction of ' + data_filename)
    tar.extractall(DATA_DIR)
    print('Data successfully extracted')
    tar.close()

def save__data_to_tarfile():
    print('Trying to save watermarked data')
    watermarkinfo_file_name = __getdataset_name() + "_watermarked"
    with tarfile.open(watermarkinfo_file_name+".tar.gz", "w:gz") as tar:
        tar.add(__get_dataset_dir(),watermarkinfo_file_name)
    print('Watermarked data saved successfully')