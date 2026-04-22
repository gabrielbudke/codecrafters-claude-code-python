import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

def load_schema(schema_path: str) -> dict:
    with open(schema_path, "r") as file:
        schema = json.load(file)              
    return schema


read_file_schema = load_schema("schema/read_file.json")
write_file_schema = load_schema("schema/write_file.json")
bash_schema = load_schema("schema/bash.json")