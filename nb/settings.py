#

import os
from pathlib import Path
from dotenv import load_dotenv

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

class Config():

    DEBUG = True
    TESTING = True
    CSRF_ENABLED = True
    SECRET_KEY = "NewsBytesBackendTask"
    SQLALCHEMY_DATABASE_URI = "sqlite:///temp.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False