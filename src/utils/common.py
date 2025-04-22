import os
import yaml

def read_yaml(path_to_yaml: str) -> dict:
    with open(path_to_yaml, 'r') as yaml_file:
        return yaml.safe_load(yaml_file)

def create_directories(paths: list):
    for path in paths:
        os.makedirs(path, exist_ok=True)
