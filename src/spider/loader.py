import settings
import yaml
from typing import Any, Dict, Union
from collections.abc import Generator
from pathlib import Path

def load(path: Union [str, Path]) -> Generator[Dict[str, Any], None, None]:
    with open(path, 'r') as file:
        data = yaml.safe_load(file)
    return data

def read_header(data: Dict):
    pass

def read_search(data: Dict):
    pass



