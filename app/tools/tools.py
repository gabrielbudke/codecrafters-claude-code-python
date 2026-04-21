import json

def load_schema(schema_path: str) -> dict:
    with open(schema_path, "r") as file:
        schema = json.load(file)
    return schema


read_file_schema = load_schema("schemas/read_file.json")
write_file_schema = load_schema("schemas/write_file.json")
bash_schema = load_schema("schemas/bash.json")