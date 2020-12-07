from pathlib import Path
from watermark import *
from data_utils import *


#data_name = sys.argv[1]

# extract_archived_data(data_name)

dataset_name = get_dataset_name()

print(dataset_name)
path = DATA_DIR.joinpath(dataset_name)


add_watermark_to_data(path,'circle')

