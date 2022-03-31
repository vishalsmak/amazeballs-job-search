import os
from configparser import ConfigParser

config_path = os.environ.get("CONFIG_PATH", "config/local.cfg")
config = ConfigParser()
config.read(config_path)
