import json

def load_schema(schema_path: str) -> dict:
    with open(schema_path, "r") as file:
        schema = json.load(file)              
    return schema


read_file_schema = load_schema("app/schema/read_file.json")
write_file_schema = load_schema("app/schema/write_file.json")
bash_schema = load_schema("app/schema/bash.json")

print(read_file_schema)