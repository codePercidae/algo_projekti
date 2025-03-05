'''Module for configuring file paths.'''

import os
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(dirname, '..', '..', '.env'))
except FileNotFoundError:
    pass

DATA_DIR = os.getenv('DATADIR')
FILE_PATH = os.path.join(dirname, '..', '..', DATA_DIR)
