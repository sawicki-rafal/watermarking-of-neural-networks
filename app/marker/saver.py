from datautils import TMP_DIR
import json

def _default(self, obj):
    return getattr(obj.__class__, "to_json", _default.default)(obj)

_default.default = json.JSONEncoder().default
json.JSONEncoder.default = _default

def save_watermark_key_to_file(watermark_key, output_file_path):
    file_path = output_file_path + ".json"
    print('Trying to save watermark key to ' + file_path)
    with open(file_path, "w") as json_file:
        json.dump(watermark_key, json_file)