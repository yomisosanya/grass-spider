from pathlib import Path

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

LOGGING_CONFIG = {
    'version': 1,
    'handlers': {}
}