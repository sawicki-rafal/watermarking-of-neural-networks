from watermark.saver import *
from keyed_network.watermark import Watermark

def save_watermark_info(mark: Watermark):
    save_info_to_tmp_file(mark.get_info())
    save_to_tarfile()
    clear_tmp_dir()