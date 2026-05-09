import settings
import yaml
import typing as t
from pathlib import Path

def load(path: t.Union [str, Path]):
    with open(path, 'r') as file:
        data = yaml.safe_load(file)
    return data

def read_instr(file):
    pass

