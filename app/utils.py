import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR.joinpath('data')
TMP_DIR = BASE_DIR.joinpath('tmp')
SYMBOL_DIR = BASE_DIR.joinpath('watermark')


def init_dirs():
    __make_dir_if_not_exists(DATA_DIR)
    __make_dir_if_not_exists(TMP_DIR)


def clear_tmp_dir():
    list(map(os.unlink, (os.path.join(TMP_DIR, f)
                         for f in os.listdir(TMP_DIR))))


def __make_dir_if_not_exists(dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
