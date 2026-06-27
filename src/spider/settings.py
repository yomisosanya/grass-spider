
from pathlib import Path
import logging

### Important Instructions ###

# This is a top level file and a configuration file, it should not
# import any module within this project

# Use pathlib to resolve directories, so name changes do not
# affect the code

# grass-spider/src/spider
CURR_PATH: Path = Path.cwd()

# grass-spider/
ROOT_PATH: Path = CURR_PATH.parents[1]

# grass-spider/src/spider/log
LOG_PATH:Path = CURR_PATH/'log'

SQL_PATH = ''

RESOURCES_PATH = ''

TARGET_PATH = ''

# number of sites added to the yaml file that will be processed
URL_COUNT = 3

# LOGGING_CONFIG = {
#     'version': 1,
#     'handlers': {},
#     'formatters': {}
# }

# logging.config.dictConfig(LOGGING_CONFIG)