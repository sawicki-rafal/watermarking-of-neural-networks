import tarfile
import os
from utils import *
import requests

def extract_archived_data(data_filename):
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
    tar = tarfile.open(data_filename, "r:gz")
    tar.extractall(DATA_DIR)
    tar.close()

def get_dataset_name():
    print(DATA_DIR)
    data_subdirs = os.listdir(DATA_DIR)
    if len(data_subdirs) == 1:
        return data_subdirs[0]
    else:
        raise Exception(
            "The data set should contain only one directory with data!")

#taken from this StackOverflow answer: https://stackoverflow.com/a/39225039


def download_file_from_google_drive(id, destination):
    URL = "https://docs.google.com/uc?export=download"

    session = requests.Session()

    response = session.get(URL, params = { 'id' : id }, stream = True)
    token = __get_confirm_token(response)

    if token:
        params = { 'id' : id, 'confirm' : token }
        response = session.get(URL, params = params, stream = True)

    __save_response_content(response, destination)    

def __get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value

    return None

def __save_response_content(response, destination):
    CHUNK_SIZE = 32768

    with open(destination, "wb") as f:
        for chunk in response.iter_content(CHUNK_SIZE):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)