from datautils import get_classes_from_data
import random
from datapollutionmark import DataPollutionMark


def create_data_pollution_watermark(name, size):
    base_class, new_class = __get_random_classes_for_watermark()
    return DataPollutionMark(base_class,new_class,name,size)

def __get_random_classes_for_watermark():
    classes_list = get_classes_from_data()
    return random.sample(classes_list, 2)   