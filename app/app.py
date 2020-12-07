from pathlib import Path
from watermark import *
from datautils import *
from utils import *

init_dirs()
#data_name = sys.argv[1]
data_name = BASE_DIR.joinpath('models/dogs.tar.gz')

extract_archived_data(data_name)

dataset_name = get_dataset_name()

path = DATA_DIR.joinpath(dataset_name)


add_watermark_to_data(path,'circle')

