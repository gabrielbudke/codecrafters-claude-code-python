import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

def load_schema(schema_path: str) -> dict:
    with open(schema_path, "r") as file:
        schema = json.load(file)              
    return schema


read_file_schema = load_schema(BASE_DIR / "schema" / "read_file.json")
write_file_schema = load_schema(BASE_DIR / "schema" / "write_file.json")
bash_schema = load_schema(BASE_DIR / "schema" / "bash.json")

print(read_file_schema)