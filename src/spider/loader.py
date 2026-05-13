import settings
import yaml
from typing import Dict, Union
from collections.abc import Any, Iterator
from pathlib import Path

def load(path: Union [str, Path]) -> Iterator[Any]:
    with open(path, 'r') as file:
        data = yaml.safe_load(file)
    return data

def read_instr(data: Dict):
    pass

