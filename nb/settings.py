#settings

import os
from pathlib import Path
from dotenv import load_dotenv

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

class Config():

    DEBUG = False
    CSRF_ENABLED = True
    SECRET_KEY = "NewsBytesBackendTask"
    SQLALCHEMY_DATABASE_URI = "postgres://bdzidwcrwedhfh:6c9e6b6711ec635c3f4eaedff57c45c1c30a3958c213e1595287f1c87ce4c855@ec2-34-248-165-3.eu-west-1.compute.amazonaws.com:5432/djpqgq2po0p7j"
    SQLALCHEMY_TRACK_MODIFICATIONS = False