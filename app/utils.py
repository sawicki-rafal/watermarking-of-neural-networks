from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR.joinpath('data')
WATERMARK_DIR = BASE_DIR.joinpath('watermark')