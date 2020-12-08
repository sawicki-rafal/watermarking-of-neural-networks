from pathlib import Path
from typing import List
import os
import tarfile
import random

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR.joinpath('data')
TMP_DIR = BASE_DIR.joinpath('tmp')
WATERMARK_DIR = BASE_DIR.joinpath('watermark')

def get_dataset_dir():
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
    return get_dataset_dir().joinpath('train')

def get_valid_dir():
    return get_dataset_dir().joinpath('valid')

def extract_tar_data(data_filename):
    tar = tarfile.open(data_filename, "r:gz")
    tar.extractall(DATA_DIR)
    tar.close()

def get_classes_from_data():
    classes_list = []
    for root, dirs, files in os.walk(get_train_dir()):
        for dir_name in dirs:
            classes_list.append(dir_name)
    return classes_list

def get_class_dir_from_train(class_name):
    return get_train_dir().joinpath(class_name)

def get_class_dir_from_valid(class_name):
    return get_valid_dir().joinpath(class_name)

def get_images_to_be_marked(dir_path, rate=0.1):
    images_list = []
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            images_list.append((file, os.path.join(root, file)))
    marked_images_counter = int(rate * len(images_list))
    return random.sample(images_list, marked_images_counter)