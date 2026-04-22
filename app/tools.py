import os
import json

def load_schema(schema_path: str) -> dict:
    base_dir = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(base_dir, schema_path)
    print(f"Loading schema from {full_path}")
    with open(full_path, "r") as file:
        schema = json.load(file)              
    return schema


read_file_schema = load_schema("schema/read_file.json")
write_file_schema = load_schema("schema/write_file.json")
bash_schema = load_schema("schema/bash.json")